#!/usr/bin/env python3
"""Fetch public pages as plain text and archive them with a URL registry.

Every quote you publish must come from an archived copy, so quotes can be
re-verified later (verify_quotes.py --registry). Uses official JSON APIs
where they exist, because they are more stable than HTML:

  Discourse forum topic  https://<forum>/t/<slug>/<id>  -> /t/<id>.json (all posts)
  Hacker News item       news.ycombinator.com/item?id=N -> hn.algolia.com/api/v1/items/N
  GitHub issue / PR      github.com/<o>/<r>/issues/N    -> api.github.com (+ comments)
  V2EX topic             v2ex.com/t/N                   -> /api/topics/show.json + replies
  Reddit post            reddit.com/r/<s>/comments/<id> -> Arctic Shift API (post + comments)
  anything else          raw HTML, scripts/styles stripped

Files: OUT/<md5-12>.txt with a header (URL, JSON meta), registry at
OUT/registry.json: {url: {"file", "kind", "title", "date"}}.

Examples:
  python3 archive_page.py https://forum.obsidian.md/t/some-topic/118339 --out pages
  python3 archive_page.py --print 400 https://news.ycombinator.com/item?id=12345 --out pages
Be polite: one request at a time, retries back off; respect robots/ToS.
"""
import argparse, datetime, hashlib, html, json, os, re, sys, time, urllib.parse, urllib.request

UA = "Mozilla/5.0 (research archiver; contact: site owner)"
ARCTIC = "https://arctic-shift.photon-reddit.com/api"


def get(url, tries=3, timeout=30):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json,text/html;q=0.9"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:  # 429/403/timeouts: back off, then give up honestly
            last = e
            time.sleep(2 + 3 * i)
    print(f"FAIL {url}: {last}", file=sys.stderr)
    return None


def getj(url, **k):
    b = get(url, **k)
    try:
        return json.loads(b) if b else None
    except ValueError:
        return None


def strip(h):
    h = re.sub(r"<(script|style|noscript)[^>]*>.*?</\1>", "", h or "", flags=re.S | re.I)
    h = re.sub(r"<br\s*/?>|</p>|</li>|</h\d>|</blockquote>|</div>", "\n", h, flags=re.I)
    return re.sub(r"\n\s*\n+", "\n\n", html.unescape(re.sub(r"<[^>]+>", "", h))).strip()


def utc(ts):
    return datetime.datetime.fromtimestamp(int(ts), datetime.timezone.utc).strftime("%Y-%m-%d")


def discourse(url, m):
    base, tid = m.group(1), m.group(2)
    j = getj(f"{base}/t/{tid}.json?print=true", tries=1) or getj(f"{base}/t/{tid}.json")
    if not j:
        return None
    parts = [f"TITLE: {j.get('title')}\nCREATED: {j.get('created_at')}"]
    for p in j["post_stream"]["posts"]:
        parts.append(f"--- post#{p['post_number']} {p['created_at']}\n{strip(p.get('cooked', ''))}")
    return "discourse", j.get("title"), (j.get("created_at") or "")[:10], "\n".join(parts)


def hn(url, m):
    j = getj(f"https://hn.algolia.com/api/v1/items/{m.group(1)}")
    if not j:
        return None
    out = []
    def walk(n, d=0):
        out.append(f"--- {'  ' * d}{n.get('type')} {n.get('created_at', '')[:10]}\n{strip(n.get('title') or '')}\n{strip(n.get('text') or '')}")
        for c in n.get("children") or []:
            walk(c, d + 1)
    walk(j)
    return "hn", j.get("title"), (j.get("created_at") or "")[:10], "\n".join(out)


def github(url, m):
    repo, num = m.group(1), m.group(2)
    i = getj(f"https://api.github.com/repos/{repo}/issues/{num}")
    if not i:
        return None
    cs = getj(f"https://api.github.com/repos/{repo}/issues/{num}/comments?per_page=100") or [] if i.get("comments") else []
    txt = f"TITLE: {i['title']}\nCREATED: {i['created_at']}\n\n{i.get('body') or ''}\n"
    txt += "".join(f"\n--- comment {c['created_at']}\n{c.get('body') or ''}\n" for c in cs)
    return "github", i["title"], i["created_at"][:10], txt


def v2ex(url, m):
    tid = m.group(1)
    t = getj(f"https://www.v2ex.com/api/topics/show.json?id={tid}")
    if not t:
        return None
    t = t[0]
    rs = getj(f"https://www.v2ex.com/api/replies/show.json?topic_id={tid}") or []
    txt = f"TITLE: {t['title']}\nCREATED: {utc(t['created'])}\n\n{t.get('content', '')}\n"
    txt += "".join(f"\n--- reply {utc(r['created'])}\n{r['content']}\n" for r in rs)
    return "v2ex", t["title"], utc(t["created"]), txt


def reddit(url, m):
    pid = m.group(1)
    p = getj(f"{ARCTIC}/posts/ids?ids={pid}", timeout=60)
    if not p or not p.get("data"):
        return None
    p = p["data"][0]
    cs = (getj(f"{ARCTIC}/comments/search?link_id={pid}&limit=100", timeout=60) or {}).get("data") or []
    txt = f"TITLE: {p.get('title')}\nCREATED: {utc(p['created_utc'])}\n\n{p.get('selftext') or ''}\n"
    txt += "".join(f"\n--- comment {utc(c['created_utc'])}\n{c.get('body', '')}\n" for c in sorted(cs, key=lambda c: c["created_utc"]))
    return "reddit", p.get("title"), utc(p["created_utc"]), txt


def generic(url, m):
    h = get(url)
    if not h:
        return None
    title = (re.search(r"<title[^>]*>(.*?)</title>", h, re.S | re.I) or [None, ""])[1].strip()
    return "web", html.unescape(title), "", strip(h)


ROUTES = [
    (r"^(https?://[^/]+)/t/(?:[^/]*[^/\d][^/]*/)?(\d+)", discourse),
    (r"news\.ycombinator\.com/item\?id=(\d+)", hn),
    (r"github\.com/([^/]+/[^/]+)/(?:issues|pull)/(\d+)", github),
    (r"v2ex\.com/t/(\d+)", v2ex),
    (r"reddit\.com/r/[^/]+/comments/([a-z0-9]+)", reddit),
    (r".", generic),
]


def archive(url, out):
    for rx, fn in ROUTES:
        m = re.search(rx, url)
        if m:
            res = fn(url, m)
            break
    if not res:
        return None, None
    kind, title, date, text = res
    os.makedirs(out, exist_ok=True)
    fn = hashlib.md5(url.encode()).hexdigest()[:12] + ".txt"
    meta = {"kind": kind, "title": title, "date": date, "fetched": datetime.date.today().isoformat()}
    open(os.path.join(out, fn), "w", encoding="utf-8").write(f"URL: {url}\n{json.dumps(meta, ensure_ascii=False)}\n\n{text}")
    regp = os.path.join(out, "registry.json")
    reg = json.load(open(regp, encoding="utf-8")) if os.path.exists(regp) else {}
    reg[url] = {"file": fn, **meta}
    json.dump(reg, open(regp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return fn, text


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("urls", nargs="+")
    ap.add_argument("--out", default="pages")
    ap.add_argument("--print", type=int, default=0, help="print the first N chars of each page")
    a = ap.parse_args()
    for u in a.urls:
        fn, text = archive(u, a.out)
        print(("SAVED " + fn if fn else "FAIL"), u, sep="\t")
        if fn and a.print:
            print(text[: a.print], "\n")
        time.sleep(1)


if __name__ == "__main__":
    main()

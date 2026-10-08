
# MDFriday Content Strategy Outline  
  
制定目标，方向，原则，用于指导 MDFriday 的内容策略，确保内容产出与 SEO、用户需求和产品定位一致。  
  
## 1. 目标  
  
让内容系统保持连贯，职责清晰，并体现专业性。   
增强 MDFriday 社区信任度，提升 MDFriday 在搜索引擎中的可见性，吸引潜在用户，提高付费转化率。  
  
## 2. 定位  
  
MDFriday 作者是 孙伟(sun wei)，英文名 Wayde Sun.  
  
### sunwei.xyz  
  
个人官网：sunwei.xyz, 用来 build in public，记录 MDFriday 的开发、运营和营销过程。讲述的是一个程序员如何将自己的知识变成自己的资产，除了打工，多了一种生活方式。   
  
### mdfriday.com  
  
MDFriday 官网：mdfriday.com, 用来承接所有关键词，发布产品页、指南和比较文章。内容以帮助用户解决实际问题。官网一级菜单包括：产品、解决方案、主题、定价页、资源，其中资源里可以包含博客，帮助中心，对比，alternative 等。目前以 Obsidian 应用场景为主，但最终定位还是一个 Markdown Publishing 平台，未来将慢慢将定位改变成 Markdown Publishing 平台，将用户的知识转变成资产，可以为用户带来被动收入。  
  
#### SEO 基本原则  
  
-  sitemap.xml 收录所有产品、解决方案、主题、定价页、资源（博客、帮助中心、对比、alternative 等）等承接页和长尾博客。  
- 每页独立的 title 和 description，主词放在前 60 个字符内。  
- canonical 指向自身；EN（/）与 ZH（/zh/）的 hreflang 要保证正确。  
- 博客文章加 Article JSON-LD（作者、发布和更新时间），比较页写明「最后核对日期」。  
- Obsidian 社区插件页的描述和官网口径一致（品牌搜索的第一结果）。  
- SEO Priority = Intent × Business Value × Product Fit × Ranking Feasibility，而不仅仅只是搜索声量  
- Homepage 不要堆砌关键词，不负责覆盖所有关键词，而负责定义网站主题，并把权重传递给 Product / Solution / Guide 页面。 要符合 Primary Keyword，Secondary Keyword，Tertiary Keyword 的分布原则。  
  
#### 竞争策略  
  
- 最低的试用门槛：在 Obsidian 里直接发布，无需账号、无需配置，10秒钟，从插件安装到第一个站点发布上线；  
- 最划算的多站点：无限站点，一个自定义域名，5G 一年 50$， 再加两个自定义域名，10$每年，总共 60$ 每年；  
- Local-first，不上传笔记到云端，本地构建，本地预览，本地导出 - no vendor lock-in  
- 竞争对手：  
  - 官方托管：Obsidian Publish  
  - 托管 + 开源核心：Flowershow - 核心竞争对手  
  - 托管 + Forestry.md， Digital Garden 插件 - 核心竞争对手  
  - 开源 SSG：Quartz  
  - 开源插件 + Vercel：Digital Garden 插件自托管  
  - 托管：Markbase  
  - 托管（邀请制 beta）：Sidian  
  - 托管：Mixa  
  - 单篇分享托管：Docferry  
  
## 3. 原则  
  
- Help-first: Google 喜欢的不只是「10 Best X」，还有真实问题 + 真实 workflow + 真实结果。从内容及评论获取用户真实问题，提供帮助，然后完善 MDFriday 相关的内容。  
- 客观公正： 不夸大、不贬低、不抹黑，事实为主，数据为证。对比竞品时，列出事实和来源，说明 MDFriday 的优势和局限。  
  
## SEO 整体策略  
  
MDFriday 的 SEO 战略浓缩成一句：  
  
> **Use Obsidian to enter the market, use Markdown to expand the market, use real publishing use cases to capture search intent, and use content + community to turn search traffic into users.**  
  
### 采用 **7 层关键词体系**  
  
```text
                         MDFriday SEO                              │             ┌────────────────┼────────────────┐             │                │                │          BOFU              MOFU              TOFU             │                │                │       Alternative          Intent          Problem             │                │                │             └────────────────┼────────────────┘                              │                       Use Case / Category                              │                    ┌─────────┼─────────┐                    │         │         │                 Markdown   Digital    Feature                            Garden  
```
  
下面这张表，是 MDFriday 的 **Keyword Strategy Master Table**。  
  
> **注意：这里的搜索量需要进一步确认和处理。**  > 需要从网络上真实获取对应的搜索量和商业价值等关键数据信息  
  
  
| Priority | Category | Keyword / Keyword Cluster | Search Intent | 商业价值 | MDFriday 匹配度 | 建议页面 | 当前状态 |  
|---|---|---|---|---:|---:|---|---|  
| **P0** | Alternative | **obsidian publish alternative** | BOFU | ★★★★★ | ★★★★★ | Product | 🔴 必做 |  
| **P0** | Alternative | **quartz alternative** | BOFU | ★★★★★ | ★★★★★ | Product | 🔴 必做 |  
| **P0** | Alternative | **flowershow alternative** | BOFU | ★★★★★ | ★★★★★ | Product | 🔴 必做 |  
| **P0** | Intent | **publish obsidian notes** | BOFU | ★★★★★ | ★★★★★ | Product | 🔴 必做 |  
| **P0** | Intent | **obsidian website** | BOFU/MOFO | ★★★★★ | ★★★★★ | Product | 🔴 必做 |  
| **P0** | Intent | **create website from obsidian** | BOFU | ★★★★★ | ★★★★★ | Product | 🔴 必做 |  
| **P0** | Problem | **publish obsidian without github** | BOFU | ★★★★★ | ★★★★★ | Guide/Product | 🔴 必做 |  
| **P0** | Problem | **obsidian website without coding** | BOFU | ★★★★★ | ★★★★★ | Guide/Product | 🔴 必做 |  
| **P0** | Use Case | **markdown website** | Commercial | ★★★★★ | ★★★★★ | Category | 🔴 必做 |  
| **P0** | Use Case | **markdown website builder** | Commercial | ★★★★★ | ★★★★★ | Product | 🔴 必做 |  
| **P0** | Use Case | **markdown wiki** | Commercial | ★★★★☆ | ★★★★★ | Use Case | 🔴 必做 |  
| **P1** | Use Case | **markdown blog** | Commercial | ★★★★☆ | ★★★★★ | Use Case | 🟠 |  
| **P1** | Use Case | **markdown docs** | Commercial | ★★★★☆ | ★★★★★ | Use Case | 🟠 |  
| **P1** | Use Case | **markdown knowledge base** | Commercial | ★★★★☆ | ★★★★★ | Use Case | 🟠 |  
| **P1** | Digital Garden | **obsidian digital garden** | Commercial | ★★★★☆ | ★★★★★ | Use Case | 🟢 已有 |  
| **P1** | Digital Garden | **digital garden tool** | Commercial | ★★★★☆ | ★★★★☆ | Category | 🟠 |  
| **P1** | Digital Garden | **digital garden platform** | Commercial | ★★★★☆ | ★★★★☆ | Category | 🟠 |  
| **P1** | Intent | **obsidian blog** | Commercial | ★★★★☆ | ★★★★★ | Product/Use Case | 🟠 |  
| **P1** | Intent | **share obsidian notes** | BOFU | ★★★★★ | ★★★★★ | Use Case | 🟢 已有 |  
| **P1** | Intent | **publish obsidian folder** | BOFU | ★★★★★ | ★★★★★ | Product | 🟠 |  
| **P1** | Problem | **how to publish obsidian notes** | Informational → Commercial | ★★★★☆ | ★★★★★ | Guide | 🟢 Blog |  
| **P1** | Problem | **how to create obsidian website** | Informational → Commercial | ★★★★☆ | ★★★★★ | Guide | 🟠 |  
| **P1** | Problem | **how to host obsidian website** | Commercial | ★★★★☆ | ★★★★★ | Guide | 🟠 |  
| **P1** | Problem | **obsidian publish custom domain** | Commercial | ★★★★★ | ★★★★★ | Guide/Product | 🟠 |  
| **P1** | Markdown | **publish markdown website** | Commercial | ★★★★☆ | ★★★★★ | Product | 🟠 |  
| **P1** | Markdown | **markdown publishing platform** | Commercial | ★★★★☆ | ★★★★★ | Product | 🟠 |  
| **P1** | Markdown | **markdown blog platform** | Commercial | ★★★★☆ | ★★★★☆ | Use Case | 🟠 |  
| **P1** | Markdown | **markdown knowledge management** | MOFU | ★★★☆☆ | ★★★★☆ | Guide | 🟠 |  
| **P2** | Alternative | **digital garden plugin alternative** | BOFU | ★★★★☆ | ★★★★☆ | Comparison | 🟠 |  
| **P2** | Alternative | **hugo alternative** | BOFU | ★★★☆☆ | ★★★★☆ | Comparison | 🟡 |  
| **P2** | Alternative | **markdown website builder alternative** | BOFU | ★★★★☆ | ★★★★☆ | Comparison | 🟡 |  
| **P2** | Intent | **publish markdown files** | Commercial | ★★★★☆ | ★★★★★ | Product | 🟡 |  
| **P2** | Intent | **turn markdown into website** | Commercial | ★★★★☆ | ★★★★★ | Product | 🟢 Homepage |  
| **P2** | Intent | **markdown to website** | Commercial | ★★★★★ | ★★★★★ | Category | 🟡 |  
| **P2** | Problem | **markdown website without coding** | Commercial | ★★★★☆ | ★★★★★ | Product/Guide | 🟡 |  
| **P2** | Problem | **publish markdown without github** | Commercial | ★★★★☆ | ★★★★★ | Guide | 🟡 |  
| **P2** | Digital Garden | **digital garden obsidian** | Commercial | ★★★★☆ | ★★★★★ | Use Case | 🟢 已有 |  
| **P2** | Digital Garden | **obsidian wiki** | Commercial | ★★★★☆ | ★★★★★ | Use Case | 🟠 |  
| **P2** | Digital Garden | **obsidian knowledge base** | Commercial | ★★★★☆ | ★★★★★ | Use Case | 🟠 |  
| **P2** | Feature | **obsidian wikilinks website** | Informational | ★★★☆☆ | ★★★★★ | Guide | 🟡 |  
| **P2** | Feature | **markdown mermaid website** | Informational | ★★☆☆☆ | ★★★★☆ | Guide | 🟡 |  
| **P2** | Feature | **markdown latex website** | Informational | ★★☆☆☆ | ★★★★☆ | Guide | 🟡 |  
| **P3** | Educational | **what is a digital garden** | TOFU | ★★☆☆☆ | ★★★☆☆ | Guide | ⚪ |  
| **P3** | Educational | **what is markdown** | TOFU | ★☆☆☆☆ | ★★☆☆☆ | Guide | ⚪ |  
| **P3** | Educational | **markdown syntax** | TOFU | ★☆☆☆☆ | ★★★☆☆ | Guide | ⚪ |  
| **P3** | Educational | **how does markdown work** | TOFU | ★☆☆☆☆ | ★★☆☆☆ | Guide | ⚪ |  
  
- **P0**，现在就做，直接影响获取第一批付费用户。  
- **P1**，未来 1–2 个月做，形成 SEO topic cluster。  
- **P2**，建立 topical authority 后做。  
- **P3**，暂时不追求流量。  
  
### MDFriday 官网 Information Architecture  
  
```text  
/home  
│  
├── /products/  
│   ├── /obsidian-publish/  
│   ├── /obsidian-sync/  
│   └── /studio/  
│  
├── /solutions/  
│   ├── /share-a-note/  
│   ├── /digital-garden/  
│   ├── /markdown-blog/  
│   ├── /markdown-wiki/  
│   ├── /markdown-docs/  
│   └── /knowledge-base/  
├── /themes/  
├── /pricing/  
├── /resources/  
│   └── /compare/  
│      ├── /obsidian-publish-alternative/  
│      ├── /flowershow-alternative/  
│      ├── /quartz-alternative/  
│      └── /digital-garden-plugin-alternative/  
│   └── /guides/  
│      ├── /publish-obsidian-without-github/  
│      ├── /obsidian-website-without-coding/  
│      ├── /publish-markdown-website/  
│      └── ...  
│   └── /blog/  
│   └── /docs/  
│  
└── ...  
```  
  
其中 compare，guides 的 URL 结构是一级目录，如/obsidian-publish-alternative/，更短，且方便 SEO topic cluster 的建立。  
  
所有页面的内容结构遵循 The Inverted Pyramid 原则，先给出直接答案，再给出详细信息。   
  
**这种结构（倒金字塔结构，Inverted Pyramid）的核心好处：**  
  
在 AI 时代，内容不仅要让人读懂，更要让 **Google AI Overview、ChatGPT、Perplexity 等 AI 系统快速提取答案**。  
  
采用倒金字塔结构：  
  
1. **先给答案，再给解释**  
    - 用户几秒钟内就能获得核心信息。  
   - AI 也能立即识别页面的主要结论。  
  
2. **更容易被 AI 引用**  
    - AI 模型会优先寻找能够直接回答问题的内容。  
   - 答案放在开头，相当于主动告诉 AI：  
      > “这就是你要找的答案。”  
  
3. **提高 Featured Snippet 和 AI Overview 的概率**  
    - Google 更容易抽取你的内容作为摘要。  
   - AI 搜索结果更容易把你当作引用来源。  
  
4. **降低信息提取成本**  
    - AI 不需要阅读大量背景故事才能找到结论。  
   - 用户也不会因为冗长引言而流失。  
  
**推荐结构：**  
  
```text  
标题（直接对应搜索问题）  
  
1. 直接答案（50~150字）  
   ↓2. 具体步骤 / 核心方法  
   ↓3. 细节说明  
   ↓4. 常见问题（FAQ）  
   ↓5. 相关扩展内容  
```  
  
例如用户搜索：  
  
> How to publish Obsidian notes with Quartz  
  
不要这样写：  
  
```text  
我从 2021 年开始使用 Obsidian...  
Quartz 是一个很流行的项目...  
```  
  
而应该直接写：  
  
```text  
How to Publish Obsidian Notes with Quartz  
  
The fastest way to publish Obsidian notes with Quartz is:  
  
1. Export your notes.  
2. Build the Quartz site.  
3. Deploy to Cloudflare Pages, Vercel, or GitHub Pages.  
  
The entire process takes about 10 minutes.  
```  
  
然后再展开介绍 Quartz、部署细节、常见问题等。  
  
**一句话总结：**  
  
> 在 AI 搜索时代，内容结构比过去更重要。最有效的写法是“答案优先（Answer First）”，先让 AI 和用户立刻看到结论，再逐层补充细节。这样更容易被 AI 摘要、引用和推荐。  
  
### Blog 的定位  
  
不应该再“随机写”，以后每一篇 Blog 发布之前必须回答：这篇文章服务哪个 Keyword Cluster？  
  
例如文章 - 《How to Publish Obsidian Notes Without GitHub》，它服务：publish obsidian without github SEO 关键词，然后还要链接到 /obsidian-publish-alternative/ ， /solutions/share-a-note/，/products/obsidian-publish/ 页面。   
  
还需要增加一个结构：  
  
```text  
Article  
   ↓Solution Page  
   ↓Product Page  
   ↓CTA  
```  
  
不能浪费掉每一次的机会。  
  
### 建立 Internal Linking System  
  
以后每一个页面至少有：  
  
```text  
1 Product link  
2 Solution links  
1 Guide link  
1 Comparison link  
1 CTA  
```  
  
例如：  
  
```text  
Markdown Wiki  
      │      ├── Obsidian Publish      ├── Digital Garden      ├── Markdown Website      ├── Quartz Alternative      └── Publish Folder Guide  
```  
  
这样 Google 才能形成：  
  
```text  
Topic Cluster  
```  
  
### 建立 SEO Content → Marketing 的统一流水线  
  
**一份内容可以同时服务 SEO + Reddit + YouTube + Indie Hackers + Product Marketing。**  
  
我建议以后每一个 Topic 都这样：  
  
```text  
                     Core Topic                         │                ┌────────┴────────┐                │                 │             SEO Page          Experience                │                 │          Google ranking       Reddit                │              YouTube                │          Indie Hackers                │                 │                └────────┬────────┘                         ↓                    Product                         ↓                     Signup                         ↓                    Publish                         ↓                    Paid user  
```  
  
举一个完整例子  
  
Topic：Publish Obsidian Without GitHub  
  
- SEO：/obsidian-publish-without-github/  
- Blog：Why Publishing Obsidian Notes Became a GitHub Problem   
- Reddit：I wanted to publish an Obsidian folder without GitHub, so I built this   
- YouTube：Obsidian → Live Website Without GitHub， 30 秒  
- Product： CTA - Install MDFriday Publish   
- Comparison 链接：Obsidian Publish Alternative ，Quartz Alternative  
  
保证要建立起完整的 marketing loop。   
  
### SEO 系统架构  
  
把 MDFriday 的增长系统定义成：  
  
```text  
                 KEYWORD                    │                    ↓                SEO PAGE                    │             ┌──────┴──────┐             ↓             ↓          Product        Guide             │             │             └──────┬──────┘                    ↓                 DEMO                    ↓               INSTALL                    ↓                 PUBLISH                    ↓                WEBSITE                    ↓              PAID USER  
```  
  
然后再从每一个核心页面反向生成：  
  
```text  
Reddit  
YouTube  
Indie Hackers  
X  
Community  
Newsletter  
```  
  
### SEO Dashboard  
  
以后每周只看这几个指标：  
  
| Metric | 目标 |  
|---|---|  
| Indexed pages | ↑ |  
| Keywords in Top 100 | ↑ |  
| Keywords in Top 20 | ↑ |  
| Keywords in Top 10 | ↑ |  
| Organic impressions | ↑ |  
| Organic clicks | ↑ |  
| CTR | ↑ |  
| Organic signups | ↑ |  
| Organic publishes | ↑ |  
| Organic paid users | **最重要** |  
  
并以  **这些访问有没有产生 Publish？有没有产生付费？** 为目标
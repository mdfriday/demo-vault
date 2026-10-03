# Hugo Playground

The experience of building a site with Hugo is great.
The first is that it is fast to build, and the second is that it is easy to use, 
a `hugo` command, and our site is ready.

During the construction process, 
Hugo provides a wealth of built-in functions that can provide you with almost any site-related information you need during the construction process.
Let the theme help with all presentation and layout related issues through reusable templates.
Allow authors to focus more on content creation.

## Playground

The construction of the site will transform the written content into website resources that the web server can understand.
For example, when we write, we use Markdown format, and the generated website resources are usually in HTML format.


Here is a simple initialization blog content:
```
-- config.toml --
theme = "mytheme"
contentDir = "mycontent"
-- myproject.txt --
Hello project!
-- themes/mytheme/mytheme.txt --
Hello theme!
-- mycontent/blog/post.md --
---
title: "Post Title"
---
### first blog
Hello Blog
-- layouts/index.html --
{{ $entries := (readDir ".") }}
START:|{{ range $entry := $entries }}{{ if not $entry.IsDir }}{{ $entry.Name }}|{{ end }}{{ end }}:END:
-- layouts/_default/single.html --
{{ .Content }}
===
Static Content
===

```

You can see that we have customized a theme **mytheme**, 
there is only one mytheme.txt file, and there is no actual template file.
This will help us understand how themes are nested and loaded in the construction process below.

Our content folder is **mycontent**, 
and there is a simple blog post /blog/post.md under the blog directory.
If you want to visit this blog post independently, 
you need to generate an HTML file for her so that we can visit it in the browser.

In the sample, in order to generate the homepage and blog, 
we also created two templates under layouts.
One is the homepage template index.html, 
and the other is the template _default/single.html that will be used in a single article.

By parsing the above text through golang tools txtar, 
it is convenient for us to convert it into a disk file with the following structure:
```
.
├── config.toml
├── layouts
│  ├── _default
│  │   └── single.html
│  └── index.html
├── mycontent
│   └── blog
│     └── post.md
├── myproject.txt
└── themes
    └── mytheme
        └── mytheme.txt
```

Building through the Hugo command can generate the following site resources:

```
➜  public tree
.
├── blog
│   └── index.html
├── index.html
└── robots.txt
```

and contains the information we want:

### Site Home

```
➜  public cat index.html

START:|config.toml|myproject.txt|:END:%
```

### Blog Page

```
➜  public cat blog/index.html
<h3 id="first-blog">first blog</h3>
<p>Hello Blog</p>

===
Static Content
===

  %
```

So how did Hugo's magic come about?

In order to understand the core principles of Hugo construction, 
the latest source code of Hugo is trimmed to remove unnecessary "noise" at the current stage.
Combined with our above example, 
a minimal working source library - [hugo playground](https://github.com/gitaction/hugo-palyground) was manually generated.
To ensure that we can play to our heart's content in this playground, 
focus on the core principles, and enjoy the entire source code learning process.

By command:

```
git ls-files | grep '\.go' | xargs wc -l
```

Count the code lines of [gohugoio/hugo](https://github.com/gohugoio/hugo) 
and [hugo playground](https://github.com/gitaction/hugo-palyground) respectively.
The data we get are **163075** and **33990** rows respectively.

**It has been reduced by nearly four times! **

I believe that all the judges will be shocked, 
and their confidence will double! Looking at the source code can be so happy.
Please prepare the melon seed drink bench, and listen carefully to the judges.

### Show Me The Code

```go
package main

import (
	"bytes"
	"fmt"
	"path/filepath"

	"golang.org/x/tools/txtar"
)

// 文件结构
// 文件名: config.toml
// 文件内容：theme = 'mytheme'
var files = "-- config.toml --\n" +
	"theme = 'mytheme'"

func main() {
	// 解析上面的文件结构
	data := txtar.Parse([]byte(files))
	fmt.Println("File start:")

	// 遍历解析生成的所有文件，通过File结构体获取文件名和文件数据
	// f.Name 获取文件名
	// f.Data 获取文件数据
	for _, f := range data.Files {
		filename := filepath.Join("workingDir", f.Name)
		data := bytes.TrimSuffix(f.Data, []byte("\n"))

		fmt.Println(filename)
		fmt.Println(string(data))
	}
	fmt.Println("File end.")
}
```
Output:
```text
# 解析后得到文件config.toml，以及下面的文件内容
# workingDir就是我们的工作目录，通常是要写入的文件目录

File start:
workingDir/config.toml
theme = 'mytheme'
File end.
```

[Try it yourself](https://c.sunwei.xyz/txtar.html)
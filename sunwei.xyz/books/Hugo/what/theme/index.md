# 自定义Hugo主题

Hugo可以创建站点，还可以创建自己的主题。
以站点[sunwe.xyz](https://sunwei.xyz)为例。
让我们将站点中的内容和主题分离，让我们专注在内容创作上。
同时还可以让更多和我们有共同诉求的人，重用我们的主题。

## 需求分析

我们的目标是分离出站点的主题，也就是将content和layouts，及static分离开，并作为主题引入。

所需要的步骤如下：

* 创建主题仓库
* 将模板样式从原有站点分离出来
* 引入主题

## 实施细节

接下来我们一步步的实现以上需求。

### 创建主题仓库

因为站点定位个人品牌，需求并不复杂，以简洁为主。
我们给主题取名`zero`，寓意起点。

首先创建好空的zero Github仓库，再用Hugo命令生成主题默认目录结构：
```shell
➜  zero git:(main) ✗ hugo new theme .
Creating theme at /Users/sunwei/github/sunwei/zero/themes
➜  zero git:(main) ✗ ls
LICENSE   README.md public    resources themes
```

可以看出，Hugo认为我们是在站点里，正在给站点创建主题。
实际上我们需要的是themes里面的内容。
在我们的实例中，其实就`theme.toml`这一个主题配置文件。
拷贝到我们的仓库根目录下后，更新其中说明内容如下：
```toml
name = "Zero"
license = "MIT"
licenselink = "https://github.com/sunwei/zero/blob/master/LICENSE"
description = "Hugo Theme for sunewi.xyz"
homepage = "https://sunwei.xyz/"
demosite = "https://sunwei.xyz"
tags = ["zero", "sunwei.xyz"]
features = ["clean"]
min_version = "0.41.0"

[author]
  name = "Sun Wei"
  homepage = "https://sunwei.xyz"

```

其它的文件都可以移除掉，因为我们并不是从零开始创建一个主题，而是将sunwei.xyz站点的主题独立出来。

为了让主题支持用模块的形式导入，我们还需要在仓库根目录下创建一个golang的模块文件`go.mod`，并更新内容如下：
```go
module github.com/sunwei/zero

go 1.18
```
这是因为Hugo模块是基于Golang模块开发的。
上面的代码第一行表示的是这个go模块的名字`github.com/sunwei/zero`，如果想导入这个模块，就需要导入这个索引。
第二行表示支持的go版本。

准备好主题配置信息和Golang模块信息后，我们就可以引入站点主题了。

### 将模板样式从原有站点分离出来

打开[站点源码](https://github.com/sunwei/xyz)。
将其中的layouts和static目录，全部拷贝至我们的zero主题仓库根目录。
当前zero主题目录结构如下所示：
```shell
➜  zero git:(main) tree
.
├── LICENSE
├── README.md
├── go.mod
├── layouts
│   ├── index.html
│   ├── partials
│   │   ├── foot.html
│   │   ├── head.html
│   │   └── language.html
│   └── taxonomy
│       └── taxonomy.html
├── static
│   └── css
│       └── style.css
└── theme.toml

5 directories, 10 files
```

实际上我们的zero主题，到此已经完成了。
将更新推送到远端，就是一个大家都可以用的Hugo主题了。
真的很方便！

### 引入主题

主题是创建完成了，接下来就是应用了。
打开[站点源码](https://github.com/sunwei/xyz)，移除相应的layouts和static目录。

先在`config.toml`配置文件中引入主题：
```toml
baseURL = 'https://sunwei.xyz/'
title = 'sunwei.xyz'
theme = "github.com/sunwei/zero"

defaultContentLanguage = 'zh'
[languages]
[languages.zh]
languageName = '中文'
contentDir = 'content'
weight = 1

[languages.en]
languageName = 'English'
contentDir = 'content.en'
weight = 2
```

接着新建go模块信息文件`go.mod`：
```go
module github.com/sunwei/xyz

go 1.18
```

用Hugo模块命令更新模块配置信息:
```shell
➜  xyz git:(master) hugo mod get -u
go: no module dependencies to download
hugo: downloading modules …
go: downloading github.com/sunwei/zero v0.0.0-20221005003323-b204559ecb5e
go: added github.com/sunwei/zero v0.0.0-20221005003323-b204559ecb5e
hugo: collected modules in 2784 ms
```

再看go.mod，有自动插入模块信息：
```go
module github.com/sunwei/xyz

go 1.18

require github.com/sunwei/zero v0.0.0-20221005003323-b204559ecb5e // indirect
```
实际上也可以主动指明版本号，但前提是zero有发布具体版本。
实际上`Hugo mod`模块命令也可以很方便为咱们管理更新。

再一起来看下现在sunwei.xyz站点仓库的目录结构:
```shell
➜  xyz git:(master) tree
.
├── CNAME
├── README.md
├── command.sh
├── config.toml
├── content
│   └── _index.md
├── content.en
│   └── _index.md
├── go.mod
└── go.sum

2 directories, 8 files

```

和之前的相比：
```shell
➜  xyz git:(master) tree
.
├── CNAME
├── README.md
├── command.sh
├── config.toml
├── content
│   └── _index.md
├── content.en
│   └── _index.md
├── layouts
│   ├── index.html
│   ├── partials
│   │   ├── foot.html
│   │   ├── head.html
│   │   └── language.html
│   └── taxonomy
│       └── taxonomy.html
└── static
    └── css
        └── style.css

11 directories, 12 files
```

是不是更简洁明了！
这就让我们可以更加专注在内容的创作上了。
感谢Hugo！

## 相关链接

* Github站点[sunwei.xyz源码](https://github.com/sunwei/xyz)
* Github主题[zero源码](https://github.com/sunwei/zero)
* 站点Demo[https://sunwei.xyz](https://sunwei.xyz)

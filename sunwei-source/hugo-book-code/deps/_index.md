### Hugo的依赖管理

在HugoSites时序图中，通过配置信息创建好站点后，HugoSites实例会先准备好需要惰性初始化的信息，然后在配置信息中补全默认模板服务提供者。
紧接着就开始创建依赖。
其中惰性初始化在当前阶段只是注册信息，真正调用的地方在后面。
而默认模板服务提供者也是补全，实际开始处理模板的触发点则是在稍后的LoadResources中。
所以我们先把这两块放一放，等实际发挥作用的时候再做解释。
先来重点看一看依赖的创建。

依赖的创建主要包含这四个规范，分别是：
* NewPathSpec
* NewSpec
* NewContentSpec
* NewSourceSpec

其中NewSpec是PathSpec和OutputFormats和MediaTypes的聚合，用来提供一些基础信息，这里直接略过先。

NewSourceSpec是基于PathSpec组织好的Data目录，提供数据文件相关的服务的。
在Hugo中，用户项目根目录中的Data目录拥有最高优先级，这意味着，如果在主题目录里也有Data目录，并且有重名的数据文件，主题里的数据文件将被覆盖掉。
在调用像index一样的函数时，就可以获取数据文件的详细信息了 - `{{ index .Site.Data "123" }}`。
我们先专注在Hugo的主流程，这里的SourceSpec我们也略过。

接下来的重点将放在文件系统集大成者PathSpec，和基础内容提供者ContentSpec。
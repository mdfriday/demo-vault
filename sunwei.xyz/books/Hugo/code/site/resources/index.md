### LoadResources

创建HugoSites的最后一步就是LoadResources，没错，不知不觉中，我们已经走到了这一步。

```go
// LoadResources loads translations and templates.
func (d *Deps) LoadResources() error {
	if err := d.templateProvider.Update(d); err != nil {
		return fmt.Errorf("loading templates: %w", err)
	}
	return nil
}
```

LoadResources也就做了一件事，就是专注在通知templateProvider，可以开始更新了。

我们的templateProvider就是默认的`tplimpl.DefaultTemplateProvider`。

```go
// Update updates the Hugo Template System in the provided Deps
// with all the additional features, templates & functions.
func (*TemplateProvider) Update(d *deps.Deps) error {
	tmpl, err := newTemplateExec(d)
	if err != nil {
		return err
	}
	return tmpl.postTransform()
}
```

基本原理有在[基础架构](../how/基础架构.md)的Template vs Layouts章节中有介绍，这里就不再复述。

接下来我们将重心放到源码实现上。


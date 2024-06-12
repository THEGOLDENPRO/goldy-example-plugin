<div align="center">

  # goldy-example-plugin 
  <sub>Source code from {insert-yt-video-here}</sub>

</div>

## Installation for development.
Here's how to install and add the plugin to mov-cli for development.

1. Clone the repo.
```sh
git clone https://github.com/THEGOLDENPRO/goldy-example-plugin.git
cd goldy-example-plugin
```

2. Install in editable mode.
```sh
make install-editable
```
> **or** ``pip install -e . --config-settings editable_mode=compat``

3. Add the plugin to mov-cli.
```sh
mov-cli -e
```
```toml
[mov-cli.plugins]
goldy = "goldy_plugin" # check out the wiki for more: https://github.com/mov-cli/mov-cli/wiki/Plugins#%EF%B8%8F-how-to-install-plugins
```

4. Create away. 😊
```sh
mov-cli -s goldy abc
```

<br>

> The [mov-cli-test](https://github.com/mov-cli/mov-cli-test) and [mov-cli-youtube](https://github.com/mov-cli/mov-cli-youtube) plugins are great resources for learning the ins and outs of mov-cli plugin development.
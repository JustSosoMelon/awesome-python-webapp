awesome-python-webapp
=====================

这是"[小白的Python教程](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000)"中"[实战](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001397616003925a3d157284cd24bc0952d6c4a7c9d8c55000)"章的完整网站 + iOS App源码。

要查看示例网站运行效果，猛击：

[http://awesome.liaoxuefeng.com/](http://awesome.liaoxuefeng.com/)

示例网站由[Sina AppEngine](http://sae.sina.com.cn/)托管。

要下载源码，请直接通过Git获取源码。

实战章节的每天的增量源码在分支"day-xx"中。

## macOS 11 快捷键修改工具

本项目包含一个用于修改 macOS 11 系统快捷键的命令行工具。

### 快速使用

```bash
# 查看帮助
python3 modify_macos_shortcuts.py --help

# 列出常见快捷键配置
python3 modify_macos_shortcuts.py --list

# 启用 Spotlight 快捷键
python3 modify_macos_shortcuts.py --preset spotlight --enable

# 禁用 Mission Control 快捷键
python3 modify_macos_shortcuts.py --preset mission_control --disable
```

详细使用说明请参考 [README_SHORTCUTS.md](README_SHORTCUTS.md)。

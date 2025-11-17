# macOS 11 快捷键修改指南

本工具提供了修改 macOS 11 系统快捷键的方法。

## 快速开始

### 1. 使用预设快捷键

```bash
# 列出所有可用的预设快捷键
python modify_macos_shortcuts.py --list

# 启用 Spotlight 快捷键
python modify_macos_shortcuts.py --preset spotlight --enable

# 禁用 Mission Control 快捷键
python modify_macos_shortcuts.py --preset mission_control --disable
```

### 2. 手动指定快捷键

```bash
# 启用 Spotlight (Cmd+Space)
python modify_macos_shortcuts.py \
  --domain com.apple.symbolichotkeys \
  --key "AppleSymbolicHotKeys:64:enabled" \
  --value 1

# 禁用 Mission Control
python modify_macos_shortcuts.py \
  --domain com.apple.symbolichotkeys \
  --key "AppleSymbolicHotKeys:32:enabled" \
  --value 0
```

## 常见快捷键配置

### Spotlight 搜索
- **默认快捷键**: Cmd+Space
- **配置键**: `AppleSymbolicHotKeys:64:enabled`
- **启用**: `--preset spotlight --enable`

### Mission Control
- **默认快捷键**: Control+Up
- **配置键**: `AppleSymbolicHotKeys:32:enabled`
- **启用**: `--preset mission_control --enable`

### 应用程序窗口
- **默认快捷键**: Control+Down
- **配置键**: `AppleSymbolicHotKeys:33:enabled`
- **启用**: `--preset application_windows --enable`

### Launchpad
- **配置键**: `AppleSymbolicHotKeys:160:enabled`
- **启用**: `--preset launchpad --enable`

## 高级用法

### 修改快捷键组合

要修改快捷键的实际按键组合，需要修改 `value` 字段。快捷键的值是一个字典，包含：
- `enabled`: 是否启用 (0/1)
- `value`: 包含 `parameters` 数组，定义实际的按键组合

示例：修改 Spotlight 为 Cmd+Option+Space

```bash
# 首先需要读取当前配置查看结构
defaults read com.apple.symbolichotkeys AppleSymbolicHotKeys:64

# 然后使用 defaults write 修改
defaults write com.apple.symbolichotkeys AppleSymbolicHotKeys:64 -dict \
  enabled -int 1 \
  value -dict \
    type -string standard \
    parameters -array \
      32 \
      49 \
      1048576
```

参数说明：
- 第一个数字 (32): 修饰键 (32=Command, 16=Option, 4=Control, 1=Shift)
- 第二个数字 (49): 主键 (49=Space, 等等)
- 第三个数字 (1048576): 特殊标志

### 使用系统偏好设置（图形界面）

1. 打开 **系统偏好设置** (System Preferences)
2. 点击 **键盘** (Keyboard)
3. 选择 **快捷键** (Shortcuts) 标签
4. 在左侧选择要修改的类别
5. 双击要修改的快捷键，然后按下新的组合键

### 使用命令行直接修改

```bash
# 读取当前配置
defaults read com.apple.symbolichotkeys AppleSymbolicHotKeys

# 写入新配置
defaults write com.apple.symbolichotkeys AppleSymbolicHotKeys:64:enabled -int 1

# 应用更改（某些更改需要重启 Finder）
killall Finder

# 或者注销并重新登录
```

## 注意事项

1. **权限**: 某些系统快捷键的修改可能需要管理员权限
2. **生效时间**: 某些更改可能需要：
   - 重启应用程序
   - 注销并重新登录
   - 重启系统
3. **备份**: 修改前建议备份配置：
   ```bash
   defaults read com.apple.symbolichotkeys > ~/shortcuts_backup.plist
   ```
4. **恢复**: 如果出现问题，可以重置：
   ```bash
   defaults delete com.apple.symbolichotkeys
   ```

## 常见问题

### Q: 修改后没有生效？
A: 尝试注销并重新登录，或者重启系统。

### Q: 如何查看所有快捷键配置？
A: 运行 `defaults read com.apple.symbolichotkeys` 查看所有配置。

### Q: 如何恢复默认设置？
A: 删除配置后系统会自动恢复默认值：
```bash
defaults delete com.apple.symbolichotkeys AppleSymbolicHotKeys:64
```

## 参考资源

- [Apple 官方文档 - 键盘快捷键](https://support.apple.com/zh-cn/HT201236)
- [macOS 快捷键完整列表](https://support.apple.com/zh-cn/guide/mac-help/mchlp2271/mac)

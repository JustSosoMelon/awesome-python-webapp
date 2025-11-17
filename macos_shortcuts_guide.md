# macOS 11 快捷键修改指南

本指南介绍如何修改 macOS 11 (Big Sur) 的系统快捷键。

## 方法一：使用系统偏好设置（推荐）

### 步骤：

1. **打开系统偏好设置**
   - 点击苹果菜单 → 系统偏好设置
   - 或使用 Spotlight 搜索 "系统偏好设置"

2. **进入键盘设置**
   - 点击"键盘"图标
   - 选择"快捷键"标签页

3. **修改快捷键**
   - **系统快捷键**: 在左侧选择类别（如"调度中心"、"键盘"等），然后点击要修改的快捷键，按下新的组合键
   - **应用快捷键**: 
     - 选择左侧的"应用快捷键"
     - 点击"+"按钮
     - 选择应用程序
     - 输入菜单项的确切名称
     - 设置新的快捷键组合

4. **保存更改**
   - 更改会立即生效，无需重启

## 方法二：使用命令行（defaults 命令）

### 查看当前快捷键设置

```bash
# 查看所有符号快捷键
defaults read com.apple.symbolichotkeys AppleSymbolicHotKeys

# 查看特定快捷键（例如 Mission Control，ID 为 60）
defaults read com.apple.symbolichotkeys AppleSymbolicHotKeys | grep -A 5 '"60"'
```

### 修改系统快捷键

```bash
# 禁用 Mission Control（ID 60）
defaults write com.apple.symbolichotkeys AppleSymbolicHotKeys -dict-add 60 '{enabled = 0;}'

# 启用并设置新的快捷键
# 格式: {enabled = 1; value = {parameters = (键码, 修饰键, 0); type = standard;};}
defaults write com.apple.symbolichotkeys AppleSymbolicHotKeys -dict-add 60 '{enabled = 1; value = {parameters = (126, 131072, 0); type = standard;};}'
```

### 常用快捷键 ID

- **60**: Mission Control
- **61**: Application windows（应用程序窗口）
- **62**: Desktop（显示桌面）
- **63**: Dashboard
- **64**: Launchpad
- **65**: Spotlight（聚焦搜索）
- **79**: 输入法切换

### 键码参考

- **126**: 上箭头 ↑
- **125**: 下箭头 ↓
- **123**: 左箭头 ←
- **124**: 右箭头 →
- **49**: 空格键
- **36**: Return 键

### 修饰键代码

- **131072**: Control (⌃)
- **262144**: Option/Alt (⌥)
- **524288**: Command (⌘)
- **1048840**: Shift (⇧)

### 修改应用程序快捷键

```bash
# 修改 Safari 的快捷键
defaults write com.apple.Safari NSUserKeyEquivalents -dict-add "新建窗口" "@n"

# 修改后需要重启应用程序
killall Safari
```

## 方法三：使用 Python 脚本

项目中的 `macos_shortcut_modifier.py` 脚本提供了便捷的 Python 接口来修改快捷键。

### 使用示例

```bash
# 列出常用快捷键
python3 macos_shortcut_modifier.py list

# 查看当前设置
python3 macos_shortcut_modifier.py get
```

## 注意事项

1. **权限要求**: 修改系统快捷键可能需要管理员权限
2. **重启生效**: 某些更改可能需要注销登录或重启系统才能生效
3. **备份设置**: 修改前建议备份当前的快捷键设置
4. **冲突检查**: 确保新快捷键不与现有快捷键冲突

## 备份和恢复快捷键设置

### 备份

```bash
# 备份所有快捷键设置
defaults read com.apple.symbolichotkeys AppleSymbolicHotKeys > ~/shortcuts_backup.plist
```

### 恢复

```bash
# 恢复快捷键设置（需要先转换为正确的格式）
defaults write com.apple.symbolichotkeys AppleSymbolicHotKeys -dict < ~/shortcuts_backup.plist
```

## 常见问题

### Q: 修改后没有生效？
A: 尝试注销并重新登录，或重启系统。

### Q: 如何重置所有快捷键？
A: 删除配置文件并重启：
```bash
defaults delete com.apple.symbolichotkeys
killall SystemUIServer
```

### Q: 如何查看某个应用程序的快捷键？
A: 打开应用程序，查看菜单栏，快捷键会显示在菜单项旁边。

## 相关资源

- [Apple 官方文档 - 键盘快捷键](https://support.apple.com/zh-cn/HT201236)
- [macOS 系统偏好设置帮助](https://support.apple.com/zh-cn/guide/mac-help/)

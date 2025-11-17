#!/bin/bash
# macOS 11 快捷键修改示例脚本

echo "=== macOS 11 快捷键修改示例 ==="
echo ""

# 显示帮助信息
echo "1. 查看帮助信息:"
python3 modify_macos_shortcuts.py --help
echo ""

# 列出常见快捷键
echo "2. 列出常见快捷键配置:"
python3 modify_macos_shortcuts.py --list
echo ""

# 示例：启用 Spotlight 快捷键
echo "3. 启用 Spotlight 快捷键示例 (注释掉，避免实际执行):"
echo "# python3 modify_macos_shortcuts.py --preset spotlight --enable"
echo ""

# 示例：禁用 Mission Control
echo "4. 禁用 Mission Control 示例 (注释掉，避免实际执行):"
echo "# python3 modify_macos_shortcuts.py --preset mission_control --disable"
echo ""

echo "注意: 实际修改快捷键的命令已注释，取消注释后才会执行。"

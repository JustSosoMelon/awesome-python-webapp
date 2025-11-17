#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
macOS 11 快捷键修改工具

此脚本用于通过命令行修改 macOS 11 的系统快捷键设置。
"""

import subprocess
import sys
import json
import os


def run_command(cmd):
    """执行 shell 命令"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"错误: {e.stderr}")
        return None


def get_current_shortcuts():
    """获取当前的快捷键设置"""
    cmd = "defaults read com.apple.symbolichotkeys AppleSymbolicHotKeys"
    output = run_command(cmd)
    if output:
        try:
            # 解析 plist 输出
            return output
        except:
            return output
    return None


def modify_shortcut(shortcut_id, enabled, key_code, modifiers):
    """
    修改快捷键
    
    参数:
    - shortcut_id: 快捷键 ID（如 60 表示 Mission Control）
    - enabled: 是否启用 (True/False)
    - key_code: 键码（如 126 表示上箭头）
    - modifiers: 修饰键组合（如 131072 表示 Control）
    
    常用快捷键 ID:
    - 60: Mission Control
    - 61: Application windows
    - 62: Desktop
    - 63: Dashboard
    - 64: Launchpad
    - 65: 显示 Spotlight
    - 79: 切换输入法
    """
    # 构建 plist 字典结构
    value = {
        "enabled": enabled,
        "value": {
            "parameters": [
                key_code,
                modifiers,
                0
            ],
            "type": "standard"
        }
    }
    
    # 使用 defaults 命令修改
    # 注意：这需要将字典转换为 plist 格式
    cmd = f"""defaults write com.apple.symbolichotkeys AppleSymbolicHotKeys -dict-add {shortcut_id} '{json.dumps(value)}'"""
    
    print(f"正在修改快捷键 ID {shortcut_id}...")
    result = run_command(cmd)
    
    if result is None:
        print("修改成功！请重启系统或注销登录以使更改生效。")
        return True
    return False


def modify_app_shortcut(app_name, menu_item, new_shortcut):
    """
    修改应用程序的快捷键
    
    参数:
    - app_name: 应用程序名称（如 "Safari"）
    - menu_item: 菜单项名称（如 "New Window"）
    - new_shortcut: 新的快捷键组合（如 "@n" 表示 Cmd+N）
    """
    # 使用 NSUserKeyEquivalents
    bundle_id = f"com.apple.{app_name.lower()}"
    
    # 注意：实际实现需要使用 plist 文件操作
    print(f"修改应用程序快捷键需要直接编辑 ~/Library/Preferences/{bundle_id}.plist")
    print(f"或使用 defaults 命令:")
    print(f'defaults write {bundle_id} NSUserKeyEquivalents -dict-add "{menu_item}" "{new_shortcut}"')


def list_common_shortcuts():
    """列出常用的快捷键 ID"""
    shortcuts = {
        "60": "Mission Control",
        "61": "Application windows",
        "62": "Desktop",
        "63": "Dashboard",
        "64": "Launchpad",
        "65": "显示 Spotlight",
        "79": "切换输入法"
    }
    
    print("\n常用快捷键 ID:")
    print("-" * 40)
    for sid, name in shortcuts.items():
        print(f"  {sid}: {name}")


def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("macOS 11 快捷键修改工具")
        print("\n使用方法:")
        print("  python3 macos_shortcut_modifier.py list          # 列出常用快捷键")
        print("  python3 macos_shortcut_modifier.py get           # 获取当前快捷键设置")
        print("  python3 macos_shortcut_modifier.py modify <id>   # 修改快捷键（需要更多参数）")
        print("\n注意: 修改系统快捷键需要管理员权限，且可能需要重启系统。")
        return
    
    command = sys.argv[1]
    
    if command == "list":
        list_common_shortcuts()
    elif command == "get":
        print("当前快捷键设置:")
        print(get_current_shortcuts())
    elif command == "modify":
        if len(sys.argv) < 3:
            print("错误: 请提供快捷键 ID")
            print("使用 'list' 命令查看可用的快捷键 ID")
            return
        shortcut_id = sys.argv[2]
        print(f"修改快捷键 ID {shortcut_id} 需要更多参数")
        print("请参考脚本中的 modify_shortcut 函数")
    else:
        print(f"未知命令: {command}")


if __name__ == "__main__":
    main()

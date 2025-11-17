#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
macOS 11 快捷键修改工具

使用方法:
    python modify_macos_shortcuts.py --help
    
示例:
    # 修改 Spotlight 快捷键为 Cmd+Space
    python modify_macos_shortcuts.py --domain com.apple.symbolichotkeys --key AppleSymbolicHotKeys:64:enabled --value 1
    
    # 修改 Mission Control 快捷键
    python modify_macos_shortcuts.py --domain com.apple.symbolichotkeys --key AppleSymbolicHotKeys:32:enabled --value 1
"""

import subprocess
import argparse
import sys
import json


def run_command(cmd):
    """执行 shell 命令并返回结果"""
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
        print(f"错误: {e.stderr}", file=sys.stderr)
        return None


def read_plist_value(domain, key):
    """读取 plist 文件中的值"""
    cmd = f"defaults read {domain} '{key}'"
    result = run_command(cmd)
    return result


def write_plist_value(domain, key, value):
    """写入 plist 文件中的值"""
    # 根据值的类型选择不同的写入方式
    if isinstance(value, bool):
        value_str = "true" if value else "false"
        cmd = f"defaults write {domain} '{key}' -bool {value_str}"
    elif isinstance(value, int):
        cmd = f"defaults write {domain} '{key}' -int {value}"
    elif isinstance(value, float):
        cmd = f"defaults write {domain} '{key}' -float {value}"
    elif isinstance(value, (list, dict)):
        # 对于复杂类型，使用 JSON 格式
        json_str = json.dumps(value)
        cmd = f"defaults write {domain} '{key}' '{json_str}'"
    else:
        cmd = f"defaults write {domain} '{key}' '{value}'"
    
    result = run_command(cmd)
    return result is not None


def get_common_shortcuts():
    """返回常见的 macOS 快捷键配置"""
    return {
        "spotlight": {
            "domain": "com.apple.symbolichotkeys",
            "key": "AppleSymbolicHotKeys:64",
            "description": "Spotlight 搜索 (默认: Cmd+Space)"
        },
        "mission_control": {
            "domain": "com.apple.symbolichotkeys",
            "key": "AppleSymbolicHotKeys:32",
            "description": "Mission Control (默认: Control+Up)"
        },
        "application_windows": {
            "domain": "com.apple.symbolichotkeys",
            "key": "AppleSymbolicHotKeys:33",
            "description": "应用程序窗口 (默认: Control+Down)"
        },
        "launchpad": {
            "domain": "com.apple.symbolichotkeys",
            "key": "AppleSymbolicHotKeys:160",
            "description": "Launchpad"
        },
        "screenshot": {
            "domain": "com.apple.symbolichotkeys",
            "key": "AppleSymbolicHotKeys:60",
            "description": "截屏工具"
        }
    }


def list_shortcuts():
    """列出常见的快捷键配置"""
    shortcuts = get_common_shortcuts()
    print("\n常见的 macOS 快捷键配置:\n")
    for name, config in shortcuts.items():
        print(f"名称: {name}")
        print(f"  描述: {config['description']}")
        print(f"  Domain: {config['domain']}")
        print(f"  Key: {config['key']}")
        
        # 尝试读取当前值
        enabled_key = f"{config['key']}:enabled"
        value = read_plist_value(config['domain'], enabled_key)
        if value:
            print(f"  当前状态: {value}")
        print()


def modify_shortcut(domain, key, value=None, enable=True):
    """
    修改快捷键
    
    Args:
        domain: plist 域名 (如 com.apple.symbolichotkeys)
        key: 键名 (如 AppleSymbolicHotKeys:64:enabled)
        value: 要设置的值 (可选)
        enable: 是否启用 (默认 True)
    """
    if value is None:
        value = 1 if enable else 0
    
    print(f"正在修改快捷键配置...")
    print(f"  Domain: {domain}")
    print(f"  Key: {key}")
    print(f"  Value: {value}")
    
    if write_plist_value(domain, key, value):
        print("✓ 修改成功!")
        print("\n注意: 某些更改可能需要重启应用程序或注销登录才能生效。")
        return True
    else:
        print("✗ 修改失败!")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="修改 macOS 11 快捷键配置工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
  # 列出常见快捷键
  %(prog)s --list
  
  # 启用 Spotlight 快捷键
  %(prog)s --domain com.apple.symbolichotkeys --key "AppleSymbolicHotKeys:64:enabled" --value 1
  
  # 禁用 Mission Control 快捷键
  %(prog)s --domain com.apple.symbolichotkeys --key "AppleSymbolicHotKeys:32:enabled" --value 0
  
  # 使用预设快捷方式
  %(prog)s --preset spotlight --enable
        """
    )
    
    parser.add_argument(
        "--list",
        action="store_true",
        help="列出常见的快捷键配置"
    )
    
    parser.add_argument(
        "--domain",
        type=str,
        help="plist 域名 (如 com.apple.symbolichotkeys)"
    )
    
    parser.add_argument(
        "--key",
        type=str,
        help="要修改的键名"
    )
    
    parser.add_argument(
        "--value",
        type=int,
        help="要设置的值 (0=禁用, 1=启用)"
    )
    
    parser.add_argument(
        "--preset",
        type=str,
        choices=["spotlight", "mission_control", "application_windows", "launchpad", "screenshot"],
        help="使用预设的快捷键配置"
    )
    
    parser.add_argument(
        "--enable",
        action="store_true",
        help="启用快捷键 (与 --preset 一起使用)"
    )
    
    parser.add_argument(
        "--disable",
        action="store_true",
        help="禁用快捷键 (与 --preset 一起使用)"
    )
    
    args = parser.parse_args()
    
    if args.list:
        list_shortcuts()
        return
    
    if args.preset:
        shortcuts = get_common_shortcuts()
        if args.preset not in shortcuts:
            print(f"错误: 未知的预设 '{args.preset}'", file=sys.stderr)
            sys.exit(1)
        
        config = shortcuts[args.preset]
        enable = args.enable if not args.disable else False
        
        key = f"{config['key']}:enabled"
        modify_shortcut(config['domain'], key, enable=enable)
        return
    
    if not args.domain or not args.key:
        parser.print_help()
        print("\n错误: 必须提供 --domain 和 --key 参数，或使用 --preset", file=sys.stderr)
        sys.exit(1)
    
    modify_shortcut(args.domain, args.key, args.value)


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""
自动化监听与 GitHub 实时推送同步脚本 (Auto Sync & Push)
功能：
1. 实时监听本地《初中数学一年通关工作台.html》及相关文件变动；
2. 检测到保存后，自动同步至 index.html 并提取最新题库；
3. 自动执行 git commit 与 git push 推送到 GitHub 远程仓库；
4. 内置 3 秒智能防抖，避免连续保存频繁触发。
"""

import os
import sys
import time
import shutil
import subprocess
from datetime import datetime

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WATCH_FILE = os.path.join(BASE_DIR, "初中数学一年通关工作台.html")
INDEX_FILE = os.path.join(BASE_DIR, "index.html")

def get_file_mtime(filepath):
    """获取文件的最后修改时间"""
    try:
        if os.path.exists(filepath):
            return os.path.getmtime(filepath)
    except Exception:
        pass
    return 0

def do_sync_and_push():
    """执行同步与推送操作"""
    try:
        print(f"\n[{datetime.now().strftime('%H:%M:%S')}] ⚡ 检测到本地文件更新，正在处理...")
        
        # 1. 同步复制为 index.html
        if os.path.exists(WATCH_FILE):
            shutil.copyfile(WATCH_FILE, INDEX_FILE)
            print("  [1/3] 已自动同步至 index.html")
        
        # 2. 尝试执行数据提取（如有需要）
        export_script = os.path.join(BASE_DIR, "crawler", "export_data.py")
        if os.path.exists(export_script):
            subprocess.run([sys.executable, export_script], cwd=BASE_DIR, capture_output=True)
            print("  [2/3] 已自动同步提取最新题库与微课数据")

        # 3. Git 提交并推送
        time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        commit_msg = f"auto: 自动同步工作台更新 ({time_str})"
        
        # git add .
        subprocess.run(["git", "add", "."], cwd=BASE_DIR, check=True)
        
        # git commit
        res = subprocess.run(["git", "commit", "-m", commit_msg], cwd=BASE_DIR, capture_output=True, text=True)
        if "nothing to commit" in res.stdout or "nothing to commit" in res.stderr:
            print("  [-] 文件内容无实质变动，无需重复推送。")
            return

        # git push
        print("  [3/3] 正在推送到 GitHub 远程仓库 (origin/main)...")
        push_res = subprocess.run(["git", "push", "origin", "main"], cwd=BASE_DIR, capture_output=True, text=True)
        
        if push_res.returncode == 0:
            print(f"  ✅ 【推送成功！】最新修改已实时生效于 GitHub 及在线网站。")
        else:
            print(f"  [!] 推送提示: {push_res.stderr.strip() or push_res.stdout.strip()}")

    except Exception as e:
        print(f"  [X] 同步推送过程遇到异常: {e}")

def start_watch():
    print("=" * 60)
    print("🚀 初中数学工作台 · 自动化监听与实时推送服务已启动")
    print(f"📁 监听文件: {os.path.basename(WATCH_FILE)}")
    print("💡 使用说明: 您在编辑器中修改并保存文件后，脚本将自动在 3 秒内完成同步并推送到 GitHub！")
    print("⏹️ 退出监听: 请按 Ctrl + C")
    print("=" * 60)

    last_mtime = get_file_mtime(WATCH_FILE)

    while True:
        try:
            time.sleep(1.5)
            current_mtime = get_file_mtime(WATCH_FILE)
            
            if current_mtime > last_mtime:
                # 3 秒防抖等待
                time.sleep(3.0)
                last_mtime = get_file_mtime(WATCH_FILE)
                do_sync_and_push()

        except KeyboardInterrupt:
            print("\n[*] 自动监听服务已安全停止。")
            break
        except Exception as e:
            time.sleep(2)

if __name__ == "__main__":
    start_watch()

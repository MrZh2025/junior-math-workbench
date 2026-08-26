@echo off
chcp 65001 >nul
title 初中数学工作台 · 自动监听同步推送服务
echo 正在启动自动化监听与 GitHub 实时推送服务...
python auto_sync.py
pause

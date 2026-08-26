# -*- coding: utf-8 -*-
"""
数据整合与导出工具 (Export Data Script)
功能：解析 HTML 中的所有知识点条目，批量整合内部可直接播放的微课与 10 题题库，
导出为前端直接可引用的 math_data.js 与结构化的 math_data.json。
"""

import json
import os
import re
import sys

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

from bilibili_video_crawler import get_default_micro_courses, get_real_videos
from seed_question_bank import get_questions_for_point

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML_PATH = os.path.join(BASE_DIR, "初中数学一年通关工作台.html")
OUTPUT_JS = os.path.join(BASE_DIR, "math_data.js")
OUTPUT_JSON = os.path.join(BASE_DIR, "math_data.json")

def parse_points_from_html():
    """
    从 HTML 文件中提取所有知识点的 ID、名称与年级标签
    """
    if not os.path.exists(HTML_PATH):
        print(f"[-] 未找到工作台 HTML 文件: {HTML_PATH}")
        return []
    
    with open(HTML_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    
    pattern = re.compile(r'<li\s+data-id="([^"]+)">.*?<span\s+class="txt">([^<]+)</span>.*?<span\s+class="grade-tag[^"]*">([^<]+)</span>', re.DOTALL)
    matches = pattern.findall(content)
    
    points = []
    for pid, title, grade in matches:
        points.append({
            "id": pid.strip(),
            "title": title.strip(),
            "grade": grade.strip()
        })
    return points

def build_dataset():
    """
    构建全量知识点内嵌微课与 10 题真题数据集
    """
    points = parse_points_from_html()
    print(f"[*] 从工作台中共提取到 {len(points)} 个知识点。")
    
    dataset = {}
    for idx, p in enumerate(points):
        pid = p["id"]
        title = p["title"]
        grade = p["grade"]
        
        # 1. 内部可播放的微课选集列表（板书讲义）
        videos = get_default_micro_courses(pid, title)

        # 2. B 站真实可内嵌播放视频（来自 video_map.json 缓存，运行 bilibili_video_crawler.py 可重新抓取）
        real_videos = get_real_videos(pid)

        # 3. 10 题真题库与深度解析
        qb = get_questions_for_point(pid, title, grade)
        
        dataset[pid] = {
            "id": pid,
            "title": title,
            "grade": grade,
            "star": qb.get("star", 5),
            "tips": qb.get("tips", ""),
            "videos": videos,
            "real_videos": real_videos,
            "questions": qb.get("questions", [])
        }
    
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(dataset, f, ensure_ascii=False, indent=2)
    print(f"[+] 已生成 JSON 题库与视频文件: {OUTPUT_JSON}")
    
    js_content = f"// 初中数学知识点微课与精选题库数据\nwindow.MATH_DATA = {json.dumps(dataset, ensure_ascii=False, indent=2)};\n"
    with open(OUTPUT_JS, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"[+] 已生成 JS 预载入文件: {OUTPUT_JS}")

if __name__ == "__main__":
    build_dataset()

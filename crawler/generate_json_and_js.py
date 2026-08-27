# -*- coding: utf-8 -*-
"""
Generate complete 50-question database for all 53 knowledge points into math_data.json and math_data.js
"""
import os
import re
import json
from seed_question_bank import get_questions_for_point
from bilibili_video_crawler import get_default_micro_courses

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML_FILE = os.path.join(BASE_DIR, "初中数学一年通关工作台.html")
VIDEO_MAP_FILE = os.path.join(os.path.dirname(__file__), "video_map.json")
OUTPUT_JSON = os.path.join(BASE_DIR, "math_data.json")
OUTPUT_JS = os.path.join(BASE_DIR, "math_data.js")

def extract_points():
    if not os.path.exists(HTML_FILE):
        return []
    with open(HTML_FILE, 'r', encoding='utf-8') as f:
        html_text = f.read()

    # Match <li data-id="xxx">...<span class="txt">yyy</span>...<span class="grade-tag ...">zzz</span>
    pattern = r'<li data-id="([^"]+)">.*?<span class="txt">([^<]+)</span>.*?<span class="grade-tag [^"]+">([^<]+)</span>'
    matches = re.findall(pattern, html_text, re.DOTALL)
    points = []
    seen = set()
    for pid, title, grade in matches:
        if pid not in seen:
            seen.add(pid)
            points.append({
                "id": pid,
                "title": title.strip(),
                "grade": grade.strip()
            })
    return points

def build_all():
    points = extract_points()
    print(f"Extracted {len(points)} knowledge points.")

    video_data = {}
    if os.path.exists(VIDEO_MAP_FILE):
        try:
            with open(VIDEO_MAP_FILE, 'r', encoding='utf-8') as f:
                video_data = json.load(f)
        except Exception as e:
            print(f"Error loading video_map: {e}")

    dataset = {}
    for p in points:
        pid = p["id"]
        title = p["title"]
        grade = p["grade"]

        point_record = get_questions_for_point(pid, title, grade)
        point_record["videos"] = get_default_micro_courses(pid, title)
        
        if pid in video_data and "videos" in video_data[pid]:
            point_record["real_videos"] = video_data[pid]["videos"]
        else:
            point_record["real_videos"] = []

        dataset[pid] = {
            "id": pid,
            "title": title,
            "grade": grade,
            "star": point_record.get("star", 5),
            "tips": point_record.get("tips", ""),
            "videos": point_record.get("videos", []),
            "real_videos": point_record.get("real_videos", []),
            "questions": point_record.get("questions", [])
        }

    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, ensure_ascii=False, indent=2)

    with open(OUTPUT_JS, 'w', encoding='utf-8') as f:
        f.write("/**\n * 初中数学一年通关工作台 - 53大考点 × 50题真题矩阵题库与微课资源\n */\n")
        f.write("window.MATH_DATA = ")
        json.dump(dataset, f, ensure_ascii=False, indent=2)
        f.write(";\n")

    print(f"Successfully generated {len(dataset)} points with 50 questions each.")

if __name__ == "__main__":
    build_all()

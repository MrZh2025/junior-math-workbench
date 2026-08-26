# -*- coding: utf-8 -*-
"""
初中数学权威微课讲义与名师板书数据库
1. get_default_micro_courses: 为每个知识点生成【第1讲 概念推导】【第2讲 典型例题】【第3讲 易错秒杀】板书讲义
2. get_real_videos: 读取 video_map.json 缓存，返回该考点可内嵌播放的 B 站真实视频列表
3. crawl_real_videos: 联网调用 B 站搜索 API，为所有考点抓取真实视频并更新 video_map.json 缓存
   （直接运行本文件即可重新抓取：python bilibili_video_crawler.py）
"""

import json
import os
import re
import sys
import time
import urllib.request
import urllib.parse
import http.cookiejar

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VIDEO_MAP_PATH = os.path.join(BASE_DIR, "video_map.json")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"


def get_default_micro_courses(point_id, point_name):
    """
    生成高质量内部可交互微课讲义与多源通道
    """
    episodes = [
        {
            "ep_id": "ep-1",
            "title": f"【第 1 讲】{point_name} · 核心概念与定理推导",
            "tag": "概念精讲",
            "duration": "12:30",
            "board_summary": f"📌 <b>【核心概念精析】</b><br>1. 概念本质：{point_name} 是初中数学的核心基石，重点考查定义域、运算性质与公理体系；<br>2. 推导过程：从基本数学模型出发，通过等量代换与逻辑演绎得出核心结论；<br>3. 适用条件：务必满足定义域约束与前提假设，不可盲目套用公式。",
            "key_points": [
                "牢记基本概念与几何/代数定义",
                "掌握定理公式的推导逻辑与反例判断",
                "明确运算范围与字母符号的实际几何意义"
            ]
        },
        {
            "ep_id": "ep-2",
            "title": f"【第 2 讲】{point_name} · 典型例题与中考必刷题",
            "tag": "真题实战",
            "duration": "15:40",
            "board_summary": f"📌 <b>【中考经典题型剖析】</b><br>1. 审题破题：圈出题干中的关键词（如“互为相反数”、“垂直平分”、“顶点在x轴”）；<br>2. 建模转化：将实际问题或几何条件转化为代数方程、不等式或函数解析式；<br>3. 书写规范：严谨写出“解”、“设”、“因为…所以…”等中考采分点步骤。",
            "key_points": [
                "题型一：基础概念与性质直接计算",
                "题型二：综合条件下的数形结合与转化",
                "题型三：中考常见解答题规范书写流程"
            ]
        },
        {
            "ep_id": "ep-3",
            "title": f"【第 3 讲】{point_name} · 易错陷阱与满分秒杀套路",
            "tag": "易错秒杀",
            "duration": "11:15",
            "board_summary": f"📌 <b>【名师避坑与秒杀绝招】</b><br>1. 陷阱一：分类讨论遗漏多解（如无图几何题、绝对值距离、二次项系数为0）；<br>2. 陷阱二：忽略隐含范围（分母不为0、被开方数非负、Δ≥0、实际问题正整数）；<br>3. 秒杀套路：特殊值检验法、排除法、特征模型秒出答案。",
            "key_points": [
                "警惕隐藏条件与边界极值",
                "牢记名师专属速记口诀",
                "考场选择题代入验证法提速 300%"
            ]
        }
    ]
    return episodes


def _load_video_map():
    if os.path.exists(VIDEO_MAP_PATH):
        try:
            with open(VIDEO_MAP_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {}


def get_real_videos(point_id):
    """
    返回该考点已抓取缓存的 B 站真实可内嵌视频列表：
    [{"bvid", "title", "author", "duration", "play"}, ...]
    """
    vm = _load_video_map()
    return vm.get(point_id, {}).get("videos", [])


# ==================== 联网抓取部分 ====================

def _make_opener():
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener.addheaders = [("User-Agent", UA), ("Referer", "https://www.bilibili.com/")]
    return opener


def _dur_secs(d):
    try:
        s = 0
        for p in d.split(":"):
            s = s * 60 + int(p)
        return s
    except Exception:
        return 0


def _clean_title(t):
    return re.sub(r"</?em[^>]*>", "", t)


def crawl_real_videos(points, per_point=3, sleep_secs=2.5):
    """
    points: [{"id":..., "title":...}, ...]
    为每个考点用 B 站搜索 API 抓取 3 条可内嵌视频（3-60 分钟），写入 video_map.json 缓存
    """
    opener = _make_opener()
    # 先访问首页领取 cookie（buvid），否则搜索接口触发风控
    try:
        opener.open("https://www.bilibili.com/", timeout=20).read()
    except Exception as e:
        print(f"[-] 访问 B 站首页失败：{e}")

    vm = _load_video_map()
    for p in points:
        pid, title = p["id"], p["title"]
        kw = "初中数学 " + title
        url = ("https://api.bilibili.com/x/web-interface/search/type?search_type=video"
               "&keyword=" + urllib.parse.quote(kw) + "&page=1&order=totalrank")
        vids = []
        try:
            data = json.loads(opener.open(url, timeout=20).read().decode("utf-8", "replace"))
            if data.get("code") == 0:
                for item in (data.get("data") or {}).get("result") or []:
                    ds = _dur_secs(item.get("duration", ""))
                    if ds < 180 or ds > 3600:
                        continue
                    vids.append({
                        "bvid": item["bvid"],
                        "title": _clean_title(item.get("title", "")),
                        "author": item.get("author", ""),
                        "duration": item.get("duration", ""),
                        "play": item.get("play", 0),
                    })
                    if len(vids) >= per_point:
                        break
            else:
                print(f"[-] {pid} 搜索接口返回 code={data.get('code')}（可能触发风控，可稍后重试）")
        except Exception as e:
            print(f"[-] {pid} 抓取失败：{e}")

        if vids:
            vm[pid] = {"keyword": kw, "videos": vids}
        print(f"[*] {pid} {title} -> {len(vids)} 条视频")
        time.sleep(sleep_secs)

    with open(VIDEO_MAP_PATH, "w", encoding="utf-8") as f:
        json.dump(vm, f, ensure_ascii=False, indent=2)
    print(f"[+] 已更新视频缓存: {VIDEO_MAP_PATH}")
    return vm


if __name__ == "__main__":
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
    # 独立运行时：从 export_data 的解析函数拿到全部考点后抓取
    from export_data import parse_points_from_html
    crawl_real_videos(parse_points_from_html())

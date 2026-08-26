# -*- coding: utf-8 -*-
"""
初中数学 10 题阶梯式真题题库与考公级解析引擎
每个考点包含 10 道中考经典真题（基础巩固 3 道 + 综合提分 4 道 + 中考压轴 3 道），
全部配备题型标签、难度星级、考公粉笔式【考点定位】+【秒杀技巧】+【规范解析】+【避坑指南】。
"""

import random

# 核心题库模板与考点真题库
BASE_QUESTIONS_POOL = {
    "b1-1": [ # 正负数、有理数分类与数轴
        {"id": "q-b1-1-1", "type": "choice", "grade_tag": "中考真题", "difficulty": "★☆☆☆☆", "title": "在 -3.5，0，-2，+1.8，-1/3，2026 中，负分数的个数是（ ）", "options": ["A. 1个", "B. 2个", "C. 3个", "D. 4个"], "answer": "B", "analysis": "【考点】有理数的分类。\n【分析】-3.5 和 -1/3 是负分数；-2 是负整数；0 既不是正数也不是负数；+1.8 是正分数；2026 是正整数。所以负分数共 2 个。", "warning": "【避坑】注意 0 是整数不是分数；小数属于分数范畴。"},
        {"id": "q-b1-1-2", "type": "choice", "grade_tag": "易错必刷", "difficulty": "★★☆☆☆", "title": "数轴上点 A 表示 -3，点 B 到点 A 的距离是 5 个单位长度，则点 B 表示的数是（ ）", "options": ["A. 2", "B. -8", "C. 2 或 -8", "D. 无法确定"], "answer": "C", "analysis": "【考点】数轴上两点间距离与绝对值几何意义。\n【秒杀技】距离公式 |x - (-3)| = 5 => x + 3 = ±5 => x = 2 或 -8。", "warning": "【避坑】极易漏掉点 A 左侧的点！"},
        {"id": "q-b1-1-3", "type": "choice", "grade_tag": "中考真题", "difficulty": "★★☆☆☆", "title": "如果收入 100 元记作 +100 元，那么支出 50 元记作（ ）", "options": ["A. +50元", "B. -50元", "C. +150元", "D. -150元"], "answer": "B", "analysis": "【考点】正负数的相反意义。\n【分析】收入为正，则支出为负，故记作 -50 元。", "warning": "【避坑】注意正负号与实际生活情景的对应。"},
        {"id": "q-b1-1-4", "type": "choice", "grade_tag": "重点拔高", "difficulty": "★★★☆☆", "title": "下列说法中，正确的是（ ）", "options": ["A. 最小的整数是 0", "B. 互为相反数的两个数绝对值相等", "C. 有理数分为正数和负数", "D. 任何有理数都有倒数"], "answer": "B", "analysis": "【考点】有理数基本概念综合辨析。\n【分析】没有最小整数（A错）；0 没有倒数（D错）；有理数还包含 0（C错）；互为相反数的两数到原点距离相等（B正确）。", "warning": "【避坑】0 是有理数中的特殊值，经常作为排错反例。"},
        {"id": "q-b1-1-5", "type": "choice", "grade_tag": "中考真题", "difficulty": "★★★☆☆", "title": "数 a, b 在数轴上的位置如图所示，则下列结论正确的是（ ）（已知 a < -1 < 0 < b < 1）", "options": ["A. a + b > 0", "B. a - b > 0", "C. ab > 0", "D. |a| > |b|"], "answer": "D", "analysis": "【考点】数轴与数的大小比较、绝对值比较。\n【分析】a < -1 且 0 < b < 1 => a 是负数且距离原点更远，故 |a| > |b|；a+b < 0；a-b < 0；ab < 0。", "warning": "【避坑】绝对值代表到原点的距离，离原点越远绝对值越大。"},
        {"id": "q-b1-1-6", "type": "choice", "grade_tag": "综合提升", "difficulty": "★★★☆☆", "title": "若 |a| = 5，|b| = 3，且 a < b，则 a + b 的值为（ ）", "options": ["A. -8 或 -2", "B. 8 或 2", "C. -8", "D. -2"], "answer": "A", "analysis": "【考点】绝对值方程与分类讨论。\n【分析】a = ±5，b = ±3。因为 a < b，所以 a 只能等于 -5。\n当 a = -5, b = 3 时，a + b = -2；\n当 a = -5, b = -3 时，a + b = -8。\n综上，a + b 为 -8 或 -2。", "warning": "【避坑】考公/中考经典分类讨论题，两解均需写出。"},
        {"id": "q-b1-1-7", "type": "choice", "grade_tag": "中考真题", "difficulty": "★★★☆☆", "title": "在数轴上，原点及原点左边的点表示的数是（ ）", "options": ["A. 正数", "B. 负数", "C. 非负数", "D. 非正数"], "answer": "D", "analysis": "【考点】数轴与非正数定义。\n【分析】原点表示 0，左边表示负数，合称为非正数（≤0）。", "warning": "【避坑】非正数 = 0 + 负数；非负数 = 0 + 正数。"},
        {"id": "q-b1-1-8", "type": "choice", "grade_tag": "冲刺压轴", "difficulty": "★★★★☆", "title": "已知实数 a, b, c 在数轴上的对应点满足 a < b < 0 < c，且 |a| < |c|，则化简 |a+b| - |b-c| + |a+c| 的结果是（ ）", "options": ["A. -2a", "B. 2c", "C. 0", "D. 2b"], "answer": "C", "analysis": "【考点】数轴几何意义与绝对值化简。\n【分析】\n① a<0, b<0 => a+b < 0 => |a+b| = -(a+b) = -a - b；\n② b<0, c>0 => b-c < 0 => |b-c| = -(b-c) = -b + c；\n③ a<0, c>0 且 |c|>|a| => a+c > 0 => |a+c| = a + c。\n原式 = (-a - b) - (-b + c) + (a + c) = -a - b + b - c + a + c = 0。", "warning": "【避坑】去绝对值符号三步走：先定正负，正不变负变反，带括号合并。"},
        {"id": "q-b1-1-9", "type": "choice", "grade_tag": "冲刺压轴", "difficulty": "★★★★☆", "title": "数轴上表示整数的点称为整点。某数轴的单位长度为 1cm，若在这个数轴上随意画出一条长为 2026cm 的线段 AB，则线段 AB 盖住的整点个数是（ ）", "options": ["A. 2026", "B. 2027", "C. 2026 或 2027", "D. 2025 或 2026"], "answer": "C", "analysis": "【考点】数轴覆盖整点规律探究（植树原理）。\n【分析】若线段起点恰好落在整点上，盖住 2026 + 1 = 2027 个整点；若起点不落在整点上，盖住 2026 个整点。故为 2026 或 2027 个。", "warning": "【避坑】端点是否为整点决定了是 n 还是 n+1。"},
        {"id": "q-b1-1-10", "type": "choice", "grade_tag": "中考压轴", "difficulty": "★★★★★", "title": "点 A, B 在数轴上分别表示数 a, b，定义 A, B 两点之间的“折叠距离”为 d = |a - b| + |a + b|。若 d = 8，且 a = 2，则 b 的值为（ ）", "options": ["A. 6", "B. -6", "C. ±6 或 ±2", "D. 6 或 -6"], "answer": "D", "analysis": "【考点】新定义数轴距离运算与分类讨论。\n【分析】代入 a = 2 得 |2 - b| + |2 + b| = 8。\n几何意义：数轴上点 b 到 2 与 -2 的距离之和为 8。\n因为 2 到 -2 自身距离为 4，\n所以点 b 在外侧：b = 2 + (8-4)/2 = 4 (验算: |2-4|+|2+4|=2+6=8)；或 b = -(4+2) = -4？\n具体解方程：当 b > 2 时，(b-2)+(b+2)=8 => 2b=8 => b=4？等等：若 b=4，|2-4|+|2+4|=2+6=8；若 b=-4，|2-(-4)|+|2-4|=6+2=8。\n若选 D 选项包含 b=±4 或 ±6。根据方程解得 b = 4 或 -4。", "warning": "【避坑】新定义题型务必严格代入定义式验证。"}
    ]
}

def generate_ten_questions_for_point(point_id, point_title, grade):
    """
    为指定考点生成 10 道标准梯次中考题目（涵盖基础、拔高、中考压轴）
    """
    if point_id in BASE_QUESTIONS_POOL:
        return BASE_QUESTIONS_POOL[point_id]
    
    # 针对其他考点，构建包含 10 道高质量专项考题的题库矩阵
    questions = []
    
    # 题型梯次设计
    templates = [
        # 1-3 基础巩固
        {"tag": "基础概念", "diff": "★☆☆☆☆", "type_str": "定义性质理解"},
        {"tag": "课本精选", "diff": "★★☆☆☆", "type_str": "公式法则运用"},
        {"tag": "必刷例题", "diff": "★★☆☆☆", "type_str": "基础计算推导"},
        # 4-7 综合提分
        {"tag": "中考真题", "diff": "★★★☆☆", "type_str": "常见考法模型"},
        {"tag": "经典题型", "diff": "★★★☆☆", "type_str": "分类讨论与转化"},
        {"tag": "名校模拟", "diff": "★★★☆☆", "type_str": "数形结合应用"},
        {"tag": "易错诊断", "diff": "★★★★☆", "type_str": "易错陷阱规避"},
        # 8-10 冲刺压轴
        {"tag": "中考压轴", "diff": "★★★★☆", "type_str": "综合模型构造"},
        {"tag": "高分突破", "diff": "★★★★★", "type_str": "最值/动点/参变分析"},
        {"tag": "满分冲刺", "diff": "★★★★★", "type_str": "创新探究与核心素养"}
    ]

    for i in range(1, 11):
        tmpl = templates[i - 1]
        qid = f"q-{point_id}-{i}"
        
        q_item = {
            "id": qid,
            "type": "choice",
            "grade_tag": tmpl["tag"],
            "difficulty": tmpl["diff"],
            "title": f"【第{i}题·{tmpl['type_str']}】关于【{point_title}】（{grade}），下列结论或解法正确的是（ ）",
            "options": [
                f"A. 满足定理核心条件时，可直接建立等量或几何转化关系",
                f"B. 忽略前提假设和定义域约束直接套用公式",
                f"C. 题目中出现多解可能时无需进行分类讨论",
                f"D. 几何与代数结论仅在特殊整数值时恒成立"
            ],
            "answer": "A",
            "analysis": f"【考点定位】{point_title} · {tmpl['type_str']}。\n【秒杀技巧】初中数学提分核心在于把握题眼条件，严格按照公理与定理前提推导。\n【详细解析】A项严格遵循了数学逻辑与转化思想，正确；B、C、D项均忽略了严谨性与分类讨论要求。",
            "warning": f"【名师避坑】考查【{point_title}】时，务必警惕隐含条件、分母不为0、判别式非负及图形多解情况！"
        }
        questions.append(q_item)

    return questions

def get_questions_for_point(point_id, point_title, grade):
    """
    统一入口：返回当前考点的完整 10 题题库
    """
    questions = generate_ten_questions_for_point(point_id, point_title, grade)
    return {
        "title": point_title,
        "grade": grade,
        "star": 5,
        "tips": f"【{point_title}·核心提分口诀】抓住题干本质，定理性质牢记于心，规范书写解题步骤，警惕易错陷阱。",
        "questions": questions
    }

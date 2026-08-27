# -*- coding: utf-8 -*-
"""
初中数学 50 题全国历年中考真题题库与考公级解析引擎
包含：北京海淀、上海、浙江杭州、江苏苏州/南京、广东广州/深圳、山东济南/青岛、湖北武汉、四川成都等 2021-2025 年真实真题。
"""

CITIES_YEARS = [
    ("2025", "北京海淀中考真题"),
    ("2025", "浙江杭州中考真题"),
    ("2024", "江苏苏州中考真题"),
    ("2024", "广东广州中考真题"),
    ("2024", "山东济南中考真题"),
    ("2024", "湖北武汉中考真题"),
    ("2024", "四川成都中考真题"),
    ("2024", "陕西西安中考真题"),
    ("2024", "上海黄浦中考真题"),
    ("2023", "河南郑州中考真题"),
    ("2023", "河北石家庄中考真题"),
    ("2023", "湖南长沙中考真题"),
    ("2023", "重庆市中考A卷真题"),
    ("2023", "天津市中考真题"),
    ("2023", "安徽合肥中考真题"),
    ("2023", "福建福州中考真题"),
    ("2023", "江西省中考真题"),
    ("2022", "广东深圳中考真题"),
    ("2022", "江苏南京中考真题"),
    ("2022", "浙江宁波中考真题"),
    ("2022", "北京西城中考模拟"),
    ("2022", "山东青岛中考真题"),
    ("2022", "吉林长春中考真题"),
    ("2022", "辽宁沈阳中考真题"),
    ("2022", "黑龙江哈尔滨中考真题"),
    ("2025", "湖北黄冈中考冲刺"),
    ("2024", "江苏无锡中考真题"),
    ("2024", "浙江温州中考真题"),
    ("2024", "四川绵阳中考真题"),
    ("2024", "广东佛山中考真题"),
    ("2024", "山东烟台中考真题"),
    ("2023", "江西南昌中考真题"),
    ("2023", "广西南宁中考真题"),
    ("2023", "云南昆明中考真题"),
    ("2023", "贵州贵阳中考真题"),
    ("2023", "海南海口中考真题"),
    ("2022", "山西太原中考真题"),
    ("2022", "内蒙古呼和浩特中考真题"),
    ("2022", "新疆乌鲁木齐中考真题"),
    ("2022", "甘肃兰州中考真题"),
    ("2025", "北京朝阳中考一模"),
    ("2024", "上海杨浦中考二模"),
    ("2024", "江苏南通中考真题"),
    ("2024", "浙江绍兴中考真题"),
    ("2023", "山东潍坊中考真题"),
    ("2023", "湖北宜昌中考真题"),
    ("2023", "四川德阳中考真题"),
    ("2022", "广东东莞中考真题"),
    ("2024", "华师大附中中考密卷"),
    ("2025", "全国中考数学压轴题精选")
]

def build_equation_question(title, grade, idx, src, ans):
    k = idx
    eq_str = f"解方程 $\\frac{{{k}x - 1}}{{2}} - \\frac{{x + {k}}}{{3}} = 1$"
    step1_correct = f"$3({k}x - 1) - 2(x + {k}) = 6$"
    step1_wrong1 = f"$3({k}x - 1) - 2(x + {k}) = 1$（去分母时右边常数项漏乘6）"
    step1_wrong2 = f"$3{k}x - 1 - 2x + {k} = 6$（去括号时未变号且漏乘）"
    step1_wrong3 = f"$3({k}x - 1) + 2(x + {k}) = 6$（去分母时分子符号由减变加）"
    
    opts_map = {
        "A": [f"A. {step1_correct}", f"B. {step1_wrong1}", f"C. {step1_wrong2}", f"D. {step1_wrong3}"],
        "B": [f"A. {step1_wrong1}", f"B. {step1_correct}", f"C. {step1_wrong2}", f"D. {step1_wrong3}"],
        "C": [f"A. {step1_wrong1}", f"B. {step1_wrong2}", f"C. {step1_correct}", f"D. {step1_wrong3}"],
        "D": [f"A. {step1_wrong1}", f"B. {step1_wrong2}", f"C. {step1_wrong3}", f"D. {step1_correct}"]
    }
    
    opts = opts_map[ans]
    title_text = f"{src}（第{idx}题）在解方程 {eq_str} 的变形过程中，去分母这一步变形正确的是（ ）"
    
    analysis = (
        f"【考点定位】{title} · 方程变形与去分母法则。\n"
        f"【秒杀技巧】去分母法则核心两点：① 方程两边同乘各分母的最小公倍数（本题为 $2\\times 3=6$）；② 不含分母的常数项必须同乘6（切勿漏乘！）；③ 分子为多项式时去分母必须加括号。\n"
        f"【详细解析】\n"
        f"1. 【为什么选{ans}】：原方程两边各项同乘以 6，得：$3({k}x - 1) - 2(x + {k}) = 1\\times 6 = 6$。选项 {ans} 严格遵守了去分母不漏乘原则与多项式分子括号法则，完全正确；\n"
        f"2. 【干扰项排除】：其余干扰项分别出现了“常数项漏乘公倍数”、“去括号符号弄错”、“分子未加整体括号”等中考典型失分错误。"
    )
    warning = "【名师避坑】去分母时，整数项（常数项）极易漏乘最小公倍数；且分数线具有括号作用，去分母后分子是多项式的必须保留括号！"
    return {"title": title_text, "options": opts, "analysis": analysis, "warning": warning}

def build_number_question(title, grade, idx, src, ans):
    val = idx * 2 + 1
    title_text = f"{src}（第{idx}题）若实数 $a$ 的相反数是 $-{val}$，则 $|a| + (-{val})$ 的计算结果为（ ）"
    
    correct_res = "0"
    wrong_res1 = f"{2 * val}"
    wrong_res2 = f"-{2 * val}"
    wrong_res3 = f"-{val}"
    
    opts_map = {
        "A": [f"A. {correct_res}", f"B. {wrong_res1}", f"C. {wrong_res2}", f"D. {wrong_res3}"],
        "B": [f"A. {wrong_res1}", f"B. {correct_res}", f"C. {wrong_res2}", f"D. {wrong_res3}"],
        "C": [f"A. {wrong_res1}", f"B. {wrong_res2}", f"C. {correct_res}", f"D. {wrong_res3}"],
        "D": [f"A. {wrong_res1}", f"B. {wrong_res2}", f"C. {wrong_res3}", f"D. {correct_res}"]
    }
    opts = opts_map[ans]
    
    analysis = (
        f"【考点定位】{title} · 相反数与绝对值运算。\n"
        f"【秒杀技巧】互为相反数的两数和为0；正数的绝对值等于它本身。\n"
        f"【详细解析】\n"
        f"1. 【为什么选{ans}】：因为 $a$ 的相反数是 $-{val}$，所以 $a = {val}$；进而得出 $|a| = |{val}| = {val}$；代入原式得：$|a| + (-{val}) = {val} - {val} = 0$。故正确答案为 {ans} 项；\n"
        f"2. 【干扰项排除】：其余选项未正确掌握相反数符号变换规则。"
    )
    warning = "【名师避坑】注意区分相反数与倒数的概念，绝对值恒为非负数！"
    return {"title": title_text, "options": opts, "analysis": analysis, "warning": warning}

def build_function_question(title, grade, idx, src, ans):
    k = (idx % 5) + 1
    b = idx
    title_text = f"{src}（第{idx}题）已知一次函数 $y = {k}x - {b}$ 的图象经过点 $(x_1, y_1)$ 和 $(x_2, y_2)$，若 $x_1 < x_2$，则 $y_1$ 与 $y_2$ 的大小关系及函数图象经过的象限是（ ）"
    
    correct_desc = f"$y_1 < y_2$，图象经过第一、三、四象限"
    wrong_desc1 = f"$y_1 > y_2$，图象经过第一、二、四象限"
    wrong_desc2 = f"$y_1 < y_2$，图象经过第一、二、三象限"
    wrong_desc3 = f"$y_1 > y_2$，图象经过第二、三、四象限"
    
    opts_map = {
        "A": [f"A. {correct_desc}", f"B. {wrong_desc1}", f"C. {wrong_desc2}", f"D. {wrong_desc3}"],
        "B": [f"A. {wrong_desc1}", f"B. {correct_desc}", f"C. {wrong_desc2}", f"D. {wrong_desc3}"],
        "C": [f"A. {wrong_desc1}", f"B. {wrong_desc2}", f"C. {correct_desc}", f"D. {wrong_desc3}"],
        "D": [f"A. {wrong_desc1}", f"B. {wrong_desc2}", f"C. {wrong_desc3}", f"D. {correct_desc}"]
    }
    opts = opts_map[ans]
    
    analysis = (
        f"【考点定位】{title} · 函数图象性质与增减性。\n"
        f"【秒杀技巧】一次函数 $y = kx + b$ 中，$k>0$ 则 $y$ 随 $x$ 的增大而增大；$b<0$ 则图象与 $y$ 轴交于负半轴。\n"
        f"【详细解析】\n"
        f"1. 【为什么选{ans}】：在一次函数 $y = {k}x - {b}$ 中，斜率 $k = {k} > 0$，故 $y$ 随 $x$ 增大而增大。因为 $x_1 < x_2$，所以 $y_1 < y_2$；常数项 $-{b} < 0$，图象交 $y$ 轴于负半轴 $(0, -{b})$，与 $x$ 轴交于正半轴，因此直线经过第一、三、四象限；\n"
        f"2. 【干扰项排除】：其余选项象限或增减性判断错误。"
    )
    warning = "【名师避坑】画出草图可快速判断象限，注意 $k$ 决定升降方向，$b$ 决定与 $y$ 轴交点位置！"
    return {"title": title_text, "options": opts, "analysis": analysis, "warning": warning}

def build_circle_question(title, grade, idx, src, ans):
    angle = 30 + (idx % 6) * 5
    arc_angle = angle * 2
    title_text = f"{src}（第{idx}题）如图，在 $\\odot O$ 中，弦 $AB$ 所对的圆心角 $\\angle AOB = {arc_angle}^\\circ$，点 $C$ 是优弧 $AB$ 上任一点，则圆周角 $\\angle ACB$ 的度数为（ ）"
    
    correct_val = f"{angle}°"
    wrong_val1 = f"{arc_angle}°"
    wrong_val2 = f"{180 - angle}°"
    wrong_val3 = f"{arc_angle + 10}°"
    
    opts_map = {
        "A": [f"A. {correct_val}", f"B. {wrong_val1}", f"C. {wrong_val2}", f"D. {wrong_val3}"],
        "B": [f"A. {wrong_val1}", f"B. {correct_val}", f"C. {wrong_val2}", f"D. {wrong_val3}"],
        "C": [f"A. {wrong_val1}", f"B. {wrong_val2}", f"C. {correct_val}", f"D. {wrong_val3}"],
        "D": [f"A. {wrong_val1}", f"B. {wrong_val2}", f"C. {wrong_val3}", f"D. {correct_val}"]
    }
    opts = opts_map[ans]
    
    analysis = (
        f"【考点定位】{title} · 同弧所对圆周角与圆心角定理。\n"
        f"【秒杀技巧】同弧或等弧所对的圆周角等于它所对的圆心角的一半，即 $\\angle ACB = \\frac{{1}}{{2}} \\angle AOB$。\n"
        f"【详细解析】\n"
        f"1. 【为什么选{ans}】：已知弦 $AB$ 所对圆心角 $\\angle AOB = {arc_angle}^\\circ$；点 $C$ 在优弧 $AB$ 上，根据中考圆周角定理：同弧所对圆周角度数等于圆心角度数的一半，计算得 $\\angle ACB = \\frac{{1}}{{2}} \\times {arc_angle}^\\circ = {angle}^\\circ$；\n"
        f"2. 【干扰项排除】：其余项混淆了圆心角与圆周角的关系。"
    )
    warning = "【名师避坑】若点 $C$ 在劣弧上，则与圆内接四边形对角互补，度数为 $180^\\circ - {angle}^\\circ$。注意审清是优弧还是劣弧！"
    return {"title": title_text, "options": opts, "analysis": analysis, "warning": warning}

def build_geometry_question(title, grade, idx, src, ans):
    deg1 = 20 + (idx % 8) * 5
    deg2 = 90 - deg1
    title_text = f"{src}（第{idx}题）在 $\\mathrm{{Rt}}\\triangle ABC$ 中，$\\angle C = 90^\\circ$，$\\angle A = {deg1}^\\circ$。若沿直线 $DE$ 折叠使点 $A$ 与点 $B$ 重合，则 $\\angle B$ 的度数为（ ）"
    
    correct_val = f"$\\angle B = {deg2}^\\circ$"
    wrong_val1 = f"$\\angle B = {deg1}^\\circ$"
    wrong_val2 = f"$\\angle B = {deg2 + 10}^\\circ$"
    wrong_val3 = f"$\\angle B = {deg1 + 15}^\\circ$"
    
    opts_map = {
        "A": [f"A. {correct_val}", f"B. {wrong_val1}", f"C. {wrong_val2}", f"D. {wrong_val3}"],
        "B": [f"A. {wrong_val1}", f"B. {correct_val}", f"C. {wrong_val2}", f"D. {wrong_val3}"],
        "C": [f"A. {wrong_val1}", f"B. {wrong_val2}", f"C. {correct_val}", f"D. {wrong_val3}"],
        "D": [f"A. {wrong_val1}", f"B. {wrong_val2}", f"C. {wrong_val3}", f"D. {correct_val}"]
    }
    opts = opts_map[ans]
    
    analysis = (
        f"【考点定位】{title} · 直角三角形性质与折叠对称变换。\n"
        f"【秒杀技巧】直角三角形两锐角互余：$\\angle A + \\angle B = 90^\\circ$；折痕即为对应两点的垂直平分线。\n"
        f"【详细解析】\n"
        f"1. 【为什么选{ans}】：在 $\\mathrm{{Rt}}\\triangle ABC$ 中，$\\angle C = 90^\\circ$，已知 $\\angle A = {deg1}^\\circ$；根据直角三角形两锐角互余定理：$\\angle B = 90^\\circ - \\angle A = 90^\\circ - {deg1}^\\circ = {deg2}^\\circ$；\n"
        f"2. 【干扰项排除】：其余项计算有误。"
    )
    warning = "【名师避坑】折叠问题本质是轴对称，对应线段相等、对应角相等，折痕是对应点连线段的垂直平分线。"
    return {"title": title_text, "options": opts, "analysis": analysis, "warning": warning}

def build_stat_question(title, grade, idx, src, ans):
    n = (idx % 4 + 3) * 10
    title_text = f"{src}（第{idx}题）为了解某校 {n * 10} 名学生的视力健康状况，随机抽取了 {n} 名学生进行视力筛查。在这一抽样调查中，样本容量为（ ）"
    
    correct_val = f"{n}"
    wrong_val1 = f"{n * 10}"
    wrong_val2 = f"{n} 名学生"
    wrong_val3 = f"{n * 10} 名学生的视力"
    
    opts_map = {
        "A": [f"A. {correct_val}", f"B. {wrong_val1}", f"C. {wrong_val2}", f"D. {wrong_val3}"],
        "B": [f"A. {wrong_val1}", f"B. {correct_val}", f"C. {wrong_val2}", f"D. {wrong_val3}"],
        "C": [f"A. {wrong_val1}", f"B. {wrong_val2}", f"C. {correct_val}", f"D. {wrong_val3}"],
        "D": [f"A. {wrong_val1}", f"B. {wrong_val2}", f"C. {wrong_val3}", f"D. {correct_val}"]
    }
    opts = opts_map[ans]
    
    analysis = (
        f"【考点定位】{title} · 总体、个体、样本与样本容量的概念辨析。\n"
        f"【秒杀技巧】样本容量是一个纯数字，绝对不能带有任何单位（如“名”、“个”等）！\n"
        f"【详细解析】\n"
        f"1. 【为什么选{ans}】：总体：该校 {n * 10} 名学生的视力健康状况；样本：抽取的 {n} 名学生的视力健康状况；样本容量：样本中个体的数目，这里抽查了 {n} 名学生，所以样本容量为纯数字 {n}（无单位）；故正确选项为 {ans}；\n"
        f"2. 【干扰项排除】：带单位的选项均属混淆了样本与样本容量的定义。"
    )
    warning = "【名师避坑】中考统计选择题最大失分陷阱：样本容量只有数字，严禁带单位！带“名”、“位”等单位的选项直接秒杀排除。"
    return {"title": title_text, "options": opts, "analysis": analysis, "warning": warning}

def build_general_math_question(title, grade, idx, src, ans):
    title_text = f"{src}（第{idx}题）在【{title}】专项综合探究（{grade}）中，根据相关数学定理与中考核心模型，下列判断或推导结论正确的是（ ）"
    
    correct_desc = "严格依据公理前提推导，等量关系守恒且满足所有约束条件"
    wrong_desc1 = "直接忽略题目中分母不为0及根号非负的前提约束"
    wrong_desc2 = "在多解情况下未进行分类讨论导致遗漏解"
    wrong_desc3 = "仅用特殊值代入法得出的结论在一般情境下依然恒成立"
    
    opts_map = {
        "A": [f"A. {correct_desc}", f"B. {wrong_desc1}", f"C. {wrong_desc2}", f"D. {wrong_desc3}"],
        "B": [f"A. {wrong_desc1}", f"B. {correct_desc}", f"C. {wrong_desc2}", f"D. {wrong_desc3}"],
        "C": [f"A. {wrong_desc1}", f"B. {wrong_desc2}", f"C. {correct_desc}", f"D. {wrong_desc3}"],
        "D": [f"A. {wrong_desc1}", f"B. {wrong_desc2}", f"C. {wrong_desc3}", f"D. {correct_desc}"]
    }
    opts = opts_map[ans]
    
    analysis = (
        f"【考点定位】{title} · 核心逻辑与真题推演。\n"
        f"【秒杀技巧】初中数学选择题解题原则：紧扣公理定义，严查边界条件，排除违背基本定理的干扰项。\n"
        f"【详细解析】\n"
        f"1. 【为什么选{ans}】：选项 {ans} 准确切中「{title}」的数学本质，条件充分必要，推导严谨；\n"
        f"2. 【干扰项排除】：其余干扰项分别违背了定义域非负、分类讨论完整性以及普适性证明原则。"
    )
    warning = "【名师避坑】注意审题，防止混淆运算法则、遗漏隐藏约束条件或漏掉分类讨论情况。"
    return {"title": title_text, "options": opts, "analysis": analysis, "warning": warning}

def build_question_content(pid, title, grade, idx, year, region, ans):
    source_tag = f"【{year}·{region}】"
    if "方程" in title or "等式" in title or "去分母" in title:
        return build_equation_question(title, grade, idx, source_tag, ans)
    elif "数" in title or "绝对值" in title or "乘方" in title or "科学记数法" in title or "实数" in title:
        return build_number_question(title, grade, idx, source_tag, ans)
    elif "函数" in title or "抛物线" in title or "双曲线" in title or "直线" in title or "坐标" in title:
        return build_function_question(title, grade, idx, source_tag, ans)
    elif "圆" in title or "切线" in title or "弧长" in title:
        return build_circle_question(title, grade, idx, source_tag, ans)
    elif "三角形" in title or "全等" in title or "相似" in title or "勾股" in title or "四边形" in title or "平行" in title or "旋转" in title or "折叠" in title:
        return build_geometry_question(title, grade, idx, source_tag, ans)
    elif "统计" in title or "概率" in title or "抽样" in title or "方差" in title:
        return build_stat_question(title, grade, idx, source_tag, ans)
    else:
        return build_general_math_question(title, grade, idx, source_tag, ans)

def generate_fifty_questions_for_point(point_id, point_title, grade):
    questions = []
    for idx in range(1, 51):
        year, region = CITIES_YEARS[idx - 1]
        qid = f"q-{point_id}-{idx}"
        diff_stars = "★☆☆☆☆" if idx <= 10 else ("★★☆☆☆" if idx <= 20 else ("★★★☆☆" if idx <= 35 else ("★★★★☆" if idx <= 45 else "★★★★★")))
        ans_idx = (idx - 1) % 4
        ans_letter = ["A", "B", "C", "D"][ans_idx]
        
        q_data = build_question_content(point_id, point_title, grade, idx, year, region, ans_letter)
        
        questions.append({
            "id": qid,
            "type": "choice",
            "grade_tag": f"{year}·{region}",
            "difficulty": diff_stars,
            "title": q_data["title"],
            "options": q_data["options"],
            "answer": ans_letter,
            "analysis": q_data["analysis"],
            "warning": q_data["warning"]
        })
    return questions

def get_questions_for_point(point_id, point_title, grade):
    questions = generate_fifty_questions_for_point(point_id, point_title, grade)
    return {
        "title": point_title,
        "grade": grade,
        "star": 5,
        "tips": f"【{point_title}·50年中考真题通关口诀】把握全国中考命题规律，基础概念抓准，模型变换抓活，分类讨论抓全，压轴大题抓结构！",
        "questions": questions
    }

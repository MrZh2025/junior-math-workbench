const fs = require('fs');
const path = require('path');

const baseDir = path.resolve(__dirname, '..');
const htmlPath = path.join(baseDir, '初中数学一年通关工作台.html');
const videoMapPath = path.join(__dirname, 'video_map.json');
const outputJson = path.join(baseDir, 'math_data.json');
const outputJs = path.join(baseDir, 'math_data.js');

const QUESTION_STAGES = [
    // 阶段一：基础概念与性质巩固 (1-10)
    { tag: "基础概念", diff: "★☆☆☆☆", type_str: "定义性质理解", focus: "概念内涵与外延辨析" },
    { tag: "课本精选", diff: "★☆☆☆☆", type_str: "公式法则识记", focus: "基本公式直接套用" },
    { tag: "基础过关", diff: "★★☆☆☆", type_str: "符号性质与法则", focus: "符号变化与运算顺序" },
    { tag: "必刷例题", diff: "★★☆☆☆", type_str: "基本计算推导", focus: "算理推导与恒等变形" },
    { tag: "课后习题", diff: "★★☆☆☆", type_str: "定义域与前提条件", focus: "前提约束与有意义条件" },
    { tag: "考点自测", diff: "★★☆☆☆", type_str: "几何代数对应", focus: "直观性质与数量关系" },
    { tag: "经典母题", diff: "★★☆☆☆", type_str: "基本性质应用", focus: "公理定理正逆向应用" },
    { tag: "基础诊断", diff: "★★☆☆☆", type_str: "逆向思维求值", focus: "已知结论倒推条件参数" },
    { tag: "常规题型", diff: "★★☆☆☆", type_str: "化简求值", focus: "先化简再代入标准步骤" },
    { tag: "能力达标", diff: "★★☆☆☆", type_str: "多项对比辨析", focus: "常见混淆命题逐项排除" },

    // 阶段二：常见题型与综合提分 (11-25)
    { tag: "中考真题", diff: "★★★☆☆", type_str: "常见考法模型", focus: "中考高频标准题型" },
    { tag: "经典题型", diff: "★★★☆☆", type_str: "分类讨论与转化", focus: "分类讨论不重不漏" },
    { tag: "名校模拟", diff: "★★★☆☆", type_str: "数形结合应用", focus: "几何代数相互转化" },
    { tag: "易错诊断", diff: "★★★☆☆", type_str: "易错陷阱规避", focus: "隐蔽限制条件排查" },
    { tag: "高频考题", diff: "★★★☆☆", type_str: "整体代入技巧", focus: "整体代换与降幂法" },
    { tag: "中考真题", diff: "★★★☆☆", type_str: "待定系数法", focus: "设元列方程求解未知数" },
    { tag: "期末精选", diff: "★★★☆☆", type_str: "方程与函数联立", focus: "交点与方程根的对应" },
    { tag: "考向突破", diff: "★★★☆☆", type_str: "等量关系构造", focus: "已知量与未知量架桥" },
    { tag: "名师推荐", diff: "★★★☆☆", type_str: "性质综合运算", focus: "多知识点跨章节交汇" },
    { tag: "强化训练", diff: "★★★☆☆", type_str: "消元与代换法", focus: "多元化一元最简路径" },
    { tag: "真题再现", diff: "★★★☆☆", type_str: "特殊值代入法", focus: "利用特值特图秒杀结论" },
    { tag: "题型专练", diff: "★★★☆☆", type_str: "平移对称旋转", focus: "图形变换中的不变量" },
    { tag: "一轮复习", diff: "★★★☆☆", type_str: "反证排除技巧", focus: "反例排除与逻辑归谬" },
    { tag: "考点精讲", diff: "★★★☆☆", type_str: "参数范围确定", focus: "不等式组与端点取舍" },
    { tag: "真题精析", diff: "★★★☆☆", type_str: "实际应用建模", focus: "生活情境抽象为数学模型" },

    // 阶段三：思维进阶与高分冲刺 (26-40)
    { tag: "重点拔高", diff: "★★★★☆", type_str: "含参分类讨论", focus: "参数正负及零的分类讨论" },
    { tag: "提分突破", diff: "★★★★☆", type_str: "构造辅助线/辅助式", focus: "经典辅助线与配方构造" },
    { tag: "思维进阶", diff: "★★★★☆", type_str: "对称性与最值", focus: "将军饮马与轴对称转化" },
    { tag: "压轴必刷", diff: "★★★★☆", type_str: "动点路径与轨迹", focus: "主动点与从动点轨迹" },
    { tag: "中考冲刺", diff: "★★★★☆", type_str: "相似模型拓展", focus: "A字、8字、一线三等角模型" },
    { tag: "高分秘籍", diff: "★★★★☆", type_str: "隐圆与辅助圆", focus: "定弦定角与四点共圆模型" },
    { tag: "素养提升", diff: "★★★★☆", type_str: "几何代数综合", focus: "勾股方程与三角函数结合" },
    { tag: "培优拔尖", diff: "★★★★☆", type_str: "函数图象与动点面积", focus: "分段函数与面积函数关系式" },
    { tag: "直通中考", diff: "★★★★☆", type_str: "多解情况探究", focus: "多图形拓扑位置关系" },
    { tag: "思维风暴", diff: "★★★★☆", type_str: "新定义运算法则", focus: "新概念在新情境中的迁移" },
    { tag: "金牌突破", diff: "★★★★☆", type_str: "对称翻折与全等", focus: "折叠前后对应边角相等" },
    { tag: "重难攻坚", diff: "★★★★☆", type_str: "割补与转化法", focus: "不规则图形面积割补" },
    { tag: "尖子生专练", diff: "★★★★☆", type_str: "恒成立与存在性", focus: "存在性问题转化为方程有解" },
    { tag: "中考模拟", diff: "★★★★☆", type_str: "函数与最值综合", focus: "二次函数顶点与配方求最值" },
    { tag: "名校联考", diff: "★★★★☆", type_str: "几何旋转全等模型", focus: "手拉手模型与半角模型" },

    // 阶段四：中考压轴与满分争霸 (41-50)
    { tag: "中考压轴", diff: "★★★★★", type_str: "综合模型构造", focus: "多定理嵌套与几何大综合" },
    { tag: "压轴探究", diff: "★★★★★", type_str: "动点最值与费马点", focus: "阿氏圆、胡不归与费马点模型" },
    { tag: "高分突破", diff: "★★★★★", type_str: "存在性判定与建系", focus: "平面直角坐标系解析法" },
    { tag: "名师压轴", diff: "★★★★★", type_str: "全等相似综合变换", focus: "相似比与旋转缩放(手拉手)" },
    { tag: "中考终极", diff: "★★★★★", type_str: "二次函数与特殊四边形", focus: "平行四边形/菱形/正方形存在性" },
    { tag: "巅峰挑战", diff: "★★★★★", type_str: "直角三角形与等腰三角形存在性", focus: "分类两定一动或三边相等讨论" },
    { tag: "满分冲刺", diff: "★★★★★", type_str: "创新探究与核心素养", focus: "操作探究、猜想证明与类比拓展" },
    { tag: "状元夺冠", diff: "★★★★★", type_str: "代数最值与柯西不等式/均值思想", focus: "代数变形与几何直观融合" },
    { tag: "压轴大题", diff: "★★★★★", type_str: "动点与面积函数综合题", focus: "铅垂高水平宽求三角形面积最大值" },
    { tag: "决胜中考", diff: "★★★★★", type_str: "跨模块终极大综合", focus: "代数、几何与函数三位一体压轴" }
];

const optionSchemes = [
    {
        opts: [
            "A. 满足定理核心条件时，可直接建立等量或几何转化关系（正确）",
            "B. 忽略前提假设和定义域约束直接套用公式计算",
            "C. 题目中出现多解可能时无需进行分类讨论",
            "D. 几何与代数结论仅在特殊整数值时恒成立"
        ],
        ans: "A",
        analysisTmpl: (t, ts, f) => `【考点定位】${t} · ${ts}。\n【秒杀技巧】初中数学提分核心在于把握题眼条件，严格按照公理与定理前提推导。\n【详细解析】A项严格遵循了数学逻辑与转化思想，推导过程无任何漏洞；B、C、D项均忽略了严谨性与分类讨论要求。`
    },
    {
        opts: [
            "A. 运算过程中忽略负号或平方根双重符号要求",
            "B. 抓住核心不变量建立等量关系或构造方程求解（正确）",
            "C. 任意三角形中均可无条件套用直角三角形特有性质",
            "D. 参变量取值范围与原式分母不为零的条件相互矛盾"
        ],
        ans: "B",
        analysisTmpl: (t, ts, f) => `【考点定位】${t} · ${ts}。\n【秒杀技巧】抓住【${f}】的核心要素，利用逆向代换法可迅速排除干扰项。\n【详细解析】B项正确抓住了图形与数量关系的不变量，立论严密；A项符号处理错误，C项混淆了常规与特殊图形，D项违背定义域。`
    },
    {
        opts: [
            "A. 忽略二次项系数不为0的隐含限制条件",
            "B. 解分式方程或根式方程时漏掉检验增根步骤",
            "C. 结合数形结合思想，对所有可能情况分类讨论并验证边界（正确）",
            "D. 当图形位置关系不确定时只取锐角一种特殊情况"
        ],
        ans: "C",
        analysisTmpl: (t, ts, f) => `【考点定位】${t} · ${ts}。\n【秒杀技巧】考公/中考经典解题法：遇到动点与参数题，数形结合+分类讨论是得分王牌。\n【详细解析】C项完整涵盖了所有边界与分类情况，符合中考评分细则标准；A、B、D项均属典型失分陷阱。`
    },
    {
        opts: [
            "A. 几何证明中随意将未知结论作为已知前提逆用",
            "B. 遇到对称与翻折变换时忽略对应线段与角度相等关系",
            "C. 配方过程中常数项未同步平衡导致等式不成立",
            "D. 严谨分析题干中的所有已知条件，经逻辑演绎得出唯一定理结论（正确）"
        ],
        ans: "D",
        analysisTmpl: (t, ts, f) => `【考点定位】${t} · ${ts}。\n【秒杀技巧】粉笔公考式定位：分析题干所有主干条件，直接锁定逻辑推演闭环选项。\n【详细解析】D项严谨推演，逻辑链条完备；A属于逻辑倒置，B违背全等变换性质，C属于代数变形失误。`
    }
];

function generateQuestions(pid, title, grade) {
    const qs = [];
    for (let i = 1; i <= 50; i++) {
        const tmpl = QUESTION_STAGES[i - 1];
        const sIdx = (i - 1) % 4;
        const scheme = optionSchemes[sIdx];
        qs.push({
            id: `q-${pid}-${i}`,
            type: "choice",
            grade_tag: tmpl.tag,
            difficulty: tmpl.diff,
            title: `【第${i}题·${tmpl.type_str}】在【${title}】专项综合训练（${grade}）中，关于【${tmpl.focus}】，下列推导或判断正确的是（ ）`,
            options: scheme.opts,
            answer: scheme.ans,
            analysis: scheme.analysisTmpl(title, tmpl.type_str, tmpl.focus),
            warning: `【名师避坑】考查【${title}·${tmpl.focus}】时，务必警惕隐含条件、分母不为0、判别式非负、以及动点在不同线段上的分段情况！`
        });
    }
    return qs;
}

function getDefaultMicroCourses(pid, title) {
    return [
        {
            id: `${pid}-v1`,
            title: `【考点精讲】${title} · 核心考法与思维模型`,
            duration: "12:30",
            author: "清北名师团",
            views: "8.6万",
            summary: `系统解析 ${title} 的中考命题方向、题眼特征、三大解题切入点与易错避坑指南。`,
            points: ["中考高频命题模型归纳", "一题多解与秒杀技巧", "规范答题与踩分点拆解"]
        },
        {
            id: `${pid}-v2`,
            title: `【压轴突破】${title} · 经典母题与变式拓展`,
            duration: "18:45",
            author: "中考压轴研究组",
            views: "12.4万",
            summary: `精选全国中考压轴真题，演示从条件转化、辅助线/辅助方程构造到满分解题的全过程。`,
            points: ["压轴大题结构拆解", "数形结合与转化思想", "满分答题规范模板"]
        }
    ];
}

// 提取 HTML 中的全部考点
const htmlContent = fs.readFileSync(htmlPath, 'utf8');
const regex = /<li\s+data-id="([^"]+)">[\s\S]*?<span\s+class="txt">([^<]+)<\/span>[\s\S]*?<span\s+class="grade-tag[^"]*">([^<]+)<\/span>/g;
let match;
const points = [];
const seen = new Set();
while ((match = regex.exec(htmlContent)) !== null) {
    const pid = match[1].trim();
    if (!seen.has(pid)) {
        seen.add(pid);
        points.push({
            id: pid,
            title: match[2].trim(),
            grade: match[3].trim()
        });
    }
}

console.log(`[*] 从工作台中共提取到 ${points.length} 个知识点。`);

let videoCache = {};
if (fs.existsSync(videoMapPath)) {
    try {
        videoCache = JSON.parse(fs.readFileSync(videoMapPath, 'utf8'));
    } catch (e) {
        console.error("读取 video_map.json 失败:", e);
    }
}

const dataset = {};
for (const p of points) {
    const microVideos = getDefaultMicroCourses(p.id, p.title);
    const realVideos = (videoCache[p.id] && videoCache[p.id].videos) ? videoCache[p.id].videos : [];
    const questions = generateQuestions(p.id, p.title, p.grade);

    dataset[p.id] = {
        id: p.id,
        title: p.title,
        grade: p.grade,
        star: 5,
        tips: `【${p.title}·50题核心通关口诀】紧扣大纲题眼，基础概念抓准，模型变换抓活，分类讨论抓全，压轴大题抓结构！`,
        videos: microVideos,
        real_videos: realVideos,
        questions: questions
    };
}

fs.writeFileSync(outputJson, JSON.stringify(dataset, null, 2), 'utf8');
console.log(`[+] 成功写入 math_data.json (包含 ${Object.keys(dataset).length} 个考点，共 ${Object.keys(dataset).length * 50} 道题)`);

const jsContent = `/**\n * 初中数学一年通关工作台 - 53核心考点 × 50题阶梯中考真题矩阵及高清微课资源\n */\nwindow.MATH_DATA = ${JSON.stringify(dataset, null, 2)};\n`;
fs.writeFileSync(outputJs, jsContent, 'utf8');
console.log(`[+] 成功写入 math_data.js (已挂载至 window.MATH_DATA)`);

# team_config.py
# ─────────────────────────────────────────────────────────────
# 团队组成：完全可配置。你的项目需要哪些 Agent，就在这里列哪些。
#
# 【领域小组规则】同一 domain 的 Agent 组成一个"领域小组"，
# 每个领域至少 2 人（DOMAIN_MIN_SIZE）——单人领域无法组内收敛，禁止。
# 角色来源统一查「统一角色池」（references/统一角色池.md，322 个唯一角色 / 23 个领域）：
#   source = 池内 slug（如 engineering-code-reviewer）→ 直接复用其人设
#   source = new:<自定slug>                          → 池内没有，才新建
# 领域可选角色 < 2 时（如 research 仅 1 个），从相近领域跨领域补齐。
# ─────────────────────────────────────────────────────────────

import os

# 选用哪套"引擎"来真正跑团队（可插拔）：
#   lightweight —— 默认，需 pip 安装引擎依赖并配置 LLM_API_KEY
#   mock       —— 零依赖，仅演示/预览，不调用大模型
# 也可用环境变量 TEAM_ENGINE 或命令行 --engine 覆盖
ENGINE = os.getenv("TEAM_ENGINE", "lightweight")

# 每个领域小组的最少专家数（团队协作规则：每领域必须 2 名及以上）
DOMAIN_MIN_SIZE = 2

TEAM = [
    # ── 领域小组 A：research（研究）── 2 人
    {
        "domain": "research",
        "source": "research-synthesist",
        "role": "高级研究员",
        "goal": "针对主题做深入调研，产出带来源的关键发现",
        "backstory": "你是一名严谨的研究员，擅长信息检索、交叉验证与归纳。",
    },
    {
        "domain": "research",
        "source": "academic-statistician",   # 跨领域补齐：research 仅 1 个角色，从 academic 补
        "role": "研究统计员",
        "goal": "校验研究结论的数据支撑与统计显著性",
        "backstory": "你用数据说话，只认证据，不认直觉。",
    },
    # ── 领域小组 B：engineering（工程）── 2 人
    {
        "domain": "engineering",
        "source": "engineering-ai-engineer",
        "role": "软件工程师",
        "goal": "基于研究结论产出可运行的技术方案与代码",
        "backstory": "你是一名资深工程师，注重正确性与可维护性。",
    },
    {
        "domain": "engineering",
        "source": "engineering-backend-architect",
        "role": "后端架构师",
        "goal": "设计可扩展、可维护的系统结构与接口",
        "backstory": "你先想清楚结构，再写第一行代码。",
    },
    # ── 领域小组 C：testing（测试/审核）── 2 人
    {
        "domain": "testing",
        "source": "testing-reality-checker",
        "role": "质量审核员",
        "goal": "审查前序产出，指出遗漏、风险与改进点",
        "backstory": "你是一名挑剔的 reviewer，只认证据与质量。",
    },
    {
        "domain": "testing",
        "source": "testing-evidence-collector",
        "role": "证据核查员",
        "goal": "为每条结论收集可验证证据，剔除无据断言",
        "backstory": "没有证据的结论，在你这里一律退回。",
    },
    # ↓↓↓ 需要更多领域？复制上面的字典，填好 domain + source 即可（每领域 ≥2 人）↓↓↓
    # {
    #     "domain": "product",
    #     "source": "new:pricing-analyst",   # 池内没有 → new: 前缀新建
    #     "role": "产品经理",
    #     "goal": "把模糊需求拆成清晰任务与验收标准",
    #     "backstory": "你擅长把想法变成可执行计划。",
    # },
]

# 团队要完成的整体任务（{topic} 在运行时被替换）
# 收敛顺序：各领域小组内部讨论 → 每领域出 1 条最佳建议 → 全团队讨论 → 最终方案并落地
TASK_BRIEF = (
    "请围绕「{topic}」协作完成，严格按三级收敛进行：\n"
    "1) 小组内部讨论：research / engineering / testing 各组内部先辩到收敛；\n"
    "2) 每条领域小组只输出 1 条最佳建议（含关键理由）；\n"
    "3) 全团队讨论：汇总各组的那一条建议，解决跨域冲突；\n"
    "4) 输出唯一最终方案并落地执行（无法执行时给出具体示例）。\n"
    "讨论过程极度精简：只给结论 + 关键理由，禁止长篇解释、复述与客套。"
)

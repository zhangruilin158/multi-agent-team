#!/usr/bin/env python
# build_team.py
# ─────────────────────────────────────────────────────────────
# 多 Agent 团队 demo —— 团队组成完全可配置（见 team_config.py），不写死角色数。
# 引擎可插拔：具体用哪套引擎由 team_config.ENGINE / 环境变量 / --engine 决定，
# 主流程不依赖任何具体框架实现（见 engines/ 插件层）。
#
# 用法：
#   python build_team.py --dry-run                 # 只打印团队组成，不调用大模型（不依赖任何引擎）
#   python build_team.py --engine mock             # 零依赖演示运行（不调用大模型）
#   python build_team.py --topic "你的主题"          # 真实运行（默认 lightweight 引擎，需配置 .env 密钥）
# ─────────────────────────────────────────────────────────────
import argparse
import os
import sys

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

import team_config
from team_config import TEAM, TASK_BRIEF, ENGINE
from engines import get_engine, available_engines

# 每个领域小组的最少专家数（团队协作规则：每领域必须 2 名及以上）
DOMAIN_MIN_SIZE = getattr(team_config, "DOMAIN_MIN_SIZE", 2)


def group_by_domain(team):
    """按 domain 字段把团队分成领域小组。"""
    groups = {}
    for m in team:
        groups.setdefault(m.get("domain", "unassigned"), []).append(m)
    return groups


def check_domain_groups(team):
    """校验领域小组人数（每领域 >= DOMAIN_MIN_SIZE），返回 (分组, 展示行, 问题列表)。"""
    groups = group_by_domain(team)
    lines, problems = [], []
    for domain, members in groups.items():
        n = len(members)
        flag = "OK " if n >= DOMAIN_MIN_SIZE else "!! "
        lines.append("  %s%-14s %d 人：%s" % (flag, domain, n,
                                            "、".join(m["role"] for m in members)))
        if n < DOMAIN_MIN_SIZE:
            problems.append(
                "领域「%s」仅 %d 人（需 >= %d），单人无法组内收敛；"
                "请从相近领域补齐或增加该领域专家。" % (domain, n, DOMAIN_MIN_SIZE))
    return groups, lines, problems


def main():
    parser = argparse.ArgumentParser(description="可配置多 Agent 团队（引擎可插拔）")
    parser.add_argument("--topic", default="如何用多智能体提升团队协作效率")
    parser.add_argument("--engine", default=None,
                        help="指定引擎：%s（覆盖 team_config 的 ENGINE）" % "/".join(available_engines()))
    parser.add_argument("--dry-run", action="store_true",
                        help="只打印团队组成，不调用大模型")
    args = parser.parse_args()

    engine_name = args.engine or ENGINE
    engine = get_engine(engine_name)

    # 领域小组校验（团队协作规则：每个领域必须 2 名及以上专家）
    _, group_lines, problems = check_domain_groups(TEAM)
    print("领域小组（每领域需 >= %d 名专家）：" % DOMAIN_MIN_SIZE)
    for line in group_lines:
        print(line)
    for p in problems:
        print("  [!] " + p)
    print()

    # 预览模式：只走引擎的 plan()，不调用大模型、不依赖任何框架
    if args.dry_run:
        print(engine.plan(TEAM, TASK_BRIEF, args.topic))
        return

    # 无需密钥的纯演示引擎
    if engine_name == "mock":
        engine.run(TEAM, TASK_BRIEF, args.topic)
        return

    # 真实引擎需要密钥
    if not os.getenv("LLM_API_KEY"):
        print("\n[!] 未检测到 LLM_API_KEY。请复制 .env.example 为 .env 并填入密钥，"
              "或使用 --engine mock 预览团队。")
        sys.exit(2)

    engine.run(TEAM, TASK_BRIEF, args.topic)


if __name__ == "__main__":
    main()

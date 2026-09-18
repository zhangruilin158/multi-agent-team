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

from team_config import TEAM, TASK_BRIEF, ENGINE
from engines import get_engine, available_engines


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

# engines/mock_engine.py
# 零依赖引擎：不装任何大模型 SDK 也能跑。用于预览、教学演示或没有密钥时的占位运行。
from .base import BaseEngine


class MockEngine(BaseEngine):
    name = "mock"

    def plan(self, team, task_brief, topic):
        lines = [
            "=== 模拟多 Agent 团队（共 %d 个角色，按接力顺序）===" % len(team)
        ]
        for i, a in enumerate(team, 1):
            lines.append("  %d. %s  →  %s" % (i, a["role"], a["goal"]))
        lines.append("\n任务主题：%s" % topic)
        lines.append("\n[模拟] 未启用真实引擎，仅展示组队方案，不调用大模型、零费用。")
        return "\n".join(lines)

    def run(self, team, task_brief, topic):
        print(self.plan(team, task_brief, topic))
        print("\n=== 模拟运行：各角色依次产出（示例占位）===")
        for a in team:
            print("  · %s 完成：<示例产出>" % a["role"])
        print(
            "\n[提示] 这是无依赖的演示运行。要真实跑起来，请在 .env 配置 LLM_API_KEY"
            " 并改用 lightweight 引擎（默认）。"
        )
        return "<mock result>"

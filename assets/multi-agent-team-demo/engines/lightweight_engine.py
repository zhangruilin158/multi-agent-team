# engines/lightweight_engine.py
# 默认引擎适配器：封装"轻量多智能体引擎"（开源、角色化组队）。
# 注意：本文件是唯一直接引用具体框架实现的地方；主流程与配置都不依赖它。
from .base import BaseEngine


class LightweightEngine(BaseEngine):
    name = "lightweight"

    def plan(self, team, task_brief, topic):
        lines = [
            "=== 已配置的多 Agent 团队（共 %d 个角色，按接力顺序）===" % len(team)
        ]
        for i, a in enumerate(team, 1):
            lines.append("  %d. %s  →  %s" % (i, a["role"], a["goal"]))
        lines.append("\n任务主题：%s" % topic)
        lines.append("\n[plan] 未调用大模型。配置 .env 后执行真实运行。")
        return "\n".join(lines)

    def run(self, team, task_brief, topic):
        # 懒加载：只有真正要跑时才 import，避免没装依赖就报错
        from crewai import Agent, Task, Crew, Process, LLM
        import os

        llm_kwargs = {
            "model": os.getenv("LLM_MODEL"),
            "api_key": os.getenv("LLM_API_KEY"),
        }
        base_url = os.getenv("LLM_BASE_URL")
        if base_url:
            llm_kwargs["base_url"] = base_url
        llm = LLM(**llm_kwargs)

        agents = [
            Agent(
                role=a["role"],
                goal=a["goal"],
                backstory=a["backstory"],
                verbose=True,
                allow_delegation=False,
                llm=llm,
            )
            for a in team
        ]
        tasks = [
            Task(
                description=(
                    "整体任务：%s\n你是「%s」，你的目标是：%s。"
                    "请完成你负责的部分，并把成果清晰地交给后续角色。"
                    % (task_brief.format(topic=topic), a["role"], a["goal"])
                ),
                expected_output="你这一角色的结构化产出（发现 / 方案 / 评审意见等）。",
                agent=agent_obj,
            )
            for a, agent_obj in zip(team, agents)
        ]
        crew = Crew(agents=agents, tasks=tasks, process=Process.sequential, verbose=True)

        print("=== 已组建的多 Agent 团队（共 %d 个角色）===" % len(crew.agents))
        for i, a in enumerate(crew.agents, 1):
            print("  %d. %s  →  %s" % (i, a.role, a.goal))
        print("\n任务主题：%s\n" % topic)

        print("=== 团队开始工作 ===")
        result = crew.kickoff(inputs={"topic": topic})
        print("\n=== 团队产出 ===")
        print(result)
        return result

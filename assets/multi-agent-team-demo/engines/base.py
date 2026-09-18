# engines/base.py
# 统一引擎接口：所有"多 Agent 引擎"都必须实现这两个方法。
# 主流程只依赖此接口，不关心背后是哪个具体框架。
from abc import ABC, abstractmethod


class BaseEngine(ABC):
    #: 引擎标识，用于在配置/命令行里选择
    name = "base"

    @abstractmethod
    def plan(self, team, task_brief, topic):
        """只打印团队方案，不调用任何大模型（用于预览 / dry-run）。"""
        raise NotImplementedError

    @abstractmethod
    def run(self, team, task_brief, topic):
        """真正组建并运行多 Agent 团队，返回最终产出。"""
        raise NotImplementedError

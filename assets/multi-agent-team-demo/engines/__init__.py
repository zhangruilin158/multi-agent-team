# engines/__init__.py
# 多 Agent 引擎插件层：主流程只认统一接口，不绑定任何具体框架。
from .base import BaseEngine
from .factory import get_engine, available_engines

__all__ = ["BaseEngine", "get_engine", "available_engines"]

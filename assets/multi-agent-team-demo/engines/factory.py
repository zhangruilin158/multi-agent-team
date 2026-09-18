# engines/factory.py
# 引擎注册表 + 工厂：新增引擎只需在此登记一个适配器类。
from .base import BaseEngine
from .lightweight_engine import LightweightEngine
from .mock_engine import MockEngine

# 已注册的引擎；想接别的多智能体框架，写个新适配器类加进这行字典即可
_ENGINES = {
    "lightweight": LightweightEngine,
    "mock": MockEngine,
}


def get_engine(name):
    cls = _ENGINES.get(name)
    if cls is None:
        raise ValueError("未知引擎：%s（可选：%s）" % (name, ", ".join(_ENGINES)))
    return cls()


def available_engines():
    return list(_ENGINES.keys())

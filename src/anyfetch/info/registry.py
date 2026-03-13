from typing import ClassVar

from anyfetch.info.modules.base import InfoModule


class InfoRegistry:
    modules: ClassVar[dict[str, type[InfoModule]]] = {}

    @classmethod
    def register(cls, module) -> None:
        cls.modules[module.key] = module

    @classmethod
    def create(cls, key) -> InfoModule:
        return cls.modules[key]()

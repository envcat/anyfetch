from typing import ClassVar

from anyfetch.info.modules.base import InfoModule


class InfoRegistry:
    modules: ClassVar[dict[str, type[InfoModule]]] = {}

    @classmethod
    def register(cls, module) -> None:
        cls.modules[module.key] = module

    @classmethod
    def create(cls, key) -> InfoModule:
        try:
            return cls.modules[key]()
        except KeyError as e:
            raise KeyError(f"Unknown info module key: {key}") from e

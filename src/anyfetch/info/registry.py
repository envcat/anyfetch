from dataclasses import dataclass, field

from anyfetch.info.modules.base import InfoModule


@dataclass
class InfoRegistry:
    modules: dict[str, type[InfoModule]] = field(default_factory=dict)

    def register(self, module: type[InfoModule]) -> None:
        self.modules[module.key] = module

    def create(self, key: str) -> InfoModule:
        try:
            return self.modules[key]()
        except KeyError as e:
            raise KeyError(f"Unknown info module key: {key}") from e

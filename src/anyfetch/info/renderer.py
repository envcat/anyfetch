from dataclasses import dataclass

from anyfetch.color.colorizer import InfoColorizer
from anyfetch.config import InfoConfig
from anyfetch.info.modules.base import InfoModule


@dataclass
class InfoRenderer:
    modules: list[InfoModule]
    config: InfoConfig
    colorizer: InfoColorizer

    def render(self) -> list[str]:
        lines = []
        for module in self.modules:
            value = module.fetch()
            key = self.colorizer.color_key(module.key)
            sep = self.colorizer.color_separator(self.config.separator)
            lines.append(f"{key}{sep}{value}")
        return lines

from dataclasses import dataclass

from anyfetch.color.colorizer import InfoColorizer
from anyfetch.config import InfoConfig


@dataclass
class InfoRenderer:
    modules: dict
    cfg: InfoConfig
    colorizer: InfoColorizer

    def render(self) -> list:
        lines = []
        for module in self.modules:
            value = module.fetch()
            key = self.colorizer.color_key(module.key)
            sep = self.colorizer.color_separator(self.cfg.separator)
            lines.append(f"{key}{sep}{value}")
        return lines

from dataclasses import dataclass

from anyfetch.color.engine import ColorEngine
from anyfetch.config import InfoColorConfig, LogoColorConfig


@dataclass
class LogoColorizer:
    cfg: LogoColorConfig
    engine: ColorEngine

    def apply(self, line: str) -> str:
        for key, color in self.cfg.colors.items():
            token = f"${key.split('-')[1]}"  # $1 $2 $3
            if token in line:
                line = line.replace(token, self.engine.COLORS.get(color, ""))
        return line + self.engine.COLORS["reset"]


@dataclass
class InfoColorizer:
    cfg: InfoColorConfig
    engine: ColorEngine

    def color_key(self, key) -> str:
        return self.engine.color(key, self.cfg.keys)

    def color_separator(self, sep) -> str:
        return self.engine.color(sep, self.cfg.separator)

    def color_title(self, title) -> str:
        return self.engine.color(title, self.cfg.title)

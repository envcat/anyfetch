from anyfetch.color.engine import ANSIColorEngine
from anyfetch.config import InfoColorConfig, LogoColorConfig


class LogoColorizer:
    def __init__(self, cfg: LogoColorConfig, engine: ANSIColorEngine):
        self.cfg = cfg.colors
        self.engine = engine

    def apply(self, line: str) -> str:
        for key, color in self.cfg.items():
            token = f"${key.split('-')[1]}"  # $1 $2 $3
            if token in line:
                line = line.replace(token, self.engine.COLORS.get(color, ""))
        return line + self.engine.COLORS["reset"]


class InfoColorizer:
    def __init__(self, cfg: InfoColorConfig, engine: ANSIColorEngine):
        self.cfg = cfg
        self.engine = engine

    def color_key(self, key):
        return self.engine.color(key, self.cfg.keys)

    def color_separator(self, sep):
        return self.engine.color(sep, self.cfg.separator)

    def color_title(self, title):
        return self.engine.color(title, self.cfg.title)

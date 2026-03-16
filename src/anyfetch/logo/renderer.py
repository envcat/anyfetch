from dataclasses import dataclass

from anyfetch.color.colorizer import LogoColorizer
from anyfetch.logo.source.ascii_logo import AsciiLogo
from anyfetch.logo.source.base import LogoSourceStrategy


@dataclass
class LogoRenderer:
    strategy: LogoSourceStrategy
    colorizer: LogoColorizer

    def render(self) -> list[str]:
        raw = self.strategy.render()
        if isinstance(self.strategy, AsciiLogo):
            return [self.colorizer.apply(line) for line in raw]
        return raw

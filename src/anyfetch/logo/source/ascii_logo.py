from dataclasses import dataclass

from anyfetch.logo.source.base import LogoSourceStrategy


@dataclass
class AsciiLogo(LogoSourceStrategy):
    distro: str

    def render(self) -> list[str]:
        return ["$1   /\\", "$2  /  \\", "$3 /____\\", f"$1 {self.distro}"]

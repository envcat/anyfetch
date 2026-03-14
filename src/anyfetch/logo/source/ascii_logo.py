from dataclasses import dataclass

from anyfetch.logo.source.base import LogoSourceStrategy


@dataclass
class AsciiLogo(LogoSourceStrategy):
    distro: str

    def render(self) -> list[str]:
        return [
            "$1   .--.",
            "$1  |o_o |",
            "$2  |:_/ |",
            "$2 //   \\ \\",
            "$3(|     | )",
            "$3/'\\_   _/`\\",
            "$1\\___)=(___/",
            f"$1  {self.distro}",
        ]

from abc import ABC, abstractmethod
from typing import ClassVar


class ColorEngine(ABC):
    COLORS: ClassVar[dict[str, str]]

    @abstractmethod
    def color(self, text: str, color: str) -> str:
        pass


class ANSIColorEngine(ColorEngine):
    COLORS = {
        "red": "\033[31m",
        "green": "\033[32m",
        "blue": "\033[34m",
        "yellow": "\033[33m",
        "reset": "\033[0m",
    }

    def color(self, text: str, color: str) -> str:
        if color not in self.COLORS:
            return text
        return f"{self.COLORS[color]}{text}{self.COLORS['reset']}"

import re
from dataclasses import dataclass

from anyfetch.layout.base import LayoutStrategy

# Match ANSI escape sequences (e.g. \033[31m, \033[0m) so we can measure visible width.
_ANSI_ESCAPE_RE = re.compile(r"\033\[[0-9;]*m")


def _visible_width(s: str) -> int:
    return len(_ANSI_ESCAPE_RE.sub("", s))


@dataclass
class LeftLayout(LayoutStrategy):
    top: int = 0
    bottom: int = 0
    left: int = 5
    right: int = 0
    padding: int = 4

    def combine(self, logo, info) -> list[str]:
        max_lines = max(len(logo), len(info))
        max_logo_width = max(_visible_width(logo[i]) if i < len(logo) else 0 for i in range(max_lines))
        content = []
        for i in range(max_lines):
            left_part = logo[i] if i < len(logo) else ""
            right_part = info[i] if i < len(info) else ""
            gap = max_logo_width - _visible_width(left_part) + self.padding
            line = f"{left_part}{' ' * gap}{right_part}"
            line = " " * self.left + line + " " * self.right
            content.append(line)
        return [""] * self.top + content + [""] * self.bottom

from anyfetch.layout.base import LayoutStrategy


class LeftLayout(LayoutStrategy):
    def combine(self, logo, info) -> list:
        lines = []
        max_lines = max(len(logo), len(info))
        for i in range(max_lines):
            left = logo[i] if i < len(logo) else ""
            right = info[i] if i < len(info) else ""
            lines.append(f"{left:<25} {right}")
        return lines

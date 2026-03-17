from dataclasses import dataclass

from anyfetch.info.renderer import InfoRenderer
from anyfetch.layout.base import LayoutStrategy
from anyfetch.logo.renderer import LogoRenderer


@dataclass
class Renderer:
    logo_renderer: LogoRenderer
    info_renderer: InfoRenderer
    layout: LayoutStrategy

    def render(self) -> None:
        logo = self.logo_renderer.render()
        info = self.info_renderer.render()
        lines = self.layout.combine(logo, info)
        for line in lines:
            print(line)

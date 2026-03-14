from cyclopts import App

from anyfetch._constants import CONFIG_FILE_PATH
from anyfetch.color.colorizer import InfoColorizer, LogoColorizer
from anyfetch.color.engine import ANSIColorEngine
from anyfetch.config import Config, ImageLogoConfig, InfoColorConfig, InfoConfig, LogoColorConfig, LogoConfig
from anyfetch.info.modules.cpu import CPUInfo
from anyfetch.info.modules.disk import DiskInfo
from anyfetch.info.modules.kernal import KernalInfo
from anyfetch.info.modules.memory import MemoryInfo
from anyfetch.info.modules.os import OSInfo
from anyfetch.info.modules.shell import ShellInfo
from anyfetch.info.modules.title import TitleInfo
from anyfetch.info.modules.uptime import UptimeInfo
from anyfetch.info.registry import InfoRegistry
from anyfetch.info.renderer import InfoRenderer
from anyfetch.layout.left import LeftLayout
from anyfetch.logo.factory import LogoFactory
from anyfetch.logo.renderer import LogoRenderer
from anyfetch.renderer import Renderer

app = App(help="Anyfetch is a tool for fetching system information and displaying them in a pretty way.")


@app.default
def main():
    for module in [TitleInfo, CPUInfo, MemoryInfo, DiskInfo, UptimeInfo, ShellInfo, OSInfo, KernalInfo]:
        InfoRegistry.register(module)

    print(CONFIG_FILE_PATH)

    config = Config(
        logo=LogoConfig(
            source="ascii_auto",  # ascii_auto / image / none
            position="left",
            color=LogoColorConfig(colors={"color-1": "blue", "color-2": "green", "color-3": "red"}),
            image=ImageLogoConfig(path="/home/user/logo.png", protocol="kitty"),
        ),
        info=InfoConfig(
            separator=": ",
            order=["title", "OS", "Kernal", "CPU", "Memory", "Disk", "Shell", "Uptime"],
            color=InfoColorConfig(keys="blue", title="red", separator="blue"),
        ),
    )

    engine = ANSIColorEngine()

    logo_strategy = LogoFactory.create(config.logo)
    logo_colorizer = LogoColorizer(config.logo.color, engine)
    logo_renderer = LogoRenderer(logo_strategy, logo_colorizer)

    modules = [InfoRegistry.create(k) for k in config.info.order]
    info_colorizer = InfoColorizer(config.info.color, engine)
    info_renderer = InfoRenderer(modules, config.info, info_colorizer)

    layout = LeftLayout()
    renderer = Renderer(logo_renderer, info_renderer, layout)
    renderer.render()


if __name__ == "__main__":
    app()

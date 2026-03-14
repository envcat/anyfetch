from cyclopts import App

from anyfetch.color.colorizer import InfoColorizer, LogoColorizer
from anyfetch.color.engine import ANSIColorEngine
from anyfetch.config import Config, ImageLogoConfig, InfoColorConfig, InfoConfig, LogoColorConfig, LogoConfig
from anyfetch.info.modules import register_builtin_modules
from anyfetch.info.registry import InfoRegistry
from anyfetch.info.renderer import InfoRenderer
from anyfetch.layout.left import LeftLayout
from anyfetch.logo.factory import LogoFactory
from anyfetch.logo.renderer import LogoRenderer
from anyfetch.renderer import Renderer


def build_renderer(config: Config, registry: InfoRegistry) -> Renderer:
    engine = ANSIColorEngine()
    logo_strategy = LogoFactory.create(config.logo)
    logo_colorizer = LogoColorizer(config.logo.color, engine)
    logo_renderer = LogoRenderer(logo_strategy, logo_colorizer)

    info_modules = [registry.create(key) for key in config.info.order]
    info_colorizer = InfoColorizer(config.info.color, engine)
    info_renderer = InfoRenderer(info_modules, config.info, info_colorizer)

    layout = LeftLayout()
    return Renderer(logo_renderer, info_renderer, layout)


app = App(help="Anyfetch is a tool for fetching system information and displaying them in a pretty way.")


@app.default
def main():
    registry = InfoRegistry()
    register_builtin_modules(registry)

    config = Config(
        logo=LogoConfig(
            source="ascii_auto",  # ascii_auto / image / none
            position="left",
            color=LogoColorConfig(colors={"color-1": "blue", "color-2": "green", "color-3": "red"}),
            image=ImageLogoConfig(path="/home/user/logo.png", protocol="kitty"),
        ),
        info=InfoConfig(
            separator=": ",
            order=["User", "OS", "Kernel", "CPU", "Memory", "Disk", "Shell", "Uptime"],
            color=InfoColorConfig(keys="blue", title="red", separator="blue"),
        ),
    )

    renderer = build_renderer(config, registry)
    renderer.render()


if __name__ == "__main__":
    app()

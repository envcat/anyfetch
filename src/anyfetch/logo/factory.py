from anyfetch.config import LogoConfig
from anyfetch.logo.protocol.iterm import ItermProtocol
from anyfetch.logo.protocol.kitty import KittyProtocol
from anyfetch.logo.protocol.sixel import SixelProtocol
from anyfetch.logo.source.ascii_logo import AsciiLogo
from anyfetch.logo.source.base import LogoSourceStrategy
from anyfetch.logo.source.empty_logo import EmptyLogo
from anyfetch.logo.source.image_logo import ImageLogo


class LogoFactory:
    @staticmethod
    def create(config: LogoConfig) -> LogoSourceStrategy:
        if config.source.startswith("ascii"):
            distro = "DemoLinux" if config.source == "ascii_auto" else config.source.replace("ascii_", "")
            return AsciiLogo(distro)
        elif config.source == "image":
            if config.image is None:
                raise ValueError("Image logo source requires image configuration")
            if config.image.protocol == "kitty":
                proto = KittyProtocol()
            elif config.image.protocol == "sixel":
                proto = SixelProtocol()
            elif config.image.protocol == "iterm":
                proto = ItermProtocol()
            else:
                raise ValueError("Unknown protocol")
            return ImageLogo(config.image.path, proto)
        elif config.source == "none":
            return EmptyLogo()
        else:
            raise ValueError("Unknown logo source")

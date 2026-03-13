from anyfetch.config import LogoConfig
from anyfetch.logo.protocol.iterm import ItermProtocol
from anyfetch.logo.protocol.kitty import KittyProtocol
from anyfetch.logo.protocol.sixel import SixelProtocol
from anyfetch.logo.source.ascii_logo import AsciiLogo
from anyfetch.logo.source.empty_logo import EmptyLogo
from anyfetch.logo.source.image_logo import ImageLogo


class LogoFactory:
    @staticmethod
    def create(cfg: LogoConfig):
        if cfg.source.startswith("ascii"):
            distro = "DemoLinux" if cfg.source == "ascii_auto" else cfg.source.replace("ascii_", "")
            return AsciiLogo(distro)
        elif cfg.source == "image":
            if cfg.image is None:
                raise ValueError("Image logo source requires image configuration")
            if cfg.image.protocol == "kitty":
                proto = KittyProtocol()
            elif cfg.image.protocol == "sixel":
                proto = SixelProtocol()
            elif cfg.image.protocol == "iterm":
                proto = ItermProtocol()
            else:
                raise ValueError("Unknown protocol")
            return ImageLogo(cfg.image.path, proto)
        elif cfg.source == "none":
            return EmptyLogo()
        else:
            raise ValueError("Unknown logo source")

from dataclasses import dataclass


@dataclass
class LogoColorConfig:
    colors: dict[str, str]


@dataclass
class InfoColorConfig:
    keys: str
    title: str
    separator: str


@dataclass
class ImageLogoConfig:
    path: str
    protocol: str  # kitty, sixel, iterm


@dataclass
class LogoConfig:
    source: str  # ascii_auto, ascii_<distro>, image, none
    position: str  # left, right, top, bottom
    color: LogoColorConfig
    image: ImageLogoConfig | None = None


@dataclass
class InfoConfig:
    separator: str
    order: list[str]
    color: InfoColorConfig


@dataclass
class Config:
    logo: LogoConfig
    info: InfoConfig

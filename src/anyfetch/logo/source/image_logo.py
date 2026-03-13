from anyfetch.logo.protocol.base import LogoProtocolStrategy
from anyfetch.logo.source.base import LogoSourceStrategy


class ImageLogo(LogoSourceStrategy):
    def __init__(self, image_path: str, protocol: LogoProtocolStrategy):
        self.image_path = image_path
        self.protocol = protocol

    def render(self) -> list[str]:
        return self.protocol.render_image(self.image_path)

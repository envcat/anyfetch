from anyfetch.logo.protocol.base import LogoProtocolStrategy


class SixelProtocol(LogoProtocolStrategy):
    def render_image(self, image_path: str) -> list[str]:
        return [f"[Sixel render of {image_path}]"]

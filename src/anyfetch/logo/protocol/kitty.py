from anyfetch.logo.protocol.base import LogoProtocolStrategy


class KittyProtocol(LogoProtocolStrategy):
    def render_image(self, image_path: str) -> list[str]:
        return [f"[Kitty render of {image_path}]"]

from anyfetch.logo.protocol.base import LogoProtocolStrategy


class ItermProtocol(LogoProtocolStrategy):
    def render_image(self, image_path: str) -> list[str]:
        return [f"[iTerm render of {image_path}]"]

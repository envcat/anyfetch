from abc import ABC, abstractmethod


class LogoProtocolStrategy(ABC):
    @abstractmethod
    def render_image(self, image_path: str) -> list[str]:
        pass

from abc import ABC, abstractmethod


class LogoSourceStrategy(ABC):
    @abstractmethod
    def render(self) -> list[str]:
        pass

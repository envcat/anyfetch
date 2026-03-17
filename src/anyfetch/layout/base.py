from abc import ABC, abstractmethod


class LayoutStrategy(ABC):
    @abstractmethod
    def combine(self, logo, info) -> list[str]:
        pass

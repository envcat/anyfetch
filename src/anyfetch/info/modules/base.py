from abc import ABC, abstractmethod
from typing import ClassVar


class InfoModule(ABC):
    key: ClassVar[str]

    @abstractmethod
    def fetch(self) -> str:
        pass

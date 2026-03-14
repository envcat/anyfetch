import platform
from typing import ClassVar

from anyfetch.info.modules.base import InfoModule


class KernalInfo(InfoModule):
    key: ClassVar[str] = "Kernal"

    def fetch(self) -> str:
        return platform.release()

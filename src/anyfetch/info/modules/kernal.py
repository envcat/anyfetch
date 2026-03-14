import platform
from typing import ClassVar

from anyfetch.info.modules.base import InfoModule


class KernelInfo(InfoModule):
    key: ClassVar[str] = "Kernel"

    def fetch(self) -> str:
        return platform.release()

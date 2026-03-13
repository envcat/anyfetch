from typing import ClassVar

from anyfetch.info.modules.base import InfoModule


class MemoryInfo(InfoModule):
    key: ClassVar[str] = "memory"

    def fetch(self):
        return "8GB / 32GB"

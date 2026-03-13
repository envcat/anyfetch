from typing import ClassVar

import psutil

from anyfetch.info.modules.base import InfoModule


class MemoryInfo(InfoModule):
    key: ClassVar[str] = "Memory"

    def fetch(self):
        mem = psutil.virtual_memory()
        used = mem.used / (1024**3)
        total = mem.total / (1024**3)
        return f"{used:.2f} GiB / {total:.2f} GiB"

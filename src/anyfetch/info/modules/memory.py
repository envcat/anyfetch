from typing import ClassVar

import psutil

from anyfetch.info.modules.base import InfoModule


class MemoryInfo(InfoModule):
    key: ClassVar[str] = "Memory"

    def fetch(self):
        memory = psutil.virtual_memory()
        used = memory.used / (1024**3)
        total = memory.total / (1024**3)
        percent = memory.percent
        return f"{used:.2f} GiB / {total:.2f} GiB ({percent}%)"

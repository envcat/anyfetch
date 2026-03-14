from typing import ClassVar

import psutil

from anyfetch.info.modules.base import InfoModule


class DiskInfo(InfoModule):
    key: ClassVar[str] = "Disk"

    def fetch(self) -> str:
        disk = psutil.disk_usage("/")

        used = disk.used / (1024**3)
        total = disk.total / (1024**3)

        return f"{used:.2f} GiB / {total:.2f} GiB"

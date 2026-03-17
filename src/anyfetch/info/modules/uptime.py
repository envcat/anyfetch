import time
from typing import ClassVar

import psutil

from anyfetch.info.modules.base import InfoModule


class UptimeInfo(InfoModule):
    key: ClassVar[str] = "Uptime"

    def fetch(self) -> str:
        boot_timestamp = psutil.boot_time()
        uptime_seconds = max(0, int(time.time() - boot_timestamp))
        days = uptime_seconds // 86400
        hours = (uptime_seconds % 86400) // 3600
        minutes = (uptime_seconds % 3600) // 60

        parts = []

        if days:
            parts.append(f"{days}d")
        if hours:
            parts.append(f"{hours}h")

        parts.append(f"{minutes}m")

        return " ".join(parts)

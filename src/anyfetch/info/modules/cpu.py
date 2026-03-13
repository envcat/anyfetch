from typing import ClassVar

import cpuinfo

from anyfetch.info.modules.base import InfoModule


class CPUInfo(InfoModule):
    key: ClassVar[str] = "CPU"

    def fetch(self) -> str:
        info = cpuinfo.get_cpu_info()
        brand = info.get("brand_raw", "Unknown CPU")
        cores = info.get("count", "Unknown Cores")
        hz = info.get("hz_actual_friendly", "Unknown Speed")
        return f"{brand} ({cores}) {hz}"

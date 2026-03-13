from typing import ClassVar

from anyfetch.info.modules.base import InfoModule


class CPUInfo(InfoModule):
    key: ClassVar[str] = "cpu"

    def fetch(self) -> str:
        return "FakeCPU 16-Core"

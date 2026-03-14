import platform
from typing import ClassVar

import distro

from anyfetch.info.modules.base import InfoModule


class OSInfo(InfoModule):
    key: ClassVar[str] = "OS"

    def fetch(self):
        try:
            name = distro.name(pretty=True)
            if not name:
                name = platform.system()
        except Exception:
            name = platform.system()

        return name

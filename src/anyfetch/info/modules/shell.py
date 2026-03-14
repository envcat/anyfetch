import os
from typing import ClassVar

from anyfetch.info.modules.base import InfoModule


class ShellInfo(InfoModule):
    key: ClassVar[str] = "Shell"

    def fetch(self):
        return os.environ.get("SHELL") or os.environ.get("COMSPEC") or "Unknown"

from typing import ClassVar

from anyfetch.info.modules.base import InfoModule


class TitleInfo(InfoModule):
    key: ClassVar[str] = "title"

    def fetch(self):
        return "demo@machine"

import getpass
import socket
from typing import ClassVar

from anyfetch.info.modules.base import InfoModule


class UserInfo(InfoModule):
    key: ClassVar[str] = "User"

    def fetch(self):
        username = getpass.getuser()
        hostname = socket.gethostname()
        return f"{username}@{hostname}"

import platform
from typing import ClassVar

from anyfetch.info.modules.base import InfoModule


class KernelInfo(InfoModule):
    key: ClassVar[str] = "Kernel"

    def fetch(self) -> str:
        system = platform.system()
        release = platform.release()

        if system == "Windows":
            version = platform.version()
            try:
                import winreg
            except ImportError:
                return f"WIN32_NT {version}"

            try:
                reg_path = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion"
                with winreg.OpenKey(
                    winreg.HKEY_LOCAL_MACHINE, reg_path, 0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY
                ) as key:
                    ubr, _ = winreg.QueryValueEx(key, "UBR")
                    return f"WIN32_NT {version}.{ubr}"
            except OSError:
                return f"WIN32_NT {version}"

        return f"{system} {release}"

import platform
from typing import ClassVar

from anyfetch.info.modules.base import InfoModule


class KernelInfo(InfoModule):
    key: ClassVar[str] = "Kernel"

    def fetch(self) -> str:
        system = platform.system()
        release = platform.release()
        version = platform.version()

        if system == "Windows":
            try:
                import winreg

                reg_path = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion"
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path) as key:
                    ubr, _ = winreg.QueryValueEx(key, "UBR")
                    return f"WIN32_NT {version}.{ubr}"
            except (ImportError, OSError):
                return f"WIN32_NT {version}"
        elif system == "Darwin":
            return f"Darwin {release}"
        elif system == "Linux":
            return f"Linux {release}"
        elif "BSD" in system:
            return f"{system} {release}"

        return f"{system} {release}"

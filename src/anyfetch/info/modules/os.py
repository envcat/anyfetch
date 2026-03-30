import platform
from typing import ClassVar

import distro

from anyfetch.info.modules.base import InfoModule


class OSInfo(InfoModule):
    key: ClassVar[str] = "OS"

    def fetch(self) -> str:
        system = platform.system()

        if system == "Windows" or "MINGW" in system or "MSYS" in system:
            try:
                import winreg

                reg_path = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion"
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path) as key:
                    prod_name, _ = winreg.QueryValueEx(key, "ProductName")
                    display_ver, _ = winreg.QueryValueEx(key, "DisplayVersion")
                    arch = platform.machine()

                    return f"{prod_name} {display_ver} ({arch})"
            except Exception:
                return f"Windows {platform.release()} ({platform.machine()})"
        elif system == "Darwin":
            mac_ver = platform.mac_ver()[0]
            arch = platform.machine()
            return f"macOS {mac_ver} ({arch})"

        elif system == "Linux":
            if distro:
                name = distro.name(pretty=True)
                if name:
                    return f"{name} ({platform.machine()})"

            return f"Linux {platform.release()} ({platform.machine()})"

        elif "BSD" in system:
            return f"{system} {platform.release()} ({platform.machine()})"

        return f"{system} {platform.release()}"

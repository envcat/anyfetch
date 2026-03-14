from __future__ import annotations

from typing import TYPE_CHECKING

from anyfetch.info.modules.base import InfoModule
from anyfetch.info.modules.cpu import CPUInfo
from anyfetch.info.modules.disk import DiskInfo
from anyfetch.info.modules.kernal import KernelInfo
from anyfetch.info.modules.memory import MemoryInfo
from anyfetch.info.modules.os import OSInfo
from anyfetch.info.modules.shell import ShellInfo
from anyfetch.info.modules.uptime import UptimeInfo
from anyfetch.info.modules.user import UserInfo

BUILTIN_MODULES: list[type[InfoModule]] = [
    UserInfo,
    CPUInfo,
    MemoryInfo,
    DiskInfo,
    UptimeInfo,
    ShellInfo,
    OSInfo,
    KernelInfo,
]


if TYPE_CHECKING:
    from anyfetch.info.registry import InfoRegistry


def register_builtin_modules(registry: InfoRegistry) -> None:
    for module_cls in BUILTIN_MODULES:
        registry.register(module_cls)


__all__ = [
    "InfoModule",
    "BUILTIN_MODULES",
    "register_builtin_modules",
    "UserInfo",
    "CPUInfo",
    "MemoryInfo",
    "DiskInfo",
    "UptimeInfo",
    "ShellInfo",
    "OSInfo",
    "KernelInfo",
]

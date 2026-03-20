import os
import platform
import subprocess
from abc import ABC, abstractmethod
from collections.abc import Callable
from pathlib import Path
from typing import ClassVar

import shellingham

from anyfetch._constants import _INFO_NOT_FOUND
from anyfetch.info.modules.base import InfoModule

type ShellName = str
type ShellExec = str

_SHELL_NAME_ALIASES = {
    "bash": "bash",
    "zsh": "zsh",
    "fish": "fish",
    "sh": "sh",
    "dash": "sh",
    "ash": "sh",
    "cmd": "cmd",
    "powershell": "powershell",
    "pwsh": "powershell",
    "nu": "nushell",
    "nushell": "nushell",
    "xonsh": "xonsh",
    "elvish": "elvish",
}


def _normalize_shell_name(shell_name: str | None) -> ShellName | None:
    if not shell_name:
        return None

    return _SHELL_NAME_ALIASES.get(shell_name.lower())


type VersionCommandBuilder = Callable[[str], list[str]]


def _build_dashdash_version(executable: str) -> list[str]:
    return [executable, "--version"]


def _build_bash_version(executable: str) -> list[str]:
    return [executable, "-c", "echo $BASH_VERSION"]


def _build_zsh_version(executable: str) -> list[str]:
    return [executable, "-c", "echo $ZSH_VERSION"]


def _build_fish_version(executable: str) -> list[str]:
    return [executable, "-c", "echo $version"]


def _build_powershell_version(executable: str) -> list[str]:
    return [
        executable,
        "-NoLogo",
        "-Command",
        "$PSVersionTable.PSVersion.ToString()",
    ]


def _build_nushell_version(executable: str) -> list[str]:
    return [executable, "-c", "version | get version"]


def _build_xonsh_version(executable: str) -> list[str]:
    return [executable, "-c", "print($XONSH_VERSION)"]


_VERSION_COMMAND_BUILDERS: dict[ShellName, VersionCommandBuilder] = {
    "bash": _build_bash_version,
    "zsh": _build_zsh_version,
    "fish": _build_fish_version,
    "powershell": _build_powershell_version,
    "nushell": _build_nushell_version,
    "xonsh": _build_xonsh_version,
    "elvish": _build_dashdash_version,
    "sh": _build_dashdash_version,
}


class ShellDetectStrategy(ABC):
    @abstractmethod
    def detect_shell(self) -> tuple[ShellName | None, ShellExec | None]:
        pass


class ProcessStrategy(ShellDetectStrategy):
    def detect_shell(self) -> tuple[ShellName | None, ShellExec | None]:
        try:
            shell_name, shell_exec = shellingham.detect_shell()
            if shell_name and shell_exec:
                return _normalize_shell_name(shell_name), shell_exec
        except (RuntimeError, shellingham.ShellDetectionFailure):
            pass

        return None, None


class EnvStrategy(ShellDetectStrategy):
    def _normalize_shell_exec_to_name(self, path: str | Path) -> ShellName | None:
        if not str(path).strip():
            return None

        stem = Path(path).stem

        return _normalize_shell_name(stem)

    def detect_shell(self) -> tuple[ShellName | None, ShellExec | None]:
        """Attempt to detect the user's shell information from environment variables.

        This method is unreliable and should be used as a fallback only.
        """
        system = platform.system()

        if not system:
            return None, None

        shell_exec = None

        if system == "Windows":
            shell_exec = os.environ.get("COMSPEC")
        else:  # Unix
            shell_exec = os.environ.get("SHELL")

        if shell_exec:
            shell_name = self._normalize_shell_exec_to_name(shell_exec)
            return shell_name, shell_exec

        return None, None


class ShellInfo(InfoModule):
    key: ClassVar[str] = "Shell"
    _strategies: ClassVar[tuple[ShellDetectStrategy, ...]] = (
        ProcessStrategy(),
        EnvStrategy(),
    )

    def _detect_shell(self) -> tuple[ShellName | None, ShellExec | None]:
        for strategy in self._strategies:
            shell_name, shell_exec = strategy.detect_shell()
            if shell_name and shell_exec:
                return shell_name, shell_exec
        return None, None

    def _get_shell_version(self, shell_name: str, shell_exec: str | Path | None) -> str | None:
        # Prefer the explicit executable path, fall back to shell name.
        executable = shell_exec or shell_name

        if not executable:
            return None

        if shell_name == "cmd":  # cmd.exe version aligns with the Windows kernel version.
            return platform.version()

        command_builder = _VERSION_COMMAND_BUILDERS.get(shell_name)
        if not command_builder:
            return None
        command = command_builder(str(executable))

        try:
            completed = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=2,
            )
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError):
            return None

        output = (completed.stdout or completed.stderr or "").strip()
        if not output:
            return None

        first_line = output.splitlines()[0].strip()
        return first_line or None

    def fetch(self) -> str:
        shell_name, shell_exec = self._detect_shell()
        if not shell_name:
            return _INFO_NOT_FOUND
        if not shell_exec:
            return _INFO_NOT_FOUND

        version = self._get_shell_version(shell_name, shell_exec)
        if version:
            return f"{shell_name} {version}"

        return shell_name

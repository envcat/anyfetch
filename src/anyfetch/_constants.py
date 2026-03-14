from pathlib import Path

from platformdirs import PlatformDirs

platform_dir = PlatformDirs("anyfetch", "envcat")
CONFIG_FILE_PATH = Path(platform_dir.user_config_dir, "anyfetch.toml")

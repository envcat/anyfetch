from pathlib import Path

from platformdirs import PlatformDirs

dir = PlatformDirs("anyfetch", "envcat")
CONFIG_FILE_PATH = Path(dir.user_config_dir, "anyfetch.toml")

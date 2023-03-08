import sysconfig
from pathlib import Path


def get_lock_file_path(lock_file_dir: Path):
    return lock_file_dir / Path(
        f"Pipfile.{sysconfig.get_python_version()}.{sysconfig.get_platform()}.lock"
    )

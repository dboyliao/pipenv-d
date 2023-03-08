import os
from pathlib import Path

from pipenv.cli import cli as _pipenv_cli

from .utils import get_lock_file_path

LOCKFILE_DIR = Path(os.environ.get("PIPENVD_LOCKFILE_DIR", ".pipenv-d"))
if not LOCKFILE_DIR.exists():
    LOCKFILE_DIR.mkdir(parents=True)


def cli():
    lockfile_path = get_lock_file_path(LOCKFILE_DIR)
    active_lockfile = Path("Pipfile.lock")
    if lockfile_path.exists():
        with active_lockfile.open("w", encoding="utf8") as out_fid, lockfile_path.open(
            "r", encoding="utf8"
        ) as in_fid:
            out_fid.write(in_fid.read())
    _pipenv_cli()
    if active_lockfile.exists():
        with lockfile_path.open("w", encoding="utf8") as out_fid, active_lockfile.open(
            "r", encoding="utf8"
        ) as in_fid:
            out_fid.write(in_fid.read())
        active_lockfile.unlink()

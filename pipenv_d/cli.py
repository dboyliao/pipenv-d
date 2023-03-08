import os
import subprocess
import sys
from pathlib import Path

from .utils import get_lock_file_path

LOCKFILE_DIR = Path(os.environ.get("PIPENVD_LOCKFILE_DIR", ".pipenv-d"))
if not LOCKFILE_DIR.exists():
    LOCKFILE_DIR.mkdir(parents=True)


def _run_pipenv():
    pipenv_cmd = [sys.executable, "-m", "pipenv"] + sys.argv[1:]
    return subprocess.call(pipenv_cmd)


def cli():
    lockfile_path = get_lock_file_path(LOCKFILE_DIR)
    active_lockfile = Path("Pipfile.lock")
    if lockfile_path.exists():
        with active_lockfile.open("w", encoding="utf8") as out_fid, lockfile_path.open(
            "r", encoding="utf8"
        ) as in_fid:
            out_fid.write(in_fid.read())
    ret_code = _run_pipenv()
    if active_lockfile.exists():
        with lockfile_path.open("w", encoding="utf8") as out_fid, active_lockfile.open(
            "r", encoding="utf8"
        ) as in_fid:
            out_fid.write(in_fid.read())
        active_lockfile.unlink()
    return ret_code

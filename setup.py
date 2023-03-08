from pathlib import Path

from setuptools import find_packages, setup


def _get_version():
    version_file_path = Path(__file__).parent / "pipenv_d" / "_version.py"
    if not version_file_path.exists():
        print(f"WARN: no {version_file_path} found, using 0.0.0 as __version__")
        return "0.0.0"
    ns = {}
    with version_file_path.open("r") as fid:
        exec(fid.read(), {}, ns)
    return ns["__version__"]


with open("./README.md", "r") as fid:
    LONG_DESCRIPTION = fid.read()

setup(
    name="pipenv-d",
    version=_get_version(),
    description="dirty hack of pipenv",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages("."),
    install_requires=["pipenv"],
    author="dboyliao",
    url="https://github.com/dboyliao/pipenv-d",
    entry_points={"console_scripts": ["pipenv-d=pipenv_d.cli:cli"]},
)

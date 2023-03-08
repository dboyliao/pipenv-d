from setuptools import find_packages, setup

setup(
    name="pipenv-d",
    version="0.0.1",
    packages=find_packages("."),
    install_requires=["pipenv"],
    author="dboyliao",
    url="https://github.com/dboyliao/pipenv-d",
    entry_points={"console_scripts": ["pipenv-d=pipenv_d.cli:cli"]},
)

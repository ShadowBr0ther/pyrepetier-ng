# -*- coding: utf-8 -*-

from pyrepetier import __version__
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'pyrepetier-ng',
    version = __version__,
    description = 'New Repetier-Server API library based on Morten Trabs version',
    author = 'Lukas Büttner',
    author_email = 'l.buettner@repetier.com',
    license= 'MIT',
    url = 'https://github.com/ShadowBr0ther/pyrepetier-ng',
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6"
)

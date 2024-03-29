import pathlib

from setuptools import setup , find_packages

HERE = pathlib.Path(__file__).parent

VERSION = "1.1.0"
PACKAGE_NAME = "hanoi_python_solver"
AUTHOR = "ESHome33"
AUTHOR_EMAIL = "eshome.fr@gmail.com"
URL = "https://github.com/esHome33/hanoi_python_solver/"

LICENSE = 'MIT'
DESCRIPTION = 'implementation of Tower of Hanoi game + shortest path to resolution at each step'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"


INSTALL_REQUIRES = []


setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages(include=["hanoi_python_solver"], exclude=["perso"]),
      )

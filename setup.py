import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = "1.0.0"
PACKAGE_NAME = "language-statistics"
AUTHOR = "Simon Ilincev"
AUTHOR_EMAIL = "simon@simonilincev.com"
URL = "https://github.com/Destaq/language-statistics"

LICENSE = "MIT License"
DESCRIPTION = "Generates a colored image showing programming language distribution in your directory."
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = ["PyYAML", "pycairo"]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    license=LICENSE,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(),
    entry_points={
        "console_scripts": ["statistics = language_statistics.statistics:main"]
    },
    include_package_data=True,
    zip_safe=False,
)


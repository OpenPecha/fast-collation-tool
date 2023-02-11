import re
from pathlib import Path

from setuptools import find_packages, setup


def read(fname):
    p = Path(__file__).parent / fname
    with p.open(encoding="utf-8") as f:
        return f.read()


def get_version(prop, project):
    project = Path(__file__).parent / project / "__init__.py"
    result = re.search(
        r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(prop), project.read_text()
    )
    return result.group(1)


setup(
    name="fast-collation-tools",
    version=get_version("__version__", "fast_collation_tools"),
    author="OpenPecha Developers",
    author_email="roux.elie@gmail.com",
    description="Fast tools for text collation",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    license="Apache2",
    url="https://github.com/OpenPecha/fast-collation-tools",
    packages=find_packages(),
    install_requires=[
        "regex",
        "openpecha",
        "fast-diff-match-patch"
    ],
    python_requires=">=3.7"
)

from setuptools import setup, find_packages
from codecs import open
import os


here = os.path.abspath(os.path.dirname(__file__))

os.chdir(here)

with open(
    os.path.join(here, "LONG_DESCRIPTION.rst"), "r", encoding="utf-8"
) as fp:
    long_description = fp.read()

setup(
    name = 'prembly',
    # version=
    packages = find_packages(exclude=["tests", "tests.*"]), 
    description="Python bindings for the Prembly IdentityPass API",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author="Olanrewaju Kabiru",
    author_email="programmerolakay@gmail.com",
    url="https://github.com/olakayCoder1/pyprembly-sdk",
    python_requires='>=3.x',
    install_requires=[
        "requests","python-dotenv", "urllib3",
    ],
)
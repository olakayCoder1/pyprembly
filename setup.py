from setuptools import setup, find_packages
from codecs import open
import os


here = os.path.abspath(os.path.dirname(__file__))

os.chdir(here)


# Get the long description from the README file
with open(os.path.join(here, 'LONG_DESCRIPTION.md'), encoding='utf-8') as f:
    long_description = f.read()



setup(
    name = 'pyprembly',
    version='0.0.2',
    packages = find_packages(exclude=["tests", "tests.*"]), 
    description="Python bindings for the Prembly IdentityPass API",
    long_description=long_description,
    long_description_content_type='text/markdown',
    zip_safe = False,
    keywords='api, client, prembly',
    author="Olanrewaju Kabiru",
    author_email="programmerolakay@gmail.com",
    url="https://github.com/olakayCoder1/pyprembly",
    python_requires='>=3.x',
    install_requires=[
        "requests","python-dotenv", "urllib3",
    ],
    license='MIT',
    package_data={'README': ['README.md']},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: Web Environment",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',   
    ]
)
from setuptools import setup, find_packages

# Package meta-data.
NAME = 'freequest'
DESCRIPTION = 'FreeQuest is an open source fantasy adventure board game inspired by games like Heroquest, Warhammer Quest, and Descent.'
URL = 'https://github.com/me/myproject'
EMAIL = 'levi@levimccormick.com'
AUTHOR = 'Levi McCormick'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = "0.1.0"

REQUIRED = []

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    install_requires=REQUIRED,
    license='Creative Commons Attribution Share Alike 4.0',
    entry_points={
        'console_scripts': ['freequest=freequest.cli:main'],
    },
)

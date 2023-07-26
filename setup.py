#!/usr/bin/env python

from setuptools import find_packages, setup

# Package meta-data.
NAME = 'ci-demon'
DESCRIPTION = 'ci demon'
LONG_DESCRIPTION = 'ci demon http service which is expose simple rest api to manipulate your development'
URL = 'https://github.com/kuza2010'
EMAIL = 'kyza20106@yandex.ru'
AUTHOR = 'Danilin Artyom'
REQUIRES_PYTHON = '>=3.10.0'
VERSION = '0.1.1'

REQUIRED = [
    'flask==2.3.2',
    'dependency-injector==4.40.0',
    'psutil==5.9.5',
]

EXTRAS = {
}

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(include=['src', 'src.*']),
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    package_data={'src': ['service/runners/transliterate_bot/transliterate_bot.sh']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['ci-demon=src.demon:main']
    },
)

from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.2.1'
DESCRIPTION = 'Censor words and phrases with censorpy.'
LONG_DESCRIPTION = 'Censor a range of words and phrases with ease, stop people from bypassing censors and more.'

setup (
    name="censorpy",
    version=VERSION,
    author="NotKatsu",
    author_email="katsudiscord@outlook.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["unidecode"],
    setup_requires=['wheel'],
    keywords=['python', 'censor', 'censorpy', 'words', 'censoring', 'block'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
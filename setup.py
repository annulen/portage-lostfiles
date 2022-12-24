from os import path

from setuptools import setup


def read(filename: str) -> str:
    """Helper to read README."""
    this_directory = path.abspath(path.dirname(__file__))
    with open(path.join(this_directory, filename), encoding="utf-8") as f:
        return f.read()


setup(
    name="lostfiles",
    version="0.5",
    author="Michael Egger",
    author_email="egger.m@protonmail.com",
    description="A simple script to identify files not tracked by Portage package manager.",
    url="https://github.com/gcarq/portage-lostfiles",
    license="GPL-2.0",
    keywords="gentoo portage maintenance",
    py_modules=["lostfiles"],
    zip_safe=False,
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
    install_requires=['portage>=3,<4'],
    classifiers=[
        "Topic :: Utilities",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    entry_points={"console_scripts": ["lostfiles=lostfiles:main"]},
)

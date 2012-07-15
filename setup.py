from os import path
from setuptools import setup, find_packages

from hip_pocket.constants import VERSION


def load(file_name):
    here = path.dirname(path.abspath(__file__))
    try:
        with open(path.join(here, file_name), "r") as fp:
            return fp.read()
    except IOError:
        return u""

setup(
    name="HipPocket",
    description="A wrapper around Flask to ease the development of larger applications",
    long_description=load("README.rst"),
    version=VERSION,
    packages=find_packages(),
    url="https://github.com/svieira/HipPocket",
    author="Sean Vieira",
    author_email="vieira.sean+hip_pocket@gmail.com",
    install_requires=[
        "Flask>=0.7",
        "Jinja2>=2.4",
        "Werkzeug>=0.7"
    ],
    platforms="any",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    include_package_data=True,
    test_suite="hip_pocket.tests.suite",
    zip_safe=False
    )

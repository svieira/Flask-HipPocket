from os import path
from setuptools import setup, find_packages


def load(file_name):
    here = path.dirname(path.abspath(__file__))
    try:
        with open(path.join(here, file_name), "r") as fp:
            return fp.read()
    except IOError:
        return u""

setup(
    name="Flask-HipPocket",
    description="A wrapper around Flask to ease the development of larger applications",
    long_description=load("README.rst"),
    version="0.2.0b1",
    packages=find_packages(),
    url="https://github.com/svieira/Flask-HipPocket",
    author="Sean Vieira",
    author_email="vieira.sean+hip_pocket@gmail.com",
    install_requires=[
        "Flask>=0.7",
        "Jinja2>=2.4",
        "Werkzeug>=0.7"
    ],
    platforms="any",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    include_package_data=True,
    test_suite="flask_hippocket.tests.suite",
    zip_safe=False
)

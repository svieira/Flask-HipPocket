from setuptools import setup

from hip_pocket.constants import VERSION

setup(
    name="HipPocket",
    description="A wrapper around Flask to ease the development of larger applications",
    version=VERSION,
    packages=["hip_pocket"],
    url="https://github.com/svieira/HipPocket",
    author="Sean Vieira",
    author_email="vieira.sean+hip_pocket@gmail.com",
    install_requires=[
        "Flask>=.7",
        "Jinja2>=2.4",
        "Werkzeug>=.7"
    ],
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
    zip_safe=False
    )

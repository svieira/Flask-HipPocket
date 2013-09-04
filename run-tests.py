#!/usr/bin/env python

if __name__ == "__main__":
    from os.path import abspath, dirname
    from sys import path
    path.insert(0, abspath(dirname(__file__)))

    from flask_hippocket.tests import main

    main()

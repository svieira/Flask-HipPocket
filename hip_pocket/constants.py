__all__ = ["__version__", "VERSION"]
__version__ = (0, 1, 2, "a")

maj, min, patch = [unicode(v) for v in __version__[:3]]
ver = u"{maj}.{min}.{patch}".format(maj=maj, min=min, patch=patch)
addenda = u".".join([unicode(v) for v in __version__[3:]])

#: HipPocket complies with http://www.python.org/dev/peps/pep-0386/
VERSION = u"{ver}{addenda}".format(ver=ver, addenda=addenda)

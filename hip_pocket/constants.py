__all__ = ["__version__", "VERSION"]
__version__ = (0, 1, 1, "alpha")

maj, min, patch = [unicode(v) for v in __version__[:3]]
ver = u"{maj}.{min}.{patch}".format(maj=maj, min=min, patch=patch)
addenda = u".".join([unicode(v) for v in __version__[3:]])

#: HipPocket complies with http://semver.org/ v2.0.0-rc.1
VERSION = u"{ver}-{addenda}".format(ver=ver, addenda=addenda).strip(u"-")

"""
**Unit** tests for Hip Pocket.
"""

import os
import sys
import unittest
from werkzeug.utils import import_string, find_modules

# The following are taken from Flask's unit test suite with much thanks to Armin
# https://github.com/mitsuhiko/flask/blob/master/flask/testsuite/__init__.py


def add_to_path(path):
    """Adds an entry to sys.path if it's not already there.  This does
    not append it but moves it to the front so that we can be sure it
    is loaded.
    """
    if not os.path.isdir(path):
        raise RuntimeError('Tried to add nonexisting path')

    def _samefile(x, y):
        try:
            return os.path.samefile(x, y)
        except (IOError, OSError):
            return False
    sys.path[:] = [x for x in sys.path if not _samefile(path, x)]
    sys.path.insert(0, path)


def iter_suites():
    """Yields all testsuites."""
    for module in find_modules(__name__):
        mod = import_string(module)
        if hasattr(mod, 'suite'):
            yield mod.suite()


def find_all_tests(suite):
    """Yields all the tests and their names from a given suite."""
    suites = [suite]
    while suites:
        s = suites.pop()
        try:
            suites.extend(s)
        except TypeError:
            yield s, '%s.%s.%s' % (
                s.__class__.__module__,
                s.__class__.__name__,
                s._testMethodName
            )


class BetterLoader(unittest.TestLoader):
    """A nicer loader that solves two problems.  First of all we are setting
    up tests from different sources and we're doing this programmatically
    which breaks the default loading logic so this is required anyways.
    Secondly this loader has a nicer interpolation for test names than the
    default one so you can just do ``run-tests.py ViewTestCase`` and it
    will work.
    """

    def getRootSuite(self):
        return suite()

    def loadTestsFromName(self, name, module=None):
        root = self.getRootSuite()
        if name == 'suite':
            return root

        all_tests = []
        for testcase, testname in find_all_tests(root):
            if testname == name or \
               testname.endswith('.' + name) or \
               ('.' + name + '.') in testname or \
               testname.startswith(name + '.'):
                all_tests.append(testcase)

        if not all_tests:
            raise LookupError('could not find test case for "%s"' % name)

        if len(all_tests) == 1:
            return all_tests[0]
        rv = unittest.TestSuite()
        for test in all_tests:
            rv.addTest(test)
        return rv


def setup_path():
    add_to_path(os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'test_apps')))


def suite():
    """A testsuite that has all the HipPocket tests.  You can use this
    function to integrate the HipPocket tests into your own testsuite
    in case you want to test that monkeypatches to HipPocket do not
    break it.
    """
    setup_path()
    suite = unittest.TestSuite()
    for other_suite in iter_suites():
        suite.addTest(other_suite)
    return suite


def main():
    """Runs the testsuite as command line application."""
    try:
        unittest.main(testLoader=BetterLoader(), defaultTest='suite')
    except Exception, e:
        print 'Error: %s' % e


if __name__ == "__main__":
    unittest.main(testLoader=BetterLoader(), defaultTest='suite')

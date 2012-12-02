~~~~~~~~~
HipPocket
~~~~~~~~~

    Circular imports have you down? Looking for a better way to build mid-to-large scale systems? You might need to pop that flask into your hip pocket and take a brisk walk to clear your head.

What is it?
-----------

HipPocket is a collection of convenience wrappers for the already intensely useful Flask_ web framework.

At its core are two classes:

``Mapper``
    Enable centralized URL mapping based on ``LazyLoader`` from `Flask's documentation`_

``HipPocket``
    A wrapper to enable running setup tasks on a Flask application at startup.

``HipPocket`` itself also comes with two pre-defined tasks:

``autoload``
    Load blueprints from a package and auto-register them with Flask
    To add a new blueprint to an autoloading application simply drop in a sub-package and reload your server.

``setup_errors``
    Add basic error responses for all HTTP error codes.

Can I use it?
-------------

It depends on your requirements. Some things to consider:

* HipPocket is licenced under the MIT licence so it's free to use for almost any purpose.
* It is currently alpha software.
* It has limited tests (currently).
* It has no documentation (aside from its docstrings).
* Its API is not stable.
* It is actively accepting `patches`_ and `feedback`_ at its `GitHub repository`_.


.. _Flask: http://flask.pocoo.org
.. _Flask's documentation: http://flask.pocoo.org/docs/patterns/lazyloading/
.. _GitHub repository: https://github.com/svieira/HipPocket
.. _patches: https://github.com/svieira/HipPocket/pulls
.. _feedback: https://github.com/svieira/HipPocket/issues
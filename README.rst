~~~~~~~~~
HipPocket
~~~~~~~~~

    Tired of circular imports? Startup times making you feel like you're working in Java?
    You might need to pop that flask into your hip pocket and take a brisk walk to clear your head.

What is it?
-----------

HipPocket is a collection of convenience wrappers for the already intensely useful Flask_ web framework.

It provides:

``Mapper``
    Enable centralized URL mapping

``LateLoader``
    Taken from `Flask's documentation`_

and of course ``HipPocket``
    A wrapper to enable running setup tasks on a Flask application at startup.

``HipPocket`` itself also comes with two pre-defined tasks:

``autoload``
    Load blueprints from a package and auto-register them with Flask
    To add a new blueprint to an autoloading application simply drop in a sub-package and reload your server
    (remember, since you are use ``Mapper`` your startup times should be significantly decreased.)

``setup_errors``
    Add basic error responses for all HTTP error codes.

Can I use it?
-------------

It depends on your requirements. Some things to consider:

* HipPocket is licenced under the MIT licence so it's free to use for almost any purpose.
* It is currently pre-alpha software.
* It has no tests (yet).
* It has no documentation (aside from its docstrings).
* Its API is not stable.
* It is actively accepting patches and feedback.


.. _Flask: http://flask.pocoo.org
.. _Flask's documentation: http://flask.pocoo.org/docs/patterns/lazyloading/
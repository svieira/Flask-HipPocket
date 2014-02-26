~~~~~~~~~~~~~~~
Flask-HipPocket
~~~~~~~~~~~~~~~

.. image:: https://drone.io/github.com/svieira/HipPocket/status.png
        :alt: Build Status (via Drone.io)
        :target: https://drone.io/github.com/svieira/HipPocket/latest
        
.. image:: https://travis-ci.org/svieira/Flask-HipPocket.png?branch=master
        :target: https://travis-ci.org/svieira/Flask-HipPocket
        :alt: Build Status (via Travis-CI)
        
.. image:: https://requires.io/github/svieira/Flask-HipPocket/requirements.png?branch=master
        :target: https://requires.io/github/svieira/Flask-HipPocket/requirements/?branch=master
        :alt: Requirements Status
        
----

.. epigraph::
    Circular imports have you down? Looking for a better way to build mid-to-large scale systems? Pop that flask into your hip pocket and take a brisk walk to clear your head.


What is it?
-----------

Flask-HipPocket is a collection of convenience wrappers for the already intensely useful Flask_ web framework.

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

* It is currently late-alpha software.
* It is licenced under the MIT licence. 
* It does not yet have full test coverage.
* It has limited `documentation`_.

Contributing
------------

Flask-HipPocket is actively accepting `patches`_ and `feedback`_ at its `GitHub repository`_.

Links
-----

* `repository`_
* `documentation`_
* `development version`_

.. _Flask: http://flask.pocoo.org
.. _Flask's documentation: http://flask.pocoo.org/docs/patterns/lazyloading/
.. _repository: https://github.com/svieira/Flask-HipPocket
.. _GitHub repository: repository_
.. _patches: https://github.com/svieira/Flask-HipPocket/pulls
.. _feedback: https://github.com/svieira/Flask-HipPocket/issues
.. _documentation: http://flask-hippocket.readthedocs.org/en/latest/
.. _development version: http://github.com/svieira/Flask-HipPocket/zipball/master#egg=Flask-HipPocket-dev

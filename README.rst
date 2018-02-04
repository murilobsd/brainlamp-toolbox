Drain Lamp Toolbox
===================

.. image:: https://badge.fury.io/py/brainlamp-toolbox.svg
   :target: https://badge.fury.io/py/brainlamp-toolbox
   :alt: Pypi package

.. image:: https://travis-ci.org/brainlamp/brainlamp-toolbox.svg?branch=master
   :target: https://travis-ci.org/brainlamp/brainlamp-toolbox
   :alt: Travis CI build status (Linux)

.. image:: https://coveralls.io/repos/github/brainlamp/brainlamp-toolbox/badge.svg?branch=master
   :target: https://coveralls.io/github/brainlamp/brainlamp-toolbox?branch=master
   :alt: Coveralls

.. image:: https://landscape.io/github/brainlamp/brainlamp-toolbox/master/landscape.svg?style=flat
   :target: https://landscape.io/github/brainlamp/brainlamp-toolbox/master
   :alt: Code Health


brainlamp_toolbox is compatible with Python 3+

Install
-------

It's available on PyPI_, so you can install it using ``pip`` (or
``easy_install``):

.. code-block:: console

   $ pip install brainlamp-toolbox

.. note::

   brainlamp-toolbox requires some packages ``nltk``

.. _PyPI: https://pypi.python.org/pypi/brainlamp-toolbox
.. _README: https://github.com/brainlamp/brainlamp-toolbox#readme


.. _example:

Example
-------

.. code-block:: pycon

   >>> import brainlamp_toolbox
   >>> with open('some_essay.txt') as f:
           essay_txt = f.read()
   >>> essay = Essay('title', essay_txt)
   >>> print("Number of words: %d" % essay.words_count)
       Number of words: 193

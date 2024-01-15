.. Pysphalt documentation master file, created by
   sphinx-quickstart on Thu Nov 30 11:03:07 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Pysphalt's documentation!
===========================================

Pysphalt is a library of machine learning models for Brazilian asphalt material data.

Installation
------------

Install the ``pysphalt`` package (or add it to your ``requirements.txt`` file):

.. code:: console

    $ pip install sphinx_rtd_theme


Usage
-----

Import one of the models from the ``pysphalt.models`` module, for example the :class:`.AsphaltModulusPredictor` model:

.. code:: python

   from pysphalt.models import AsphaltModulusPredictor

   predictor = AsphaltModulusPredictor()

   predictor.predict([[<your sample row 1>], [<your sample row 2>], ...])


.. toctree::
   :maxdepth: 2
   :caption: Python API:

   api/models

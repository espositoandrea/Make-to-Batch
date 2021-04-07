.. Make to Batch documentation master file, created by
   sphinx-quickstart on Mon Oct  5 16:38:43 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Make to Batch
=============

Welcome to the documentation of Make to Batch.

This is a simple tool to convert a GNU Makefile into a Windows Batch file.

.. toctree::
   :glob:
   :maxdepth: 2
   :caption: Code Documentation

   code/*

Usage
-----

Install the tool by using `PyPI <https://pypi.org/project/make-to-batch/>`_ using
the following command:
::

   pip install make-to-batch

You can also install by downloading the source code:
::

   cd path/to/source/
   python setup.py install

The tool provides only a command, ``make-to-batch``, that converts a Makefile in
the current directory to a batch file in the same directory. The tool behaviour
can be customized using some options: here is the help of the tool.
::

   $ make-to-batch -h
   usage: make-to-batch [-h] [-v] [-i INPUT] [-o OUTPUT]

   Convert a Makefile to a Batch (Windows) file.

   optional arguments:
     -h, --help            show this help message and exit
     -v, --version         show program's version number and exit
     -i INPUT, --input INPUT
                           set the makefile to be converted. Defaults to
                           './Makefile'
     -o OUTPUT, --output OUTPUT
                           set the name of the output batch file. Defaults to
                           './make.bat'

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

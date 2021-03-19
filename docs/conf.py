# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath('../'))

import make_to_batch.look_up_table as lut

# -- Project information -----------------------------------------------------

project = 'Make to Batch'
copyright = '2020, Andrea Esposito'
author = 'Andrea Esposito'

# The full version, including alpha/beta/rc tags
release = '0.2.3'

# -- General configuration ---------------------------------------------------

master_doc = 'index'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinx_rtd_theme'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# Adding the table of commands to the look up table docs.
table_row = '''
| {:16s} |  {:18s} |
+------------------+---------------------+
'''.strip()
lut.__doc__ += '''
Available Commands
------------------
+------------------+---------------------+
|   Unix Command   |   Windows Command   |
+==================+=====================+
''' + \
    "\n".join(table_row.format("``"+k+"``", "``"+v['command']+"``")
              for k, v in lut.linux_to_dos.items())

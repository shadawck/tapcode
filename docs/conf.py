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
import sphinx_rtd_theme
sys.path.append(os.path.join(os.path.dirname(__name__), ".."))


# -- Project information -----------------------------------------------------

project = "Tapcode"
copyright = "Copyright 2020, The TapCode Project"
author = "HUGUET Rémi"
credits = ["shadawck", "Itsnexn"]
license = "MIT"

# The full version, including alpha/beta/rc tags
release = "1.1.0"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named "sphinx.ext.*") or your custom
# ones.
extensions = ["sphinx.ext.autodoc","sphinx.ext.coverage","sphinx.ext.napoleon", "sphinx_rtd_theme"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]
html_theme_path = ["_themes", ]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Specify the main page
master_doc = "index"


# -- Options for HTML output -------------------------------------------------

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = [
    "css/custom.css",
]

# Pygment style color highlihting for code-block
pygments_style = "sphinx"

# HTML Theme for html page and configurations options
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "canonical_url": "",
    "logo_only": False,
    "display_version": True,
    "prev_next_buttons_location": "bottom",
    "style_external_links": True,
    # Toc options
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False
}
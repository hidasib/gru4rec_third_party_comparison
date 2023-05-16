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
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
# -- Project information -----------------------------------------------------

project = 'GRU4Rec Third Party Experiments'
copyright = ''
author = 'Balázs Hidasi & Ádám Czapp'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['recommonmark', 'sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'sphinx_design']

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
url_branch = "master"
html_theme = "sphinx_book_theme" #'sphinx_rtd_theme'
html_theme_options = {
    "repository_provider": "github",  # or "gitlab", "bitbucket"
    "repository_url": f"https://github.com/hidasib/gru4rec_third_party_comparison/tree/{url_branch}",
    "use_repository_button": True,
    "icon_links": [
        {
            "name": "Github Last Commit",
            "url": "https://github.com/hidasib/gru4rec_third_party_comparison/tree/master",
            "icon": "https://img.shields.io/github/last-commit/hidasib/GRU4Rec/master",
            "type": "url",
        }
    ]
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ["custom.css"]
html_js_files = ["custom.js"]

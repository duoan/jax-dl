# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Deep Learning with JAX"
copyright = "2025, Victor An"
author = "Victor An"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "nbsphinx",  # This extension will allow Jupyter notebook support
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "en"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Specify the theme for the ReadTheDocs theme
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]


# Optional: Set this to True if you want to run the notebooks automatically when building the docs
nbsphinx_execute = "auto"

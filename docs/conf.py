# Configuration file for the Sphinx documentation builder.

# import os
# import sys

# sys.path.insert(
#     0, os.path.abspath("c:\\users\\ruben\\appdata\\local\\programs\\python\\python310\\lib\\site-packages")
# )
# import sphinx_rtd_theme

# -- Project information

project = "Material Picker"
copyright = "2023, Ruben Messerschmidt"
author = "Ruben Messerschmidt"

release = "1.0.0"
version = "1.0.0"

# -- General configuration

extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for HTML output

html_theme = "sphinx_rtd_theme"

# -- Options for EPUB output
epub_show_urls = "footnote"

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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'openGauss'
copyright = '2023, openGauss'
author = 'openGauss'

# The full version, including alpha/beta/rc tags
release = 'latest'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
     'myst_parser',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# source_parsers = {
#     '.md': 'recommonmark.parser.CommonMarkParser',
# }

from sphinx.builders.html import StandaloneHTMLBuilder

StandaloneHTMLBuilder.supported_image_types = ['image/svg+xml', 'image/png', 'image/gif', 'image/jpeg']
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# latex_elements = {
#     # The paper size ('letterpaper' or 'a4paper').
#     # 'papersize': 'letterpaper',

#     # The font size ('10pt', '11pt' or '12pt').
#     # 'pointsize': '10pt',

#     # Additional stuff for the LaTeX preamble.
#     'preamble': '''
#     \\hypersetup{unicode=true}
#     \\usepackage{CJKutf8}
#     \\AtBeginDocument{\\begin{CJK}{UTF8}{gbsn}}
#     \\AtEndDocument{\\end{CJK}}
#     ''',

#     # Latex figure (float) alignment
#     # 'figure_align': 'htbp',
# }

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
# html_style = '_static/my_theme.css'
master_doc= 'index'


# from docutils import nodes
# from sphinxcontrib.confluencebuilder.translator.storage import ConfluenceStorageFormatTranslator

# def override_raw_hook(self, node):
#     if 'html' in node.get('format', '').split():
#         node['format'] += ' confluence_storage'
#         ConfluenceStorageFormatTranslator.visit_raw(self, node)
#     raise nodes.SkipNode

# def setup(app):
#     app.add_node(nodes.raw,
#         confluence=(override_raw_hook, None),
#         override=True)
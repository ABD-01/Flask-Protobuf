# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
from protoserver import __version__

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'TMCVP Protobuf Server'
copyright = '2024, Muhammed Abdullah Shaikh'
author = 'Muhammed Abdullah Shaikh'
release = __version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'myst_parser',
    'sphinx_design',
    'sphinx.ext.intersphinx',
    # 'sphinx_tippy',     # for links
    'sphinxcontrib.mermaid',    # for mermaid diagrams
]

source_suffix = ['.rst', '.md']

myst_enable_extensions = [
    "colon_fence",
    # "attrs_inline", "attrs_block",  # Ref: https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#attributes
    ]
myst_all_links_external = True

autoclass_content = 'class'
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'undoc-members': True,
}
# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True      # To show return type separately
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = False

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "protobuf": ("https://googleapis.dev/python/protobuf/latest/", None),
    "Flask": ("https://flask.palletsprojects.com/en/latest/", None),
    "Flask-WTF": ("https://flask-wtf.readthedocs.io/en/1.2.x/", None),
    "WTForms": ("https://wtforms.readthedocs.io/en/3.1.x/", None),
    "werkzeug" : ("https://werkzeug.palletsprojects.com/en/latest/", None),
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

html_favicon = '_static/favicon.ico'

html_extra_path = ['demo']

html_theme_options = {
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/ABD-01/Flask-Protobuf",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": "",
        },
    ],
}
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

project = "TriFinger Documentation"
copyright = "2023, Max Planck Institute for Intelligent Systems"
author = "Max Planck Institute for Intelligent Systems"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "venv"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_material"

# Material theme options
html_theme_options = {
    # Set the name of the project to appear in the navigation.
    "nav_title": "TriFinger Documentation",
    # Visible levels of the global TOC; -1 means unlimited
    "globaltoc_depth": 1,
    # If False, expand all TOC entries
    "globaltoc_collapse": True,
    # If True, show hidden TOC entries
    "globaltoc_includehidden": False,
}

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
# This is theme-specific.
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

html_title = "Main Documentation"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# These paths are either relative to html_static_path or fully qualified paths (eg.
# https://...)
html_css_files = [
    'custom.css',
]


# == intersphinx ==
intersphinx_mapping = {
    "robot_fingers": (
        "https://open-dynamic-robot-initiative.github.io/robot_fingers",
        None,
    ),
    "robot_interfaces": (
        "https://open-dynamic-robot-initiative.github.io/robot_interfaces",
        None,
    ),
    "robot_properties_fingers": (
        "https://open-dynamic-robot-initiative.github.io/robot_properties_fingers",
        None,
    ),
    "blmc_drivers": (
        "https://open-dynamic-robot-initiative.github.io/blmc_drivers",
        None,
    ),
    "trifinger_simulation": (
        "https://open-dynamic-robot-initiative.github.io/trifinger_simulation",
        None,
    ),
    "trifinger_cameras": (
        "https://open-dynamic-robot-initiative.github.io/trifinger_cameras",
        None,
    ),
    "trifinger_object_tracking": (
        "https://open-dynamic-robot-initiative.github.io/trifinger_object_tracking",
        None,
    ),
}

# == todo ==

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

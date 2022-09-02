# -*- coding: utf-8 -*-
#
# IOOS Next Gen Sensor Map documentation build configuration file, created by
# sphinx-quickstart on Mon Aug 28 11:05:37 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import datetime
import os
import sphinx_rtd_theme
import yaml

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = '3.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.intersphinx', 'sphinx.ext.autosectionlabel', 'sphinx.ext.ifconfig']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
author = u'Axiom Data Science'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u''
# The full version, including alpha/beta/rc tags.
release = u''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = 'sphinx_rtd_theme'

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

#disable "View Source Link"
html_show_sourcelink = False

#html_favicon = 'images/IOOS_favicon.ico'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Set app config including static paths, stylesheets, and includes
# These settings are reactive to the PORTAL environment variable
def setup(app):
    #set config defaults
    config = {
        'title': 'Data Portal Documentation',
        'logo':'partner_content/global/images/axiom_logo.png',
        'favicon':'partner_content/global/images/axiom_favicon.png'
    }

    app.add_stylesheet('css/my_theme.css')
    app.config.html_static_path = ['custom']
    app.config.rst_prolog = '.. include:: /partner_content/global/global_substitutions.txt'
    app.config.exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
    app.config.copyright = '%d, Axiom Data Science' % datetime.datetime.now().year

    if 'PORTAL' in os.environ:
        portal = os.environ['PORTAL']
        tags.add(portal)

        for contentdir in os.listdir('partner_content'):
            if contentdir != portal:
                app.config.exclude_patterns.append('partner_content/%s/pages' % contentdir)

        #exclude catalog how-to pages from ioos build toc
        if portal == 'ioos':
            app.config.exclude_patterns.append('how-to/catalog')
            app.config.exclude_patterns.append('how-to/map/map-add-layers.rst')
            app.config.exclude_patterns.append('how-to/map/view-historical-gridded-data.rst')
       
        #include glider data pages only for secoora and caloos
        if portal != 'secoora' and portal != 'caloos':
            app.config.exclude_patterns.append('how-to/map/map-view-glider-data.rst')

        #exclude main how-to pages from ooi build toc
        if portal == 'ooi':
            app.config.exclude_patterns.append('how-to/catalog')
            app.config.exclude_patterns.append('how-to/map')
            app.config.exclude_patterns.append('how-to/data-views')
            
        #exclude ooi how-to pages from not ooi build toc
        if portal != 'ooi':
            app.config.exclude_patterns.append('how-to/ooi')

        #exclude data views, QARTOD and Data Inventory from ATN
        if portal == 'atn':
            app.config.exclude_patterns.append('how-to/map/data-charts-QARTOD.rst')
            app.config.exclude_patterns.append('how-to/map/data-charts-data-inventory.rst')

        #exclude QARTOD, Data Inventory and Contribute Data from MBON
        if portal == 'mbon':
            app.config.exclude_patterns.append('how-to/map/data-charts-QARTOD.rst')
            app.config.exclude_patterns.append('how-to/map/data-charts-data-inventory.rst')
            app.config.exclude_patterns.append('how-to/catalog/contribute-data.rst')

        #include custom map how tos for only mariculture map portal
        if portal != 'marm':
            app.config.exclude_patterns.append('how-to/map/draw-tools-how-to.rst')
            app.config.exclude_patterns.append('how-to/map/create-custom-map-how-to.rst')
            app.config.exclude_patterns.append('how-to/map/create-account-how-to.rst')
            app.config.exclude_patterns.append('how-to/map/map-view-layer-types.rst')

        #include portal include file if one exists
        portal_include_file = 'partner_content/%s/substitutions.txt' % portal
        if os.path.exists(portal_include_file):
            app.config.rst_prolog += '\n.. include:: /%s' % portal_include_file
        else:
            app.config.rst_prolog += '\n.. include:: /partner_content/global/default_substitutions.txt'

        #include custom portal static content
        portal_content_dir = 'partner_content/%s/static' % portal
        if os.path.exists(portal_content_dir):
            app.config.html_static_path.append(portal_content_dir)

        #load config file
        portal_config_file = 'partner_content/%s/config.yml' % portal
        if os.path.exists(portal_config_file):
            #override config defaults with yaml config values
            config.update(yaml.load(open(portal_config_file)))

        #load css
        portal_css_file = 'partner_content/%s/static/css/partner_theme.css' % portal
        if os.path.exists(portal_css_file):
            app.add_stylesheet('css/partner_theme.css')

    else:
        app.config.rst_prolog += '\n.. include:: /partner_content/global/default_substitutions.txt'
        app.config.exclude_patterns.append('partner_content/**/pages')

    app.config.project = config['title']
    app.config.html_title = config['title']
    app.config.html_logo = config['logo']
    app.config.html_favicon = config['favicon']

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'DataPortaldoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'IOOSNextGenSensorMap.tex', u'IOOS Next Gen Sensor Map Documentation',
     u'Axiom Data Science', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'ioosnextgensensormap', u'IOOS Next Gen Sensor Map Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'IOOSNextGenSensorMap', u'IOOS Next Gen Sensor Map Documentation',
     author, 'IOOSNextGenSensorMap', 'One line description of project.',
     'Miscellaneous'),
]




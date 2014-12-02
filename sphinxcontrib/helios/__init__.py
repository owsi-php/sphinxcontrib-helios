# -*- coding: utf-8 -*-

"""
    SphinxContrib.helios
    ~~~~~~~~~~~~~~~~~~~~

    .. autofunction:: setup
"""

from sphinxcontrib.helios.roles import HeliosRole
from sphinxcontrib.helios.nodes import helios
from sphinxcontrib.helios.directives import HeliosDirective

def setup(app):
    """Set up the helios extension:

        * register roles
        * register nodes
        * register directives

    """

    app.add_role("helios", HeliosRole())
    app.add_nodes(helios)
    app.add_directives("helios", HeliosDirective)

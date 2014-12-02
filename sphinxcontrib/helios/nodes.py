# -*- coding: utf-8 -*-

"""
    New Doctree Roles Helios
    ~~~~~~~~~~~~~~~~~~~~~~~~

    .. autoclass:: HeliosRole
        :show-inheritance:

        .. automethod:: result_nodes
"""

from sphinx.roles import XRefRole

class HeliosRole(XRefRole):

    """Class for processing the :rst:role:`helios` role."""

    def result_nodes(self, document, env, node, is_ref):
        """ Transform helios node"""
        return "TODO"

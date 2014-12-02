# -*- coding: utf-8 -*-
"""
    New Doctree Directive : Helios
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. autoclass:: HeliosDirective

        .. automethod:: run
        .. automethod:: process_helios
        .. automethod:: parse_helios

    .. autofunction:: process_start_option
"""
from docutils.parsers.rst import directives
from sphinx.util.compat import Directive

def process_start_option(value:):
    """Process and validate the start option value
    of a :rst:dir:`helios` directive.
    The *value* is converted.
    """
    return value

class HeliosDirective(Directive):

    """Class for processing the :rst:dir:`helios` directive.

    """

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = Truehas_content = False
    option_spec = {
        'style': directives.unchanged
    }

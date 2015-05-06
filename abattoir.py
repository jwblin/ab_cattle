#==============================================================================
# Abattoir class
#
# By Johnny Lin
# May 2015
#==============================================================================


import numpy as N


class Abattoir(object):
    """Create and manage a abattoir.

    As cattle location information is stored in a Cattle object, the
    purpose of the environmenet objects is to keep track of possible
    spatial locations.
    """
    def __init__(self):
        self.length = None
        self.width = None


    def next_location(self, x_current, y_current):
        """Given the current location in the environment, ."""
        pass

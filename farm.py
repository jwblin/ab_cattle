#==============================================================================
# Farm class
#
# By Johnny Lin
# May 2015
#==============================================================================


import numpy as N


class Farm(object):
    """Create and manage a farm.

    The constructor here does not create a Cattle object, which is how the
    farm initialization method works in Shiflet & Shiflet (2014).  As
    cattle location information is stored in a Cattle object, the purpose
    of the environmenet objects is to keep track of possible spatial 
    locations.
    """
    def __init__(self):
        self.length = 95
        self.width = 16


    def next_location(self, x_current, y_current):
        """Given the current location in the environment, ."""
        pass

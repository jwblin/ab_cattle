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


    def move_cattle(self, inCattle):
        pass


    def feed_cattle(self, inCattle):
        pass


    def sir_cattle(self, inCattle):
        pass


    def _test_pass_in_cattle(self, inCattle):
        """Test receiving a Cattle object."""
        return inCattle.loc_in_environ

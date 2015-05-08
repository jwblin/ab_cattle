#==============================================================================
# Farm class
#
# By Johnny Lin
# May 2015
#==============================================================================


import numpy as N
from roadeast import RoadEast


class Farm(object):
    """Create and manage a farm.

    Attributes
    ----------
    road : RoadEast or RoadWest
        The object that is the road that is adjacent to this farm.

    farm_index : int
        Each farm has an index from 0 to 2.  The 0th index is the farm that
        is the farthest away from the salebarn.  The 2th index is farm that
        is adjacent to the salebarn.  We also assume the farm width indices
        go from farthest away from salebarn @@@edit

    The constructor here does not create a Cattle object, which is how the
    farm initialization method works in Shiflet & Shiflet (2014).  As
    cattle location information is stored in a Cattle object, the purpose
    of the environmenet objects is to keep track of possible spatial 
    locations.
    """
    def __init__(self, road=RoadEast(), farm_index=0):
        self.length = 95
        self.width = 16
        self.adjacent_road = road
        self.farm_index = farm_index


    def move_cattle(self, inCattle):
        """Move the cattle in the farm or off.

        Notes
        -----
            This method incorporates part of inFarm and farm2Sale from Shiflet 
            and Shiflet (2014).

            The choice of random number generators was informed by this:
            http://stackoverflow.com/a/13353563.
        """
        if inCattle.weight < 600.0:
            loc = [inCattle.loc_in_environ[0], inCattle.loc_in_environ[1]]
            step = [1, -1]
            N.random.shuffle(step)
            loc = [loc[0]+step, loc[1]]
            N.random.shuffle(step)
            loc = [loc[0],      loc[1]+step]
            if loc[0] < 0:  loc[0] = 0
            if loc[1] < 0:  loc[1] = 0
            if loc[0] > self.length:  loc[0] = 0
            if loc[1] > self.width:   loc[1] = 0
        return inCattle


    def feed_cattle(self, inCattle):
        pass


    def sir_cattle(self, inCattle):
        pass


    def _test_pass_in_cattle_chg(self, inCattle):
        """Test receiving a Cattle object."""
        inCattle.loc_in_environ = (6, 11)
        return inCattle


    def _test_pass_in_cattle_no_chg(self, inCattle):
        """Another test receiving a Cattle object."""
        return inCattle.loc_in_environ

#==============================================================================
# Farm class
#
# By Johnny Lin
# May 2015
#==============================================================================


import numpy as N
from roadeast import RoadEast
from roadwest import RoadWest


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
        increment starting from the location farthest away from salebarn to
        the location nearest.  Thus, for a 6 farm simulation, the farms with
        index 2 are both adjacent to the salebarn.

    The constructor here does not create a Cattle object, which is how the
    farm initialization method works in Shiflet & Shiflet (2014).  As
    cattle location information is stored in a Cattle object, the purpose
    of the environment objects is to keep track of possible spatial 
    locations.
    """
    def __init__(self, adjacent_road=None, farm_index=0):
        self.length = 95    #- length is the y direction
        self.width = 16     #- width is the x direction
        self.adjacent_road = adjacent_road
        self.farm_index = farm_index
        self.list_cattle = []


    def move_cattle(self, inCattle):
        """Move the cattle in the farm or off the farm.

        When moving the cattle off the farm, you enter the road at the location
        directly across from the width location of the farm you were on.

        Notes
        -----
            This method incorporates part of inFarm and farm2Sale from Shiflet 
            and Shiflet (2014).

            The choice of random number generators was informed by this:
            http://stackoverflow.com/a/13353563.
        """
        loc = N.array([inCattle.loc_in_environ[0], inCattle.loc_in_environ[1]])

        if inCattle.weight < 600.0:
            step = [1, -1]
            N.random.shuffle(step)
            loc = N.array([loc[0]+step[0], loc[1]])
            N.random.shuffle(step)
            loc = N.array([loc[0],      loc[1]+step[0]])
            if loc[0] < 0:  loc[0] = 0
            if loc[1] < 0:  loc[1] = 0
            if loc[1] >= self.width:   loc[1] = self.width-1
            if loc[0] >= self.length:  loc[0] = self.length-1

        else:                            #- move south
            loc[0] = loc[0] + 1
            if loc[0] >= self.length:    #+ move onto road
                inCattle.farm_just_left = inCattle.environ
                inCattle.environ = self.adjacent_road
                inCattle.environ.list_cattle.append(inCattle)
                self.list_cattle.remove(inCattle)
                loc = N.array([0, inCattle.environ.loc_on_road(inCattle)])
                inCattle.loc_in_environ = loc
                inCattle.farm_just_left = None
                return inCattle


        #- Check new location does not conflict with another cattle on the 
        #  farm.  If it does, retain old location:

        for iother in self.list_cattle:
            if isinstance(inCattle.environ, Farm) and \
               isinstance(iother.environ, Farm) and \
               N.allclose(N.array(iother.loc_in_environ), N.array(loc)) and \
               (id(iother) != id(inCattle)):
                return inCattle

        inCattle.loc_in_environ = loc
        return inCattle


    def feed_cattle(self, inCattle):
        if inCattle.weight < 600.0:
            inCattle.weight += N.random.uniform(0.5, 0.75)
        return inCattle


    def sir_cattle(self, inCattle):
        pass


    def _test_pass_in_cattle_chg(self, inCattle):
        """Test receiving a Cattle object."""
        inCattle.loc_in_environ = (6, 11)
        return inCattle


    def _test_pass_in_cattle_no_chg(self, inCattle):
        """Another test receiving a Cattle object."""
        return inCattle.loc_in_environ

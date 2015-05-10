#==============================================================================
# RoadEast class
#
# By Johnny Lin
# May 2015
#==============================================================================


import numpy as N


class RoadEast(object):
    """Create and manage a road east.

    As cattle location information is stored in a Cattle object, the
    purpose of the environmenet objects is to keep track of possible
    spatial locations.
    """
    def __init__(self, adjacent_salebarn=None):
        self.length = 1
        self.width = 3*16   #- Value depends on Farm width attribute
        self.adjacent_salebarn = adjacent_salebarn
        self.list_cattle = []


    def loc_on_road(self, inCattle):
        """Return location on the road.

        Since the road allows one cattle at any location, this method
        only returns the value of how far you're down the road.  The
        end of the road is at the salebarn, and so the highest location
        index is at the salebarn.
        """
        if inCattle.farm_just_left == None:
            if isinstance(inCattle, RoadEast):
                return inCattle.loc_in_environ[1]
            else:
                return None
        else:
            aFarm = inCattle.farm_just_left
            return aFarm.farm_index * aFarm.width + inCattle.loc_in_environ[1]


    def move_cattle(self, inCattle):
        """Move cattle down the road or into the salebarn.

        Assume that more than one cattle can occupy a single location.
        """
        loc = N.array([0, inCattle.loc_in_environ[1] + 1])

        if loc[1] >= self.width:            #- end of the road, goto salebarn
            self.list_cattle.remove(inCattle)
            inCattle.environ = self.adjacent_salebarn
            inCattle.inSale1 = True
            inCattle.environ.list_cattle.append(inCattle)
            loc = N.array([0, 0])

        inCattle.loc_in_environ = loc
        return inCattle


    def feed_cattle(self, inCattle):
        """Cattle eat no food and gain no weight on the road.
        """
        return inCattle

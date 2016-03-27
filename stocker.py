#==============================================================================
# Stocker class
#
# By Johnny Lin
# May 2015
#==============================================================================


import numpy as N
from roadeast import RoadEast


class Stocker(object):
    """Create and manage a stocker.

    The constructor here does not create a Cattle object, which is how the
    farm initialization method works in Shiflet & Shiflet (2014).  As
    cattle location information is stored in a Cattle object, the purpose
    of the environment objects is to keep track of possible spatial 
    locations.
    """
    def __init__(self, road=RoadEast(), farm_index=0):
        self.length = 16    #- length is y direction, same as salebarn
        self.width = 16*3   #- width is x direction, depends on number farms
        self.adjacent_salebarn = None
        self.list_cattle = []


    def move_cattle(self, inCattle):
        """Move the cattle in the stocker or off the stocker.

        As the width index decreases, you are moving further away from the
        salebarn.

        The algorithm for this method differs from Shiflet & Shiflet in that
        the cattle moves "randomly" west until they reach the midway point of
        the stocker, then they walk randomly.  This prevents bunching up near
        the boundary with the salebarn.
        """
        #- Initialize loc.  If reached minimum weight and and next to the 
        #  salebarn then move on to the salebarn.  Else, randomly move:

        loc = N.array([inCattle.loc_in_environ[0], inCattle.loc_in_environ[1]])

        if inCattle.weight >= 900.0:
            loc = N.array([loc[0], loc[1]+1])  #- move east
            if loc[1] < self.width:
                pass
            else:
                inCattle.environ = self.adjacent_salebarn
                inCattle.inSale2 = True
                inCattle.environ.list_cattle.append(inCattle)
                self.list_cattle.remove(inCattle)
                loc = N.array([loc[0], 0])
                inCattle.loc_in_environ = loc
                return inCattle

        else:                         #- move west past half-way point,
            step = [1, -1]            #  then randomly all directions
            N.random.shuffle(step)
            loc = N.array([loc[0]+step[0], loc[1]])
            if inCattle.loc_in_environ[1] > int(self.width/2):
                loc = N.array([loc[0], loc[1]-1])
            else:
                N.random.shuffle(step)
                loc = N.array([loc[0], loc[1]+step[0]])
            if loc[0] < 0:  loc[0] = 0
            if loc[1] < 0:  loc[1] = 0
            if loc[1] >= self.width:   loc[1] = self.width-1
            if loc[0] >= self.length:  loc[0] = self.length-1


        #- Check new location does not conflict with another cattle on the 
        #  stocker.  If it does, retain old location:

        for iother in self.list_cattle:
            if isinstance(inCattle.environ, Stocker) and \
               isinstance(iother.environ, Stocker) and \
               N.allclose(N.array(iother.loc_in_environ), N.array(loc)) and \
               (id(iother) != id(inCattle)):
                return inCattle

        inCattle.loc_in_environ = loc
        return inCattle


    def feed_cattle(self, inCattle):
        if inCattle.weight < 900.0:
            inCattle.weight += N.random.uniform(0.4, 0.6)
        return inCattle


    def sir_cattle(self, inCattle):
        pass




#===== end file =====

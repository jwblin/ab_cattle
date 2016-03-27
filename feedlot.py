#==============================================================================
# Feedlot class
#
# By Johnny Lin
# May 2015
#==============================================================================


import numpy as N


class Feedlot(object):
    """Create and manage a feedlot.

    The constructor here does not create a Cattle object, which is how the
    farm initialization method works in Shiflet & Shiflet (2014).  As
    cattle location information is stored in a Cattle object, the purpose
    of the environment objects is to keep track of possible spatial 
    locations.
    """
    def __init__(self):
        self.length = 16           #- length is y direction, same as salebarn
        self.width = int(16*1.5)   #- width is x direction
        self.adjacent_salebarn = None
        self.adjacent_abattoir = None
        self.list_cattle = []


    def move_cattle(self, inCattle):
        """Move the cattle in the feedlot or off the feedlot.

        As the width index increases, you are moving further away from the
        salebarn.
        """
        loc = N.array([inCattle.loc_in_environ[0], inCattle.loc_in_environ[1]])

        if inCattle.weight >= 1300.0:   #- heading towards abattoir (can
            loc = N.array([loc[0], loc[1]+1])    #  run over other cattle)
            if loc[1] >= self.width:    #- move to abattoir
                loc = N.array([loc[0], 0])
                inCattle.environ = self.adjacent_abattoir
                inCattle.environ.list_cattle.append(inCattle)
                self.list_cattle.remove(inCattle)
                inCattle.loc_in_environ = loc
                return inCattle

        else:                           #- random walk with no west movement
            step = [1, -1]
            N.random.shuffle(step)
            loc = N.array([loc[0]+step[0], loc[1]])
            loc = N.array([loc[0], loc[1]+1])
            if loc[0] < 0:  loc[0] = 0
            if loc[1] < 0:  loc[1] = 0
            if loc[1] >= self.width:   loc[1] = self.width-1
            if loc[0] >= self.length:  loc[0] = self.length-1

        #- Check new location does not conflict with another cattle on the 
        #  farm.  If it does, retain old location:

        for iother in self.list_cattle:
            if isinstance(inCattle.environ, Feedlot) and \
               isinstance(iother.environ, Feedlot) and \
               N.allclose(N.array(iother.loc_in_environ), N.array(loc)) and \
               (id(iother) != id(inCattle)):
                return inCattle

        inCattle.loc_in_environ = loc
        return inCattle


    def feed_cattle(self, inCattle):
        if inCattle.weight < 1300.0:
            inCattle.weight += N.random.uniform(0.5, 1.0)
        return inCattle


    def sir_cattle(self, inCattle):
        pass




#===== end file=====

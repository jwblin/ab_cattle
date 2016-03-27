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
    purpose of the environment objects is to keep track of possible
    spatial locations.
    """
    def __init__(self):
        self.length = 16
        self.width = 4
        self.list_cattle = []


    def move_cattle(self, inCattle):
        """Move the cattle in the abattoir for visualization.

        As the width index increases, you are moving further away from the
        salebarn.
        """
        #- Move randomly; collisions okay but cannot go west:

        loc = N.array([inCattle.loc_in_environ[0], inCattle.loc_in_environ[1]])
        step = [1, -1]
        N.random.shuffle(step)
        loc = N.array([loc[0]+step[0], loc[1]])
        loc = N.array([loc[0], loc[1]+1])
        if loc[0] < 0:  loc[0] = 0
        if loc[1] < 0:  loc[1] = 0
        if loc[1] >= self.width:   loc[1] = self.width-1
        if loc[0] >= self.length:  loc[0] = self.length-1

        inCattle.loc_in_environ = loc
        return inCattle


    def feed_cattle(self, inCattle):
        return inCattle


    def sir_cattle(self, inCattle):
        pass




#===== end file =====

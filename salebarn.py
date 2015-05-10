#==============================================================================
# SaleBarn class
#
# By Johnny Lin
# May 2015
#==============================================================================


import numpy as N


class SaleBarn(object):
    """Create and manage a sale barn.

    As cattle location information is stored in a Cattle object, the
    purpose of the environmenet objects is to keep track of possible
    spatial locations.
    """
    def __init__(self):
        self.length = 16  #- length is the y direction 
        self.width = 1    #- width is the x direction
        self.adjacent_stocker = None
        self.adjacent_feedlot = None
        self.list_cattle = []


    def move_cattle(self, inCattle):
        """Move cattle in the salebarn.

        Assume that more than one cattle can occupy a single location.  The
        algorithm we use is slightly different from Shiflet & Shiflet (2014)'s.
        """
        step = [1, -1]
        N.random.shuffle(step)
        loc = N.array([inCattle.loc_in_environ[0]+step[0], 0])
        if loc[0] < 0:  loc[0] = 0
        if loc[0] >= self.length:  loc[0] = self.length-1

        if inCattle.inSale1 and not inCattle.inSale2:
            if inCattle.time1InSale == 0:
                inCattle.time1InSale = N.random.randint(1,6)
            else:
                inCattle.time1InSale += 1

            if inCattle.time1InSale > 8:  #- goto stocker
                inCattle.environ = self.adjacent_stocker
                inCattle.inSale1 = False
                inCattle.environ.list_cattle.append(inCattle)
                self.list_cattle.remove(inCattle)
                loc = N.array([loc[0], inCattle.environ.width-1])

        elif inCattle.inSale2 and not inCattle.inSale1:
            if inCattle.time2InSale == 0:
                inCattle.time2InSale = N.random.randint(1,6)
            else:
                inCattle.time2InSale += 1

            if inCattle.time2InSale > 8:  #- goto feedlot
                inCattle.environ = self.adjacent_feedlot
                inCattle.inSale2 = False
                inCattle.environ.list_cattle.append(inCattle)
                self.list_cattle.remove(inCattle)
                loc = N.array([loc[0], 0])

        else:
            raise ValueError, "Should not be in the salebarn"

        inCattle.loc_in_environ = loc
        return inCattle


    def feed_cattle(self, inCattle):
        return inCattle




#===== end file =====

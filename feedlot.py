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
        #TO DO
        pass


    def feed_cattle(self, inCattle):
        #TO DO
        pass


    def sir_cattle(self, inCattle):
        pass




#===== end file=====

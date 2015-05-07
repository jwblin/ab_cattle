#==============================================================================
# Model class
#
# By Johnny Lin
# May 2015
#==============================================================================


import numpy as N
from cattle import Cattle
from farm import Farm
from roadeast import RoadEast
from roadwest import RoadWest
from salebarn import SaleBarn
from stocker import Stocker
from feedlot import Feedlot
from abattoir import Abattoir
import visualize as V


class Model(object):
    def __init__(self, dt=0.25):
        """Initialize model object.

        Parameters
        ----------
        dt : float
            Time step in days.
        """
        self._string_test = "Hello there"
        self.dt = dt
        self.numSusceptible = 0
        self.numInfected = 0
        self.numRecovered = 0

        self.INIT_CATTLE_PROBABILITY = 0.02

        self.list_cattle = []
        self.list_environ = []
        self.list_environ.append(RoadEast())
        self.list_environ.append(RoadWest())
        self.list_environ.append(SaleBarn())
        self.list_environ.append(Stocker())
        self.list_environ.append(Feedlot())
        self.list_environ.append(Abattoir())

        self.num_farms = 6
        self.farm_cattle_init()


    def farm_cattle_init(self):
        for inum in range(self.num_farms):
            aFarm = Farm()
            self.list_environ.append(aFarm)

            for ilength in range(aFarm.length):
                for iwidth in range(aFarm.width):
                    if N.random.uniform() < self.INIT_CATTLE_PROBABILITY:
                        aCattle = Cattle(x_init=iwidth, y_init=ilength, 
                                         env=aFarm)
                        self.list_cattle.append(aCattle)
                        del aCattle
            del aFarm


    def plot_one_timestep(self):
        pass


    def run_session(self, num_days=100):
        print("Running ...")
        #@@@for it in range( int(N.ceil(num_days/self.dt)) ):
            #@@@for icattle in self.list_cattle:
                #@@@icattle.update()
        print("Program successfully ended.")

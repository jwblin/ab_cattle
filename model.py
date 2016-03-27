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
import matplotlib.pyplot as plt


class Model(object):
    """Cattle model.
    
    Attributes
    ----------
    sim_day : float
        Simulation day.  Created when run_session is called.
    """
    def __init__(self, dt=0.25, init_extra_weight=0.0):
        """Initialize model object.

        Parameters
        ----------
        dt : float
            Time step in days.

        init_extra_weight : float
            Adds this many pounds to the initialization of each cattle in
            order to speed-up the simulation.
        """
        self._string_test = "Hello there"
        self.dt = dt
        self.numSusceptible = 0
        self.numInfected = 0
        self.numRecovered = 0
        self.cumulativeInfected = 0

        self.INIT_CATTLE_PROBABILITY = 0.02
        self._init_extra_weight = init_extra_weight

        self.plot_figure = None
        self.plot_axes = None
        self.plot_image = None

        self.list_cattle = []
        self.list_farms = []
        self.salebarn = SaleBarn()
        self.stocker = Stocker()
        self.feedlot = Feedlot()
        self.abattoir = Abattoir()
        self.roadeast = RoadEast(adjacent_salebarn=self.salebarn)
        self.roadwest = RoadWest(adjacent_salebarn=self.salebarn)


        #- Linkages for multi-way movement between certain regions:

        self.salebarn.adjacent_stocker = self.stocker
        self.salebarn.adjacent_feedlot = self.feedlot
        self.stocker.adjacent_salebarn = self.salebarn
        self.feedlot.adjacent_salebarn = self.salebarn
        self.feedlot.adjacent_abattoir = self.abattoir

        self.num_farms = 6
        self.farm_cattle_init()


    def farm_cattle_init(self):
        #- Fill up with susceptible cattle:

        each_side_farm_index = range(int(self.num_farms)/int(2))

        for inum in each_side_farm_index:
            roadEastFarm = Farm(adjacent_road=self.roadeast, farm_index=inum)
            self.list_farms.append(roadEastFarm)

            for ilength in range(roadEastFarm.length):
                for iwidth in range(roadEastFarm.width):
                    if N.random.uniform() < self.INIT_CATTLE_PROBABILITY:
                        aCattle = Cattle(x_init=iwidth, y_init=ilength,
                                         dt=self.dt,
                                         env=roadEastFarm)
                        aCattle.weight += self._init_extra_weight
                        roadEastFarm.list_cattle.append(aCattle)
                        self.list_cattle.append(aCattle)

        each_side_farm_index.reverse()
        for inum in each_side_farm_index:
            roadWestFarm = Farm(adjacent_road=self.roadwest, farm_index=inum)
            self.list_farms.append(roadWestFarm)

            for ilength in range(roadWestFarm.length):
                for iwidth in range(roadWestFarm.width):
                    if N.random.uniform() < self.INIT_CATTLE_PROBABILITY:
                        aCattle = Cattle(x_init=iwidth, y_init=ilength, 
                                         dt=self.dt,
                                         env=roadWestFarm)
                        aCattle.weight += self._init_extra_weight
                        roadWestFarm.list_cattle.append(aCattle)
                        self.list_cattle.append(aCattle)

        self.numSusceptible = len(self.list_cattle) - 1


        #- Make one cattle infected:

        self.list_cattle[20].state = "Infected"
        self.list_cattle[20].daysSick = 0
        self.numInfected += 1
        self.cumulativeInfected += 1


    def run_session(self, num_days=300):
        print("Running ...")
        for it in range( int(N.ceil(num_days/self.dt)) ):
            self.sim_day = it*self.dt
            for icattle in self.list_cattle:
                a, b, c, d = icattle.update()
                self.numSusceptible += a
                self.numInfected += b
                self.numRecovered += c
                self.cumulativeInfected += d

            print "Day " + str(self.sim_day) + \
                ": Susceptible = " + str(self.numSusceptible)
            print "Day " + str(self.sim_day) + \
                ": Infected = " + str(self.numInfected)
            print "Day " + str(self.sim_day) + \
                ": Recovered = " + str(self.numRecovered)
        print("Program successfully ended.")


    def _run_session_plot_out(self, num_days=10):
        print("Running ...")
        for it in range( int(N.ceil(num_days/self.dt)) ):
            self.sim_day = it*self.dt
            for icattle in self.list_cattle:
                a, b, c, d = icattle.update()
                self.numSusceptible += a
                self.numInfected += b
                self.numRecovered += c
                self.cumulativeInfected += d

            if it == 0:
                plt.ion()
                self.plot_figure, self.plot_axes, self.plot_image = \
                    V.plot_ranch(self)
            else:
                self.plot_figure, self.plot_axes, self.plot_image = \
                    V.plot_ranch(self, 
                    use_objs=(self.plot_figure, self.plot_axes, 
                              self.plot_image))
            print "Day " + str(self.sim_day) + \
                ": Susceptible = " + str(self.numSusceptible)
            print "Day " + str(self.sim_day) + \
                ": Infected = " + str(self.numInfected)
            print "Day " + str(self.sim_day) + \
                ": Recovered = " + str(self.numRecovered)
        print("Program successfully ended.")


    def _run_session_print_out(self, num_days=300):
        print("Running ...")
        for it in range( int(N.ceil(num_days/self.dt)) ):
            self.sim_day = it*self.dt
            for i in range(len(self.list_cattle)):
                icattle = self.list_cattle[i]
                if i == 0:
                    print it, icattle.loc_in_environ, icattle.weight, \
                          icattle.environ, len(icattle.environ.list_cattle)
                icattle.update()
        print("Program successfully ended.")




#===== end file =====

#==============================================================================
# Cattle class
#
# By Johnny Lin
# May 2015
#==============================================================================


import numpy as N
from farm import Farm
from roadeast import RoadEast
from roadwest import RoadWest
from salebarn import SaleBarn
from stocker import Stocker
from feedlot import Feedlot
from abattoir import Abattoir


class Cattle(object):
    """Create and manage a cattle.

    Attributes
    ----------
    environ : variety of types
        The environment object where the cattle current is.

    loc_in_environ : numpy.ndarray
        The x and y locations in the environment.  The values are ints
        and are given in the coordinates of the given environment type.
        Two-elements long.

    state : string
        Either "Susceptible", "Infected", "Recovered", or "Processed".
    """
    def __init__(self, x_init=0, y_init=0, env=None, state="Susceptible",
                 dt=0.25):
        self.environ = env
        self.loc_in_environ = N.array([y_init, x_init])
        self.farm_just_left = None
        self.state = state
        self.dt = dt
        self.inSale1 = False   #- Are you in the salebarn the 1st time?
        self.inSale2 = False   #- Are you in the salebarn the 2nd time?
        self.time1InSale = 0
        self.time2InSale = 0
        self.weight = N.random.uniform()*40.0 + 60.0
        if self.state == "Infected":
            self.daysSick = 0
        else:
            self.daysSick = None
        self.INFECTIOUS_PERIOD = 40.0
        self.INFECTION_PROBABILITY = 0.125


    def state_as_int(self):
        if self.state == "Susceptible":
            return 1
        elif self.state == "Infected":
            return 2
        elif self.state == "Recovered":
            return 3
        elif self.state == "Processed":
            return 4
        else:
            raise ValueError, "Incorrect state"


    def isNextToInfected(self):
        north = N.array([self.loc_in_environ[0]+1, self.loc_in_environ[1]])
        south = N.array([self.loc_in_environ[0]-1, self.loc_in_environ[1]])
        east = N.array([self.loc_in_environ[0], self.loc_in_environ[1]+1])
        west = N.array([self.loc_in_environ[0], self.loc_in_environ[1]-1])

        if north[0] < 0:  north[0] = 0
        if south[0] < 0:  south[0] = 0
        if east[1] < 0:  east[1] = 0
        if west[1] < 0:  west[1] = 0

        if north[0] > self.environ.length-1:  north[0] = self.environ.length-1
        if south[0] > self.environ.length-1:  south[0] = self.environ.length-1
        if east[1] > self.environ.width-1:  east[1] = self.environ.width-1
        if west[1] > self.environ.width-1:  west[1] = self.environ.width-1

        for inext in [north, south, east, west]:
            for iCattle in self.environ.list_cattle:
                if N.allclose(N.array(inext), N.array(iCattle.loc_in_environ)):
                    if iCattle.state == "Infected":
                        return True
        return False


    def sir(self):
        """Advance the illness state for the cattle.

        Returns counter increments.  Non-SIR cattle do not alter the 
        counters.
        """
        dnumSusceptible = 0
        dnumInfected = 0
        dnumRecovered = 0
        dcumulativeInfected = 0

        if (self.state == "Infected") and \
           (self.daysSick > self.INFECTIOUS_PERIOD):
            self.state = "Recovered"
            dnumInfected = -1
            dnumRecovered = 1
        elif (self.state == "Infected"):
            self.daysSick += self.dt
        elif (self.state == "Susceptible") and self.isNextToInfected():
            rand = N.random.uniform()
            if rand < self.INFECTION_PROBABILITY:
                self.state = "Infected"
                self.daysSick = 0
                dnumSusceptible = -1
                dnumInfected = 1
                dcumulativeInfected = 1
        else:
            pass

        return dnumSusceptible, dnumInfected, \
               dnumRecovered, dcumulativeInfected


    def update(self):
        dnumSusceptible = 0
        dnumInfected = 0
        dnumRecovered = 0
        dcumulativeInfected = 0

        if isinstance(self.environ, Abattoir):
            if self.state == "Susceptible":
                dnumSusceptible = -1
            elif self.state == "Infected":
                dnumInfected = -1
            elif self.state == "Recovered":
                dnumRecovered = -1
            else:
                pass
            self.state = "Processed"  #- Once in abattoir you become processed
        else:
            dnumSusceptible, dnumInfected, \
                dnumRecovered, dcumulativeInfected = self.sir()

        self.environ.move_cattle(self)
        self.environ.feed_cattle(self)

        return dnumSusceptible, dnumInfected, \
               dnumRecovered, dcumulativeInfected


    def _test_pass_in_self_chg(self):
        """Test passing in self as a parameter."""
        return self.environ._test_pass_in_cattle_chg(self)


    def _test_pass_in_self_no_chg(self):
        """Test passing in self as a parameter."""
        return self.environ._test_pass_in_cattle_no_chg(self)

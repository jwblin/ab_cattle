#==============================================================================
# Cattle class
#
# By Johnny Lin
# May 2015
#==============================================================================


import numpy as N
from .farm import Farm
from .roadeast import RoadEast
from .roadwest import RoadWest
from .salebarn import SaleBarn
from .stocker import Stocker
from .feedlot import Feedlot
from .abattoir import Abattoir


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
            raise ValueError("Incorrect state")


    def isNextToInfected(self):
        pass   # Put code in lieu of this line


    def sir(self):
        """Advance the illness state for the cattle.

        Returns counter increments.  Non-SIR cattle do not alter the 
        counters.
        """
        pass   # Put code in lieu of this line

        return dnumSusceptible, dnumInfected, \
               dnumRecovered, dcumulativeInfected


    def update(self):
        pass   # Put code in lieu of this line

        return dnumSusceptible, dnumInfected, \
               dnumRecovered, dcumulativeInfected


    def _test_pass_in_self_chg(self):
        """Test passing in self as a parameter."""
        return self.environ._test_pass_in_cattle_chg(self)


    def _test_pass_in_self_no_chg(self):
        """Test passing in self as a parameter."""
        return self.environ._test_pass_in_cattle_no_chg(self)

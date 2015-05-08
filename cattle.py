#==============================================================================
# Cattle class
#
# By Johnny Lin
# May 2015
#==============================================================================


from farm import Farm
from feedlot import Feedlot


class Cattle(object):
    """Create and manage a cattle.

    Attributes
    ----------
    environ : variety of types
        The environment object where the cattle current is.

    loc_in_environ : tuple
        The x and y locations in the environment.  The values are ints
        and are given in the coordinates of the given environment type.

    state : string
        Either "Susceptible", "Infected", or "Recovered".
    """
    def __init__(self, x_init=0, y_init=0, env=None, state="Susceptible"):
        self.environ = env
        self.loc_in_environ = [y_init, x_init]
        self.state = state
        self.weight = N.random.uniform()*40.0 + 60.0
        if self.state == "Infected":
            self.days_sick = 0
        else:
            self.days_sick = None


    def state_as_int(self):
        if self.state == "Susceptible":
            return 1
        elif self.state == "Infected":
            return 2
        elif self.state == "Recovered":
            return 3
        else:
            raise ValueError, "Incorrect state"


    def update(self):
        if isinstance(self.environ, Farm):
            self.sir()
            if self.weight < 600.0:
                self.environ.move_cattle(self)
                self.environ.feed_cattle(self)
            else:
                pass #@@@

        elif isinstance(self.environ, Feedlot):
            pass #@@@



    def _test_pass_in_self_chg(self):
        """Test passing in self as a parameter."""
        return self.environ._test_pass_in_cattle_chg(self)


    def _test_pass_in_self_no_chg(self):
        """Test passing in self as a parameter."""
        return self.environ._test_pass_in_cattle_no_chg(self)

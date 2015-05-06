#==============================================================================
# Cattle class
#
# By Johnny Lin
# May 2015
#==============================================================================


class Cattle(object):
    """Create and manage a cattle.

    Attributes
    ----------
    environ : variety of types
        The environment object where the cattle is on.

    loc_in_environ : tuple
        The x and y locations in the environment.  The values are ints
        and are given in the coordinates of the given environment type.

    state : string
        Either "Susceptible", "Infected", or "Recovered".
    """
    def __init__(self, x_init=0, y_init=0, env=None):
        self.environ = env
        self.loc_in_environ = (y_init, x_init)
        self.state = "Susceptible"


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
        """Runs scheduler."""
        pass

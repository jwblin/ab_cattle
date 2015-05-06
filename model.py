#==============================================================================
# Model class
#
# By Johnny Lin
# May 2015
#==============================================================================


class Model(object):
    def __init__(self, dt=0.25):
        self._string_test = "Hello there"
        self.numSusceptible = 0
        self.numInfected = 0
        self.numRecovered = 0

    def run_session(self):
        print("Running ...")
        print("Program successfully ended.")

#!/usr/bin/python -tt
#==============================================================================
#                            General Documentation

"""Define tests for unittest for module cattle in the ab_cattle package.

   Execution of:
   $ python test.py

   in this tests directory will execute all tests, including those defined 
   in this current module.

   This module contains a single class named Tests.  This class consists
   solely of methods that are tests.  Global data initialization is done
   in test.py.
"""

#------------------------------------------------------------------------------
#                           Additional Documentation
#
# RCS Revision Code:
#   $Id: test_exam.py 64 2008-11-13 18:47:45Z jlin $
#
# Modification History:
# - 5 May 2015:  Adapted for cattle and disease package.
# - 16 Mar 2006:  Original by Johnny Lin, Physics Department, North Park 
#   University.
#
# Notes:
# - Written for Python 2.7.
# - See import/reload statements throughout module for dependencies.
#
# Copyright (c) 2006-2015 by Johnny Lin.  For licensing, distribution 
# conditions, contact information, and additional documentation see
# the URL http://www.johnny-lin.com/pylib.shtml.
#==============================================================================




#------------------- Module General Import and Declarations -------------------

#- If you're importing this module in testing mode, append the directory
#  the package is in to the PYTHONPATH so imports to the package can be
#  resolved.  See:  http://stackoverflow.com/a/19190695.

import os
if (__name__ == '__main__') and (__package__ is None):
    filename = os.path.abspath(__file__)
    tests_dir = os.path.dirname(filename)
    package_dir = os.path.dirname(tests_dir)
    parent_to_package_dir = os.path.dirname(package_dir)
    os.sys.path.append(parent_to_package_dir)


#- Import other modules at module level:

import copy
import matplotlib.pyplot as plt
import numpy as N
from ab_cattle import cattle
from ab_cattle import farm
from ab_cattle import model
from ab_cattle import visualize




#------------------------------------ Tests -----------------------------------

class Tests(object):
#commented out for now since I just want to do a single visualization
#    def test_show_plot_of_farm(self):
#        """Plots a single farm."""
#        aFarm = farm.Farm()
#        list_of_cattle = []
#        list_of_states = ["Susceptible", "Infected", "Recovered"]
#
#        for i in range(50):
#            xloc = N.random.randint(aFarm.width)
#            yloc = N.random.randint(aFarm.length)
#            temp_cattle = cattle.Cattle( x_init=xloc, 
#                                         y_init=yloc,
#                                         env=aFarm )
#            temp_cattle.state = list_of_states[N.random.randint(3)]
#            list_of_cattle.append(temp_cattle)

        #- Commented out since I know the farm works:
        #visualize.plot_farm(aFarm, list_of_cattle, show=True)


    def test_run_session_plot_out(self):
        """This method demonstrates and displays the model running."""
        modelobj = model.Model(init_extra_weight=590.0)
        modelobj._run_session_plot_out(num_days=60)




#------------------------------- Main Program ---------------------------------
#
# Set variable run_verbose to True or False, depending on what I want to do 
# i.e. verbose testing or not verbose testing).

if __name__ == "__main__":
    import unittest
    class TheseTests( unittest.TestCase, Tests ):  pass
    run_verbose = True          #- Set this to control verbosity
    run_verbose = False         #- Set this to control verbosity
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TheseTests))
    if run_verbose:
        unittest.TextTestRunner(verbosity=2).run(suite)
    else:
        unittest.TextTestRunner(verbosity=1).run(suite)




# ===== end file =====

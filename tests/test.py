#!/usr/bin/python -tt
#==============================================================================
#                            General Documentation

"""Unittest for the ab_cattle package.

   Execution of this file:
   $ python test.py

   from the tests directory will execute all tests.  Class definition of 
   tests of sub-units of the package are in test_*.py modules.
"""

#------------------------------------------------------------------------------
#                           Additional Documentation
#
# RCS Revision Code:
#   $Id: test.py 64 2008-11-13 18:47:45Z jlin $
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
import unittest
from ab_cattle import cattle
from ab_cattle import model
import test_cattle
import test_model
import test_pkg_init
import test_visualize




#----------------- Set Up Class for All Tests of the Package ------------------

class SetUpTest(unittest.TestCase):
    """Set up data common for all tests of the package.
    """
    def setUp(self):
        self.string_test = "Hello there"
        self.modelobj = model.Model()
        self.cattleobj = cattle.Cattle()




#------------------------------------ Tests -----------------------------------

class Tests(object):
    """Tests of the SetUpTest class.
    """
    def test_SetUpTest_string_test(self):
        self.failUnless( self.string_test == "Hello there" )




#---------------------------- Actual Test Classes -----------------------------
#
# These are the classes that are added to the TestSuite.  These class
# definitions show multiple inheritance and ensures every class of
# Tests has the same setUp method.

class SetUpTestTests( SetUpTest, Tests ):  pass
class CattleTests( SetUpTest, test_cattle.Tests ):  pass
class ModelTests( SetUpTest, test_model.Tests ):  pass
class PkgInitTests( SetUpTest, test_pkg_init.Tests ):  pass
class VisualizeTests( SetUpTest, test_visualize.Tests ):  pass




#------------------------------- Main Program ---------------------------------
#
# Set variable run_verbose to True or False, depending on what I want to do 
# i.e. verbose testing or not verbose testing).

if __name__ == "__main__":
    run_verbose = True          #- Set this to control verbosity
    run_verbose = False         #- Set this to control verbosity
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(SetUpTestTests))
    suite.addTest(unittest.makeSuite(CattleTests))
    suite.addTest(unittest.makeSuite(ModelTests))
    suite.addTest(unittest.makeSuite(PkgInitTests))
    suite.addTest(unittest.makeSuite(VisualizeTests))
    if run_verbose:
        unittest.TextTestRunner(verbosity=2).run(suite)
    else:
        unittest.TextTestRunner(verbosity=1).run(suite)




# ===== end file =====

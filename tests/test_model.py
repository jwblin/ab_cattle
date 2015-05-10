#!/usr/bin/python -tt
#==============================================================================
#                            General Documentation

"""Define tests for unittest for module model in the ab_cattle package.

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
from ab_cattle.model import Model




#------------------------------------ Tests -----------------------------------

class Tests(object):
    def divide_by_two(self, a):
        """Tries to divide a by 2.0.
        """
        return a / 2.0

    def test_method_init(self):
        self.failUnless( self.modelobj._string_test == "Hello there" )

    def test_method_init_error(self):
        self.failUnlessRaises( TypeError, 
            self.divide_by_two, self.modelobj._string_test )

#@@@comment out for now
#    def test_run_session_print_out(self):
#        modelobj = Model(init_extra_weight=590.0)
#        modelobj._run_session_print_out(num_days=1)
#
#    def test_run_session(self):
#        try:
#            self.modelobj.run_session(num_days=1)
#        except:
#            self.fail("Run session failed")




# ===== end file =====

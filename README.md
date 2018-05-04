# ab_cattle
Agent-based model cattle and disease model from Shiflet &amp; Shiflet (2014).

This branch is the full solution to the model using an object-oriented
framework but with the bodies of the following methods mostly removed:

* abattoir.py:  feed_cattle, move_cattle
* cattle.py:  isNextToInfected, sir, update
* farm.py:  feed_cattle, move_cattle
* feedlot.py:  feed_cattle, move_cattle

The model has been tested on Python 2.7 and 3.4.  It should work on
Python 3.x.

I HACKED THIS QUICKLY SO IT MAY NOT GIVE CORRECT RESULTS.  It's also
something of a resource hog.  It's main purpose is to illustrate an
object-oriented programming decomposed model.

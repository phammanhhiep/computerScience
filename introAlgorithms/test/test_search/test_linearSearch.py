import sys, os
sys.path.insert (0, os.path.abspath ('./'))

import pytest
from search.linearSearch import linear_search

def test_linear_search ():
	s = [4,1,6,7,7,10,20]
	expected_i = 5
	val = 10
	i = linear_search (s, val)
	assert i == expected_i
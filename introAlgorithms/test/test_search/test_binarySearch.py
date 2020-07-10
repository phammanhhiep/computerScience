import sys, os
sys.path.insert (0, os.path.abspath ('./'))

import pytest
from search.binarySearch import binary_search, _binary_search

# @pytest.mark.skip
def test_binary_search ():
	'''
	Test: sequence has odd number of elements
	'''
	s = [1,10,30,5,40]
	val = 30
	i = 3
	j = binary_search (s, val)

	assert i == j

# @pytest.mark.skip	
def test_binary_search2 ():
	'''
	Test: sequence has even number of elements
	'''
	s = [1,10,11,30,5,40]
	val = 30
	i = 4
	j = binary_search (s, val)

	assert i == j	

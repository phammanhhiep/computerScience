import sys, os
sys.path.insert (0, os.path.abspath ('./'))

import pytest
from sort.selectionSort import selection_sort

def test_selection_sort ():
	s = [4,1,6,7,2,2,10]
	expected_s = [1,2,2,4,6,7,10]
	s = selection_sort (s)
	print (s)
	assert len (s) == len (expected_s)
	for i in range (len (s)):
		assert s[i] == expected_s[i]
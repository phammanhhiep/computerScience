import sys, os
sys.path.insert (0, os.path.abspath ('./'))

import pytest
from sort.bubbleSort import bubble_sort

def test_bubble_sort ():
	s = [9,7,8,1,2,5,4,10]
	e = [1,2,4,5,7,8,9,10]
	bubble_sort (s)
	
	assert len (s) == len (e)
	for i in range (len (s)):
		assert s[i] == e[i]


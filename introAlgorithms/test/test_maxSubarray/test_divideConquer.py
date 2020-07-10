import os, sys
sys.path.insert (0, os.path.abspath ('./'))

from maxSubarray.divideConquer import find_max_subarray, find_max_crossing_subarray
import pytest

@pytest.mark.skip
def test_find_max_crossing_subarray ():
	s = [1,-5,-1,3,-10,2,4]
	max_val, start, end = find_max_crossing_subarray (s,0,3,6)

	assert max_val == -1
	assert start == 3
	assert end == 6 

# @pytest.mark.skip
def test_find_max_subarray ():
	s = [12,-3,-10,15,4,-7,-2,15,4,-2]
	max_val, start, end = find_max_subarray (s,0,len (s)-1)

	assert max_val == 29
	assert start == 3
	assert end == 8
import os, sys
sys.path.insert (0, os.path.abspath ('./'))

from maxSubarray.iterateSubarrays import find_max_subarray
import pytest

# @pytest.mark.skip
def test_find_max_subarray ():
	s = [12,-3,-10,15,4,-7,-2,15,4,-2]
	max_val, start, end = find_max_subarray (s)

	assert max_val == 29
	assert start == 3
	assert end == 8

import sys, os
sys.path.insert (0, os.path.abspath ('./'))

import pytest
from sort.insertionSort import insertion_sort, rev_insertion_sort, recursive_insertion_sort

@pytest.mark.skip
def test_insertion_sort ():
	s = [4,1,6,7,2,2,10]
	expected_s = [1,2,2,4,6,7,10]
	insertion_sort (s)

	assert len (s) == len (expected_s)
	for i in range (len (s)):
		assert s[i] == expected_s[i]

@pytest.mark.skip
def test_rev_insertion_sort ():
	s = [4,1,6,7,2,2,10]
	expected_s = [10,7,6,4,2,2,1]
	rev_insertion_sort (s)

	assert len (s) == len (expected_s)
	for i in range (len (s)):
		assert s[i] == expected_s[i]

# @pytest.mark.skip
def test_recursive_insertion_sort ():
	s = [4,1,6,7,2,2,10]
	expected_s = [1,2,2,4,6,7,10]
	recursive_insertion_sort (s)

	assert len (s) == len (expected_s)
	for i in range (len (s)):
		assert s[i] == expected_s[i]	
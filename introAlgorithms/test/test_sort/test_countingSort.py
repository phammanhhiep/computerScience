import os, sys
sys.path.insert (0, os.path.abspath ('./'))

from sort.countingSort import counting_sort
import pytest

def test_counting_sort ():
	A = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
	k = 7
	B = [None] * len (A) 
	counting_sort (A, B, k)

	E = [0, 0, 1, 1, 2, 2, 3, 3, 4, 6, 6]

	assert len (B) == len (E)
	for i in range (len (B)):
		assert B[i] == E[i]

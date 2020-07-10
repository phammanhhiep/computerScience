import sys, os
sys.path.insert (0, os.path.abspath ('./'))

import pytest
from sort.mergeSort import merge, merge_sort

@pytest.mark.skip
def test_merge ():
	'''
	Test: merge sequences with the same lengths
	'''	
	A = [1,3,10,20,2,5,9,19]
	exp = [1,2,3,5,9,10,19,20]
	merge (A,0,3,len (A)-1)

	assert len (exp) == len (A)
	for i in range (len (exp)):
		assert exp[i] == A[i]

@pytest.mark.skip
def test_merge2 ():
	'''
	Test: merge sequences with different lengths
	'''
	A = [1,3,10,20,2,5,9,19,20,21,22]
	exp = [1,2,3,5,9,10,19,20,20,21,22]
	merge (A,0,3,len (A)-1)

	assert len (exp) == len (A)
	for i in range (len (exp)):
		assert exp[i] == A[i]


@pytest.mark.skip
def test_merge_sort ():
	'''
	Test: sort sequence with length of even value 
	'''
	A = [1,3,10,20,2,5,9,19]
	exp = [1,2,3,5,9,10,19,20]
	merge_sort (A,0,len (A)-1)

	assert len (exp) == len (A)
	for i in range (len (exp)):
		assert exp[i] == A[i]

@pytest.mark.skip
def test_merge_sort2 ():
	'''
	Test: sort sequence with length of odd value 
	'''
	A = [1,3,10,20,2,5,19,20,9,22,21]
	exp = [1,2,3,5,9,10,19,20,20,21,22]
	merge_sort (A,0,len (A)-1)

	assert len (exp) == len (A)
	for i in range (len (exp)):
		assert exp[i] == A[i]	


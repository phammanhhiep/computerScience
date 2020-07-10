import os, sys
sys.path.insert (0, os.path.abspath ('./'))

from sort.heapSort import max_heapify, max_heapify2, min_heapify, build_max_heap, heap_sort
import pytest

@pytest.mark.skip
def test_max_heapify ():
	a = [27,17,3,16,13,10,1,5,7,12,4,8,9,0]
	e = [27,17,10,16,13,9,1,5,7,12,4,8,3,0]
	max_heapify (a,2)

	assert len (a) == len (e)
	for i in range (len (a)):
		assert a[i] == e[i]

	a = [9, 22, 19, 10, 3, 17, 6, 5]
	e = [22, 10, 19, 9, 3, 17, 6, 5]
	
	max_heapify (a,0)

	assert len (a) == len (e)
	for i in range (len (a)):
		assert a[i] == e[i]	

@pytest.mark.skip
def test_max_heapify2 ():
	a = [27,17,3,16,13,10,1,5,7,12,4,8,9,0]
	e = [27,17,10,16,13,9,1,5,7,12,4,8,3,0]
	max_heapify2 (a,2)

	assert len (a) == len (e)
	for i in range (len (a)):
		assert a[i] == e[i]

@pytest.mark.skip
def test_min_heapify ():
	a = [0,5,6,3,7,15,14,4,9,11,10]
	e = [0,3,6,4,7,15,14,5,9,11,10]
	min_heapify (a,1)

	assert len (a) == len (e)
	for i in range (len (a)):
		assert a[i] == e[i]

@pytest.mark.skip
def test_build_max_heap ():
	a = [5, 3, 17, 10, 84, 19, 6, 22, 9]
	e = [84, 22, 19, 10, 3, 17, 6, 5, 9]
	build_max_heap (a)

	assert len (a) == len (e)
	for i in range (len (a)):
		assert a[i] == e[i]	

# @pytest.mark.skip
def test_heap_sort ():
	a = [5,3,17,10,84,19,6,22,9]
	e = [3,5,6,9,10,17,19,22,84]
	a = heap_sort (a)
	
	assert len (a) == len (e)
	for i in range (len (a)):
		assert a[i] == e[i]		
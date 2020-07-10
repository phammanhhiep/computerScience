import os, sys, math
sys.path.insert (0, os.path.abspath ('./'))

from sort.mergeSort import merge_sort

def _binary_search (s, val, p, q):
	i = None
	if p < q:
		j = math.floor ((q - p) / 2) + p
		if s[j] > val:
			i = _binary_search (s, val, p, j-1)
		elif s[j] < val:
			i = _binary_search (s, val, j+1, q)
		else:
			i = j
	else:
		if s[p] == val:
			i = p
	return i

def binary_search (s, val):
	n = len (s)
	merge_sort (s, 0, len (s)-1) # n*log2(n)
	return _binary_search (s, val, 0, n) # log2(n)


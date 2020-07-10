# Max heap sort
import math

def heap_sort (A):
	build_max_heap (A)
	n = len (A)
	temp = A[n-1]
	A[n-1] = A[0]
	A[0] = temp 
	for i in range (n-2):
		last_index = n-i-1
		curA = A[:last_index]
		max_heapify (curA, 0)
		A = curA + A[last_index:]
		temp = A[last_index-1]
		A[last_index-1] = A[0]
		A[0] = temp
	return A

def right (i):
	return ((i + 1) * 2)

def left (i):
	return ((i + 1) * 2) - 1

def parent (i):
	return math.ceil (i / 2 - 1)

def build_max_heap (A):
	n = len (A)
	h = math.floor (math.log (n, 2))
	for i in range (2^h - 2, -1, -1):
		max_heapify (A, i)

def max_heapify (A, i):
	'''	
	Recursive version.
	'''
	maxi = i
	n = len (A)
	li = left (i)
	ri = right (i)
	# print (A, len (A), i, li, ri)
	pval = A[i]
	maxval = pval
	if li < n:
		lval = A[li]
		if maxval < lval:
			maxi = li
			maxval = lval
	if ri < n:
		rval = A[ri]
		if maxval < rval:
			maxi = ri
			maxval = rval
	if i != maxi:
		A[maxi] = pval
		A[i] = maxval
		if left (maxi) < len (A):
			max_heapify (A, maxi)

def max_heapify2 (A, i):
	'''
	For-loop version
	'''
	maxi = None
	while (maxi is not None and left (maxi) < len (A)) or maxi is None:
		maxi = i
		pval = A[i]
		maxval = pval
		li = left (i)
		ri = right (i)
		lval = A[li]
		rval = A[ri]
		if maxval < lval:
			maxi = li
			maxval = lval
		if maxval < rval:
			maxi = ri
			maxval = rval
		if i != maxi:
			A[maxi] = pval
			A[i] = maxval
			i = maxi
		else:
			break	

def min_heapify (A, i):
	mini = i
	li = left (i)
	ri = right (i)
	lval = A[li]
	rval = A[ri]
	pval = A[i]
	minval = pval

	if minval > lval:
		mini = li
		minval = lval
	if minval > rval:
		mini = ri
		minval = rval
	if mini != i:
		A[i] = minval
		A[mini] = pval
		if left (mini) < len (A):
			min_heapify (A, mini)

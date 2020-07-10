import math

def merge (A,p,q,r):
	'''
	a,b are two sorted sequence in ascending order.
	The function compares two smallest value which is not select and add the 
	smaller to a result list. 
	Repeat the process until one of two empty. 
	Then add the remaining of unempty sequence to the result. 
	'''
	i = 0
	j = 0
	L = A[p:q+1]
	R = A[q+1:r+1]
	l = len (L)
	r = len (R)
	for k in range (r+l):
		if (i < l and j < r and L[i] <= R[j]) or (i < l and j == r):
			A[p + k] = L[i]
			i += 1
		elif (i < l and j < r and L[i] > R[j]) or (i == l and j < r):
			A[p + k] = R[j]
			j += 1
			
def merge_sort (A,p,r):
	if p < r:
		q = math.floor ((p + r) / 2)
		merge_sort (A,p,q)
		merge_sort (A,q+1,r)
		merge (A,p,q,r)
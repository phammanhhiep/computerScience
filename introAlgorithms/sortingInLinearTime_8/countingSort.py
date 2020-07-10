def counting_sort (A, B, k):
	'''
	Naive implementation of counting sort. Assume the following
		-- k = (max (A) - 1). Because index of an array C start from 0 to (max (A) - 1).
			Using build a heap and then find max take Big-O of (n). And thus doing so does not 
			change the asymptotical running time of the algorithm.
	'''
	C = [0] * k
	n = len (A)
	for i in range (n):
		C[A[i]] += 1
	for i in range (1,k):
		C[i] += C[i-1]
	for i in range (n-1, -1, -1):
		B[C[A[i]] - 1] = A[i]
		C[A[i]] -= 1
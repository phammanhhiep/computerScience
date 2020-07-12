def find_max_subarray (s):
	'''
	Brute-force. Iterate all subarrays and return a max subarray index and its value.
	'''
	n = len (s)
	cur_sum = None
	max_sum = None
	max_start = None
	max_end = None
	for i in range (n-1):
		for j in range (i, n):
			cur_sum = sum (s[i:j+1])
			if max_sum is None or max_sum < cur_sum:
				max_sum = cur_sum
				max_start = i
				max_end = j
	return max_sum, max_start, max_end	
def selection_sort (s=None):
	if s is None: 
		raise Exception ('No sequence is provided!')
	n = len (s)
	for curr_index in range (n-1): # c1 * n
		min_ele = s[curr_index] # c2 * (n-1)
		min_index = curr_index # c3 * (n-1)
		for j in range (curr_index + 1, n): # c4 * SUM (tj) | tj = [2,...,n+1]
			if min_ele > s[j]: # c5 * SUM (tj - 1)
				min_ele = s[j] # c6 * SUM (tj - 1)
				min_index = j # c7 * SUM (tj - 1)
		_temp = s[curr_index]  # c8 * (n-1)
		s[curr_index] = min_ele # c9 * (n-1)
		s[min_index] = _temp # c10 * (n-1)
	return s

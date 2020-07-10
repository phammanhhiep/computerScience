def insertion_sort (s=None):
	'''
	Return sequence in ascending order
	'''	
	if s is None:
		raise Exception ('No sequence is provided!')

	snum = len (s)
	for i in range (1, snum):
		curr_ele = s[i]
		j = i - 1
		while j >= 0 and s[j] > curr_ele:
			s[j+1] = s[j]
			j -= 1
		s[j+1] = curr_ele

def rev_insertion_sort (s=None):
	'''
	Return sequence in decending order
	'''
	if s is None:
		raise Exception ('No sequence is provided!')
	snum = len (s)
	for i in range (snum-1,-1,-1):
		curr_ele = s[i]
		j = i + 1
		while j < snum and s[j] > curr_ele:
			s[j-1] = s[j]
			j += 1
		s[j-1] = curr_ele

def recursive_insertion_sort (s=None, i=None):
	if i is None or i >= 0:
		i = (i - 1) if i is not None else len (s) - 1
		recursive_insertion_sort (s,i)		
		curr_ele = s[i]
		j = i - 1
		while j >= 0 and s[j] > curr_ele:
			s[j+1] = s[j]
			j -= 1
		s[j+1] = curr_ele	
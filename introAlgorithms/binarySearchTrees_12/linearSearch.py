def linear_search (s, val):
	n = len (s)
	vi = None
	for i in range (n):
		if val == s[i]:
			vi = i
			break
	return vi
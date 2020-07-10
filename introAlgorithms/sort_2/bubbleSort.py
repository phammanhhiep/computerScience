def bubble_sort (s):
	n = len (s)
	for i in range (n-1): # n
		for j in range (n-1, i, -1): # sum (t) | t = [1,2,...,n-1]
			if s[j] < s[j-1]: # sum (t-1)
				temp = s[j-1] # sum (t-2)
				s[j-1] = s[j] 
				s[j] = temp

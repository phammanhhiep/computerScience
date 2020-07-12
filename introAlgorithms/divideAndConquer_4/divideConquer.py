import math

def find_max_subarray (s, start, end):
	if start == end:
		return s[start], start, end
	else:
		mid_index = start + math.floor ((end-start)/2)
		left_max, left_start, left_end = find_max_subarray (s, start, mid_index)
		right_max, right_start, right_end = find_max_subarray (s, mid_index+1, end)	
		cross_max, cross_start, cross_end = find_max_crossing_subarray (s, start, mid_index, end)

		if left_max > right_max and left_max > cross_max:
			return left_max, left_start, left_end
		elif right_max > left_max and right_max > cross_max:
			return right_max, right_start, right_end
		else:
			return cross_max, cross_start, cross_end


def find_max_crossing_subarray (s, start, mid, end):
	'''
	Find the maximum subarray in the left and that in the right and then combine.
	Return the maximum value and the subarray indexes.
	'''
	max_left = None
	max_right = None
	sum_left = 0
	sum_right = 0
	start_left = None
	end_left = None
	for i in range (mid, start-1, -1):
		sum_left += s[i]
		if max_left is None or max_left < sum_left:
			max_left = sum_left
			start_left = i

	for i in range (mid+1, end+1):
		sum_right += s[i]
		if max_right is None or max_right < sum_right:
			max_right = sum_right
			end_left = i

	return (max_right + max_left), start_left, end_left
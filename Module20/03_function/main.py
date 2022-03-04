def slice_tuple(tuple, elem):
	start = 0
	end = len(tuple)
	for index, el in enumerate(tuple):
		if el == elem and start == 0:
			start = index
		elif el == elem:
			end = index
			break
	return tuple[start:end + 1]


T = (1, 'h', 2, 3, 4, 'h', 5, 'j', 7, 23, 34, 'j')

print(slice_tuple(T, 'h'))

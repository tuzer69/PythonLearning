def sort_tuple(tpl):
	lst = list(tpl)
	for i_num in tpl:
		if not isinstance(i_num, int):
			return tpl
	lst.sort()
	return tuple(lst)


numbers = (3, 4, 6, 34, 2, 5, 8, 12, 21, 1, 7, 18, 19)

print(sort_tuple(numbers))

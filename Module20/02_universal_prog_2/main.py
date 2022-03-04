def to_list(iterable):
	lst = []
	for i_index, i_item in enumerate(iterable):
		if is_prime(i_index):
			lst.append(i_item)
	return lst


def is_prime(number):
	k = 0
	for i in range(2, number // 2 + 1):
		if number % i == 0:
			k = k + 1
	if k <= 0:
		return True
	else:
		return False

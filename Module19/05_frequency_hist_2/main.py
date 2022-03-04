orig_dict = {' ': 2, '-': 1, 'З': 1, 'а': 2, 'д': 1, 'е': 1, 'и': 1, 'н': 2, 'о': 3, 'п': 1, 'с': 2, 'т': 2, 'ч': 1, 'ь': 1}


def invert_hist(dic):
	sym_dict = dict()
	for i_item in dic.keys():
		sym_dict[dic.get(i_item)] = [i for i in dic.keys() if dic.get(i) == dic.get(i_item)]
	return sym_dict


invert = invert_hist(orig_dict)
for i_item in range(1, len(invert) + 1):
	print(i_item, invert[i_item])


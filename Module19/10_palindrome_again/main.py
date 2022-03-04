def is_palindrome(string):
	sym_dict = {}
	odd = 0
	for i_sym in string:
		if sym_dict.get(i_sym, {}):
			sym_dict[i_sym] += 1
		else:
			sym_dict[i_sym] = 1
	for i_sym in sym_dict.values():
		if i_sym % 2 != 0:
			odd += 1
	return odd <= 1

N = input('Введите строку: ')
if is_palindrome(N):
	print('Можно сделать палиндромом')
else:
	print('Нельзя сделать палиндромом')

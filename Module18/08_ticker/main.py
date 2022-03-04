def shift(string1, string2):
	for i_sym in range(len(string1)):
		if string1[i_sym:] + string1[:i_sym] == string2:
			return i_sym
	return -1


result = shift(input("Первая строка: "), input("Вторая строка: "))
if result != -1:
	print("Первая строка получается из второй со сдвигом", result)
else:
	print("Первую строку нельзя получить из второй с помощью циклического сдвига.")

def fibonachi(position):
	cur = 1
	if position > 2:
		cur = fibonachi(position - 1) + fibonachi(position - 2)
	return cur


N = int(input('Введите позицию числа в ряде Фибоначчи: '))
print('Число:', fibonachi(N))

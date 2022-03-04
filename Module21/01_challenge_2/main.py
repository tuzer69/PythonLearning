def print_num(N):
	if N == 0:
		return
	print_num(N - 1)
	print(N, end=' ')


N = int(input('Введите число: '))
print_num(N)

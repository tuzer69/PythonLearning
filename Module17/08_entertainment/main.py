N = int(input("Кол-во палок: "))
K = int(input("Кол-во бросков: "))
game = [x for x in range(1, N + 1)]

for i_ in range(K):
	print("Бросок", i_ + 1, ".Сбиты палки с номера ", end='')
	start = int(input())
	while start <= 1 or start > N:
		print("Номер палки должен быть в диапазоне от 2 до ", N)
		start = int(input("Сбиты палки с номера "))
	print("по номер ", end='')
	end = int(input())
	while end <= start or end > N:
		print("Номер палки должен быть в диапазоне от,", start, "до ", N)
		print("по номер ", end='')
		end = int(input())
	game = [game[i] if i not in range(start - 1, end) else 0 for i in range(len(game))]
result = [('|' if game[x] > 0 else '.') for x in range(len(game))]

print("Результат: ", end='')
for i in range(len(result)):
	print(result[i], end='')

N = int(input('Сколько записей вносится в протокол? '))
print('Записи (результат и имя):')
tournament = []
record = ''

for i_num in range(1, N + 1):
	print(i_num, 'запись: ', end='')
	record = input().split()
	tournament.append((record[1], int(record[0])))

index = 0
winners = []
while index < 3:
	last_game = ('', 0)
	for i_game in tournament:
		if i_game[1] > last_game[1] and not i_game[0] in winners:
			last_game = i_game
	print(index + 1, ' место ', last_game[0], ' (', last_game[1], ')', sep='')
	winners.append(last_game[0])
	tournament.remove(last_game)
	index += 1


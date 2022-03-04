import random

summa = 0
while summa <= 777:
	number = 0
	try:
		number = int(input('Введите число: '))
	except ValueError:
		print('Неверно введено значение')
	summa += number
	try:
		if random.randint(1, 13) == 5:
			raise BaseException()
		with open('result.txt', 'a', encoding='utf-8') as res_f:
			res_f.write(str(number) + '\n')
	except BaseException:
		print('Аварийное завершение работы программы')
		break

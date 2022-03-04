import random

N = int(input('Введите максимальное число: '))
rnd_numbers = {'help': [random.randint(1, N + 1) for _ in range(1, 4)]}
answer = ""
while answer != rnd_numbers.get('help', {})[0]:
	print('\nНужное число есть среди вот этих чисел: ', end='')
	answer = input()
	tmp = answer.split()
	if answer == str(rnd_numbers['help'][0]):
		print('Вы угадали!')
		break
	elif answer == 'Помогите!':
		print('Артём мог загадать следующие числа: ', end=' ')
		for i_num in rnd_numbers.get('help', {}):
			print(i_num, end=' ')
	for i_answer in range(len(tmp)):
		if int(tmp[i_answer]) == rnd_numbers['help'][0]:
			tmp = int(tmp[i_answer])
			break
	if tmp == rnd_numbers['help'][0]:
		print('Да')
	else:
		print('Нет')


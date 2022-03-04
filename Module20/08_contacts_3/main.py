phonebook = {}
f_name = ''
s_name = ''
phone = 0
while True:
	print('Выберите действие:'
		   '\n\t1-Добавить контакт\n\t2-Поиск человека по фамилии\n')
	n = int(input())
	if n == 1:
		f_name = input('Введите имя: ')
		s_name = input('Введите фамилию: ')
		for i_item in phonebook.keys():
			while f_name in i_item and s_name in i_item:
				print('Такой человек уже есть! Попробуйте еще раз')
				f_name = input('Введите имя: ')
				s_name = input('Введите фамилию: ')
		phone = int(input('Введите номер телефона: '))
		phonebook[(f_name + ' ' + s_name)] = phone
		print('*' * 30)
		for i_user, i_phone in phonebook.items():
			print(i_user, i_phone)
		print('*' * 30)
	elif n == 2:
		s_name = input('Введите фамилию: ').lower()
		for i_user, i_phone in phonebook.items():
			if s_name in i_user.lower():
				print(i_user, i_phone)
		print('*' * 30)
	else:
		print('Выберите номер 1 или 2\n')
		continue

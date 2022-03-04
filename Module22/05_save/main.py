import os


def check_path():
	path = ''
	while not os.path.exists(path):
		print('Куда хотите сохранить файл? '
		  'Введите последовательность папок (через пробел): ')
		pth = input().split()
		for i_elem in pth:
			path = os.path.join(path, i_elem)
		if not os.path.exists(path):
			print('Такого пути не существует!!!. Попробуйте еще раз\n')
	return path


def check_file(path, f_name):
	if os.path.exists(os.path.join(path, f_name)):
		return True
	else:
		return False


def write_file(path, file_name, text):
	with open(os.path.join(path, file_name), 'w', encoding='utf-8') as f:
		f.write(text)
		print('Файл успешно перезаписан!')


def save_file(path, text):
	print('Введите имя файла: ', end='')
	f_name = input() + '.txt'
	if check_file(path, f_name):
		print('Вы действительно хотите перезаписать файл?: ', end='')
		answer = input().lower()
		if answer == 'да':
			write_file(path, f_name, text)
			return
		else:
			print('Введите имя файла: ', end='')
			f_name = input() + '.txt'
			write_file(path, f_name, text)
			return
	else:
		write_file(path, f_name, text)
		return


text = input('Введите строку: ')
pth = check_path()
save_file(pth, text)

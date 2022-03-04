import os


def get_size(pth, file):
	if os.path.isfile(os.path.join(pth, file)):
		return os.path.getsize(os.path.join(pth, file))
	else:
		result = 0
		for i_itemm in os.listdir(os.path.join(pth, file)):
			result += get_size(os.path.join(pth, file), i_itemm)
		return result


def get_files(pth):
	if os.path.isfile(os.path.abspath(pth)):
		return 1
	else:
		result = 0
		for i_itemm in os.listdir(os.path.abspath(pth)):
			result += get_files(os.path.abspath(os.path.join(pth, i_itemm)))
	return result



def get_dir(pth):
	result = 0
	for i_itemm in os.listdir(pth):
		if os.path.isdir(os.path.join(pth, i_itemm)):
			result += get_dir(os.path.join(pth, i_itemm))
			result += 1
	return result


path = input('Введите путь: ')

weight = 0
for i_item in os.listdir(path):
	weight += get_size(path, i_item)
print('Размер каталога (в Кб):', round(weight / 1024, 2))
print('Количество файлов:', get_files(path))
print('Количество подкаталогов:', get_dir(path))

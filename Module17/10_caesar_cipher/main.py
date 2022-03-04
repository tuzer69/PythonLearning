def crypt(string, shift):
	char_list = [(alphabet[(alphabet.index(sym) + shift) % 33] if sym != ' ' else ' ') for sym in string]
	new_str = ''
	for i_char in char_list:
		new_str += i_char
	return new_str

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

string = input("Введиете строку: ")
shift = int(input("Введите сдвиг: "))

out_str = crypt(string, shift)
print("Зашифрованная строка: ", out_str)
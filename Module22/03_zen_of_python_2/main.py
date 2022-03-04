import os

word_count = 0
line_count = 0
sym_count = 0
min_sym = ''
sym_dict = {}

with open('zen.txt', 'r', encoding='utf-8') as zen_file:
	for i_line in zen_file:
		for i_word in i_line.split():
			for i_sym in i_word:
				if i_sym.isascii():
					sym_count += 1
					if sym_dict.get(i_sym, {}):
						sym_dict[i_sym] += 1
					else:
						sym_dict[i_sym] = 1
			if len(i_word) > 1:
				word_count += 1
		line_count += 1

min_count = 1
for i_sym, i_count in sym_dict.items():
	if i_count <= min_count and i_sym.isalpha():
		min_sym = i_sym
print('Количество строк:', line_count)
print('Количество слов:', word_count)
print('Количество букв:', sym_count)
print('Наименее встречаемый символ:', min_sym)

with open('cipher_text.txt', 'w', encoding='utf-8') as fwrite:
	with open('text.txt', 'r', encoding='utf-8') as fread:
		num_line = 1
		for i_line in fread:
			tmp_line = ''
			for i_sym in i_line:
				if i_sym == '\n':
					continue
				tmp_line += chr(ord(i_sym) + num_line)
			fwrite.write(tmp_line + '\n')
			num_line += 1


print('Содержимое файла text.txt:')
with open('text.txt', 'r', encoding='utf-8') as f:
	print(f.read() + '\n')

print('Содержимое файла cipher_text.txt:')
with open('cipher_text.txt', 'r', encoding='utf-8') as f:
	print(f.read())

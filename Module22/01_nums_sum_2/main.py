import os

file_r = open('numbers.txt', 'r', encoding='utf-8')
summa = 0

for i_line in file_r:
	if i_line.strip().isdigit():
		summa += int(i_line.strip())
file_r.close()

file_w = open('answer.txt', 'w', encoding='utf-8')
file_w.write(str(summa))
file_w.close()

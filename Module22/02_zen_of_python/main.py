zen_file = open('zen.txt', 'r', encoding='utf-8')
new_zen = open('new_zen.txt', 'w', encoding='utf-8')

for i_line in reversed(zen_file.readlines()):
	new_zen.write(i_line)

zen_file.close()
new_zen.close()

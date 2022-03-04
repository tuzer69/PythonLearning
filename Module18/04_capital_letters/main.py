string = input("Введите строку: ")
str_list = string.split()

for i_word in range(len(str_list)):
	str_list[i_word] = str_list[i_word][0].upper() + str_list[i_word][1:]
print("Результат:", " ".join(str_list))
def chek_sym(word, black_list):
	for i_sim in range(len(black_list)):
		if name[i_sim] == black_list[i_sim]:
			return True
	return False


name = input("Название файла: ")
stop_list = list("@№$%^&*()")

if chek_sym(name, stop_list):
	print("Ошибка: название начинается на один из специальных символов")
elif (not name.endswith(".txt")) and (not name.endswith(".docx")):
	print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx")
else:
	print("Файл назван верно")


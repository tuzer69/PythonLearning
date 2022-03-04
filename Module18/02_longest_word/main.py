text = input("Введите строку: ")
words = text.split()
max_word = ""
for i_item in range(len(words)):
	if len(words[i_item]) > len(max_word):
		max_word = words[i_item]

print("\nСамое длинное слово:", max_word, "\nЕго длинна:", len(max_word))

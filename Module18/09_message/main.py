N = input("Сообщение: ")
mess_list = N.split()
new_list = []
for i_item in mess_list:
	word = ""
	for i_word in range(len(i_item)):
		if not i_item[i_word].isalpha():
			word += i_item[:i_word - 1:-1]
			word += i_item[i_word]
		else:
			word = i_item[i_word] + word

new_list.append(word)
print(" ".join(new_list))



user_text = input('Сообщение: ').split()
for index, word in enumerate(user_text):
    if word.isalpha():
        user_text[index] = word[::-1]
    else:
        for symbol in word:
            if not symbol.isalpha():
                pivot = word.index(symbol)
                user_text[index] = word[pivot - 1::-1] + symbol + word[-1:pivot:-1]

print('\nНовое сообщение:', ' '.join(user_text))

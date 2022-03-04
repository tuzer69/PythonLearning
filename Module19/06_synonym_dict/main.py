words = dict()
word = ""
N = int(input('Введите количество пар слов: '))

for i_word in range(1, N + 1):
	print(i_word, 'Пара: ', end='')
	word = input().split()
	words[word[2].lower()] = word[0]

for i_word in range(1, N + 1):
	word = input('Введите слово: ').lower()
	if words.get(word, {}):
		print('Синоним:', words.get(word))
	else:
		while not words.get(word, {}):
			print('Такого слова в словаре нет.')
			word = input('Введите слово: ').lower()
		print('Синоним:', words.get(word))



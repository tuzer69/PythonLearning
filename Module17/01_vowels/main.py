vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
text = input("Введите текст: ")
lst = [x for x in text if vowels.count(x) > 0]
print("Список гласных букв: ", lst)
print("Длина списка: ", len(lst))
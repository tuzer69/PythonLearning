def check_pal(word):
    w = list(word)
    for i in range(len(w)):
        if w[i] != w[-(i + 1)]:
            return True


word = input("Введите слово: ")
if check_pal(word):
    print("Слово не является палиндромом")
else:
    print("Слово является палиндромом")

# зачтено

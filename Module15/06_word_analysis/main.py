word = list(input("Введите слово: "))
u_count = 0
for i in range(len(word)):
    cnt = 0
    for n in word:
        if word[i] == n:
            cnt += 1
    if cnt < 2:
        u_count += 1
print("Кол-во уникальных букв: ", u_count)

# зачтено

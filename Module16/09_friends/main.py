N = int(input("Кол-во друзей: "))
K = int(input("Долговых расписок: "))
friends = []
for _i in range(N):
    friends.append([_i + 1, 0])
for _i in range(K):
    print(_i + 1, "расписка ")
    f1 = int(input("Кому: "))
    f2 = int(input("От кого: "))
    while f2 == f1:
        print("Ошибка! Друг не может дать деньги самому себе.")
        f2 = int(input("От кого: "))
    summa = int(input("Сколько: "))
    for i_f in friends:
        if i_f[0] == f1:
            i_f[1] -= summa
        elif i_f[0] == f2:
            i_f[1] += summa

print("Баланс друзей:")
for i_friend in friends:
    print(i_friend[0], ":", i_friend[1])

# зачетно

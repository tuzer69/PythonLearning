N = int(input("Кол-во человек: "))
K = int(input("Какое число в считалке? "))
people = list(range(1, N + 1))
print("Значит, выбывает каждый ", K, "человек")
index = 0
print()
while len(people) != 1:
    print("Текущий круг людей: ", people)
    print("Начало счёта с номера ", people[index])
    for _i in range(K - 1):
        if index == len(people) - 1:
            index = 0
        else:
            index += 1

    print("Выбывает человек под номером ", people[index])
    people.remove(people[index])
    if index == len(people):
        index = 0
    print()
print()
print("Остался человек под номером ", people[0])

# зачтено

skates = []
people = []
people_count = 0
N = int(input("Кол-во коньков: "))
for _i in range(N):
    print("Размер", _i + 1, "пары: ", end="")
    skates.append(int(input()))
K = int(input("Кол-во людей: "))
for _i in range(K):
    print("Размер ноги ", _i + 1, "человека: ", end="")
    people.append(int(input()))
for _i in people:
    if skates.count(_i) >= 1:
        people.remove(_i)
        people_count += 1
print("Наибольшее кол-во людей, которые могут взять ролики: ", people_count)

# зачтено

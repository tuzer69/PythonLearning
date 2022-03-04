count = int(input("Кол-во контейнеров: "))
containers = []
position = 0
last_weight = 200
for i in range(count):
    x = int(input("Введите вес контейнера: "))
    while x > last_weight:
        print("Масса не должен превышать: ", last_weight)
        x = int(input("Введите вес контейнера: "))
    last_weight = x
    containers.append(x)
print()
X = int(input("Введите вес нового контейнера: "))
for i in containers:
    position += 1
    if X == i:
        break
    else:
        position = len(containers) + 1
print()
print("Номер, куда встанет новый контейнер: ", position)


one = []
two = []
print("Введите первый список")
for i_item in range(3):
    print("Введите ", i_item + 1, "число: ", end="")
    one.append(int(input()))
print()
print("Введите второй список")
for i_item in range(7):
    print("Введите ", i_item + 1, "число: ", end="")
    two.append(int(input()))
print()
print("Первый список: ", one)
print("Первый список: ", two)
one.extend(two)
for i_item in one:
    while one.count(i_item) > 1:
        one.remove(i_item)
print()
print("Новый первый список с уникальными элементами: ", one)

# зачтено

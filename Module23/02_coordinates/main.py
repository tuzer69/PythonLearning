import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return round(x / y, 2)


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return round(y / x, 2)


try:
    with open('coordinates.txt', 'r') as file:
        for line in file:
            nums_list = line.split()
            try:
                res1 = f(int(nums_list[0]), int(nums_list[1]))
                res2 = f2(int(nums_list[0]), int(nums_list[1]))
            except ZeroDivisionError:
                print('Делить на ноль нельзя!')
            except IndexError:
                print('Отсутствует или неверно указано значение')
            number = random.randint(0, 100)
            with open('result.txt', 'a', encoding='utf-8') as file_2:
                my_list = sorted([res1, res2, number])
                file_2.write(' '.join(str(my_list) + '\n'))
except FileNotFoundError:
    print("Файл coordinates.txt не существует")
except TypeError:
    print('Файл coordinates.txt содержит неверный тип данных')

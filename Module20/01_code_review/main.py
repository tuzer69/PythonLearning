students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

# 2. Написать функцию, которая принимает в качестве аргумента словарь
# и возвращает два значения: полный список интересов всех студентов и
# общую длину всех фамилий студентов.
def f(dict):
    lst = []
    string = ''
    for i in dict:
        lst += (dict[i]['interests'])
        string += dict[i]['surname']
    return lst, len(string)


# 1. Вывести на экран список пар «ID студента — возраст».
for i_id in students.items():
    print(i_id[0], '—', i_id[1]['age'])

# 3. Далее в основном коде эта функция вызывается, и значения присваиваются
# отдельным переменным, которые после выводятся на экран.
# (Т.е. нужно распаковать все возвращаемые значения в отдельные переменные.
interest, famLong = f(students)
print(interest, famLong)

from operator import itemgetter
import random


def medium(lst):
    result = 0
    for i_item in lst:
        result += i_item
    return int(result / len(lst))


class Student:
    def __init__(self):
        self.FI = 'Name_' + str(random.randint(1, 99))
        self.GrNumber = random.randint(1, 5)
        self.Scores = [random.randint(3, 9) for _ in range(5)]


students = [Student() for _ in range(10)]
ball = {st.FI: medium(st.Scores) for st in students}

print('{0:10}{1:20}'.format('Cтудент', 'Средний балл'))
print('-' * 40)
for i_student in sorted(ball.items(), key=itemgetter(1), reverse=True):
    print('{0:10}{1:5}'.format(
        i_student[0], i_student[1]))
print('-' * 40)

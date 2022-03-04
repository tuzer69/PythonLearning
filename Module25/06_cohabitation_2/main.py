from Husband import Husband
from Wife import Wife
from home import Home
from Cat import Cat


home = Home()
one = Husband('Boris')
two = Wife('Elena')
cat = Cat('Barsik')
home.add_peoplе(one)
home.add_peoplе(two)
home.add_peoplе(cat)

for i_day in range(1, 366):
    print('-' * 30, '\n', 'Day is - ', i_day, '\n', '-' * 30, sep='')

    for i_man in home.people:
        if i_man.is_alive():
            print('Human is dead!')
            break

        print(i_man.name, '=========>')
        print('Запас еды в доме: ', i_man.house.food, '\n',
              'Запас счастья: ', i_man.happiness, '\n',
              'Запас денег: ', i_man.house.money, sep='')

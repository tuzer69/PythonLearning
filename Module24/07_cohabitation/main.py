import random
from human import Human
from home import Home


home = Home('TownHouse')
one = Human('Ken')
two = Human('Elen')
home.add_peopel(one)
home.add_peopel(two)
is_dead = False

for i_day in range(1, 366):
    num = random.randint(1, 6)
    print('-' * 30, '\n', 'Day is - ', i_day, '\n', '-' * 30, sep='')

    for i_man in home.people:
        if i_man.is_alive():
            if i_man.satiety < 20:
                i_man.work()
            elif i_man.house.food < 10:
                i_man.shopping()
            elif i_man.house.money < 50:
                i_man.work()
            elif num == 1:
                i_man.work()
            elif num == 2:
                i_man.eat()
            else:
                i_man.game()
        else:
            print('Human is dead!')
            break
        print(i_man.name, '=========>')
        print('Запас еды в доме: ', i_man.house.food, '\n',
              'Запас денег: ', i_man.house.money, sep='')

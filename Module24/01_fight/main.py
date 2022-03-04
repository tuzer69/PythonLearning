import random


class Unit:
    def __init__(self, name):
        self.health = 100
        self.name = name

    def damage(self, unit):
        if unit.health > 0:
            unit.health -= 20
            return True
        else:
            return False


U1 = Unit('ONE')
U2 = Unit('TWO')
units = [U1, U2]
winner = 0

while True:
    hit = random.randint(0, 1)
    if hit == 0 and units[hit].damage(units[1]):
        print('Атаковал юнит', units[hit].name,
              '\nУ противка осталось здоровья:', units[1].health)
        if units[1].health == 0: winner = hit
    elif hit == 1 and units[hit].damage(units[0]):
        print('Атаковал юнит', units[hit].name,
              '\nУ противка осталось здоровья:', units[0].health)
        if units[0].health == 0: winner = hit
    else:
        print('Игра окончена игрок', units[winner].name, 'победил')
        break

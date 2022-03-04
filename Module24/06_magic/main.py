class Water:
    def __add__(self, other):
        if type(other) == Air: return Answer('Вода + Воздух = Шторм')
        elif type(other) == Fire: return Answer('Вода + Огонь = Пар')
        elif type(other) == Groud: return Answer('Вода + Земля = Грязь')
        else: return Answer('')


class Air:
    def __add__(self, other):
        if type(other) == Fire: return Answer('Воздух + Огонь = Молния')
        elif type(other) == Groud: return Answer('Воздух + Земля = Пыль')
        elif type(other) == Water: return Answer('Вода + Воздух = Шторм')
        else: return Answer('')


class Fire:
    def __add__(self, other):
        if type(other) == Groud: return Answer('Огонь + Земля = Лава')
        elif type(other) == Air: return Answer('Воздух + Огонь = Молния')
        elif type(other) == Water: return Answer('Вода + Огонь = Пар')
        else: return Answer('')


class Groud:
    def __add__(self, other):
        if type(other) == Fire: return Answer('Огонь + Земля = Лава')
        elif type(other) == Air: return Answer('Воздух + Земля = Пыль')
        elif type(other) == Water:return Answer(' Вода + Земля = Грязь')
        else: return Answer('')


class Answer:
    def __init__(self, answer):
        if answer != '':
            self.answer = answer
        else:
            self.answer = None


a = Water()
b = Fire()
d = a + b
print(d.answer)

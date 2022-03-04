import random
from home import Home


class Cat:
    def __init__(self, name):
        self.name = name
        self.satiety = 30
        self.house = Home()
        self.happiness = 100

    def eat(self):
        r = random.randint(2, 10)
        self.satiety += r * 2
        self.house.cat_food -= r

    def tearing(self):
        self.house.dirt += 5

    def sleep(self):
        r = random.randint(3, 10)
        self.satiety -= r

    def is_alive(self):
        if self.satiety <= 0:
            return False
        if self.satiety < 20:
            self.eat()
            self.sleep()
        elif self.satiety < 10:
            self.tearing()


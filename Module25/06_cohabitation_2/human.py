import random

from home import Home


class Human:
    def __init__(self, name):
        self.name = name
        self.satiety = 30
        self.happiness = 100
        self.house = Home()

    def is_alive(self):
        if self.satiety <= 0 and self.happiness < 10:
            return False
        self.satiety -= 10
        self.house.dirt += 5
        if self.satiety < 20:
            self.eat()
        elif self.house.dirt > 90:
            self.happiness -= 10

    def eat(self):
        r = random.randint(10, 30)
        self.house.food -= r
        self.satiety += r

    def pet_cat(self):
        self.happiness += 5

    def work(self):
        self.house.money += 150

    def buy_coat(self):
        self.house.money -= 350

    def shopping(self):
        self.house.food += 10
        self.house.cat_food += 10
        self.house.money -= 10

    def clean(self):
        pass

    def game(self):
        pass


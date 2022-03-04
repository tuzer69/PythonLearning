from home import Home


class Human:
    def __init__(self, name):
        self.name = name
        self.satiety = 50
        self.house = Home('')

    def eat(self):
        self.satiety += 7
        self.house.food -= 1

    def work(self):
        self.satiety -= 1
        self.house.money += 5

    def game(self):
        self.satiety -= 1

    def shopping(self):
        self.house.money -= 1
        self.house.food += 7

    def is_alive(self):
        if self.satiety > 0:
            return True
        else:
            return False

class Home:
    def __init__(self, name):
        self.food = 50
        self.cat_food = 30
        self.money = 100
        self.people = []
        self.dirt = 0

    def add_peopel(self, human):
        self.people.append(human)
        human.house = self

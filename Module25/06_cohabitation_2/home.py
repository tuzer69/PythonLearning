class Home:
    def __init__(self):
        self.food = 50
        self.cat_food = 30
        self.money = 0
        self.people = []
        self.dirt = 0

    def add_peoplе(self, human):
        self.people.append(human)
        human.house = self

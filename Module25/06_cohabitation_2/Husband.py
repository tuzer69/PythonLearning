from human import Human


class Husband(Human):
    def work(self):
        self.house.money += 150

    def game(self):
        self.happiness += 20

    def is_alive(self):
        super(Husband, self).is_alive()
        if self.happiness < 20:
            self.game()
        elif self.house.money < 20:
            self.work()




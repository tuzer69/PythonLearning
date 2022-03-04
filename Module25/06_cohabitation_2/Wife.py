from human import Human


class Wife(Human):
    def clean(self):
        if self.house.dirt < 100:
            self.house.dirt = 0
        else:
            self.house.dirt -= 100

    def buy_coat(self):
        self.happiness += 60

    def is_alive(self):
        if self.happiness < 20:
            self.game()
        elif self.house.food < 30:
            self.shopping()
        elif self.house.dirt > 90:
            self.clean()
        elif self.happiness < 20:
            self.pet_cat()
        elif self.house.money > 700:
            self.buy_coat()
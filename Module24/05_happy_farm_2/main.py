class Potato:
    stages = {0: 'Семя', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, number):
        self.number = number
        self.stage = 0

    def show_stage(self):
        print('Стадия роста:', self.stages[self.stage])

    def grow(self):
        if self.stage < 3:
            self.stage += 1


class PotatoGarden:
    def __init__(self):
        self.potatos = []

    def show_info(self):
        for i_potato in self.potatos:
            print('Картошка ', i_potato.number, ': ',
                  i_potato.stages[i_potato.stage], sep='')

    def grow(self):
        for i_potato in self.potatos:
            i_potato.grow()


class Gardener:
    def __init__(self, name, garden):
        self.name = name
        self.garden = garden
        self.potato_count = 0

    def watering(self):
        self.garden.grow()

    def harvest(self):
        for i_potato in self.garden.potatos:
            if i_potato.stage == 3:
                i_potato.stage = 0
                self.potato_count += 1
        print('Картошки собрано:', self.potato_count)


garden = PotatoGarden()
garden.potatos.append(Potato(1))
garden.potatos.append(Potato(2))
garden.potatos.append(Potato(3))
gardener = Gardener('Nik', garden)

gardener.watering()
gardener.watering()
gardener.watering()
garden.show_info()
gardener.harvest()
garden.show_info()

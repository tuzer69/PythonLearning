from Figures import threeDfigure


class cube(threeDfigure):
    def __init__(self, base):
        super().__init__()
        self.height = base
        self.width = base

    def get_square(self):
        return self.height * self.width

    def get_perimetr(self):
        return self.base * 4

    def get_area(self):
        return (self.height * self.width) * 6


class triange(threeDfigure):
    def __init__(self, base, height):
        super().__init__()
        self.height = height
        self.base = base

    def get_area(self):
        pass

    def get_perimetr(self):
        return 2 * self.height * self.base

    def get_square(self):
        return 0.5 * self.height * self.base

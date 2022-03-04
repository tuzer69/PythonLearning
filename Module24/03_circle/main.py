import math


class Circle:
    def __init__(self, X=0, Y=0, R=1):
        self.X = X
        self.Y = Y
        self.R = R
        self.S = round(math.pi * R ** 2, 2)

    def square(self):
        print('Площадь:', self.S)

    def perimeter(self):
        print('Периметр:', round(2 * math.pi * self.R, 2))

    def scale(self):
        scale = int(input('Во сколько раз увеличить окружность? '))
        self.R *= scale
        self.S = round(math.pi * self.R ** 2, 2)
        print('Новая площадь окружности:', self.S)

    def cross(self, circle):
        r_summa = self.R + circle.R
        if abs(self.X - circle.X) and abs(self.Y - circle.Y) < r_summa:
            print('Окружности пересекаются')
        else:
            print('Окружности НЕ пересекаются')


one = Circle(1, 2, 2)
two = Circle(8, 7, 3)

one.square()
one.perimeter()
one.scale()
one.cross(two)

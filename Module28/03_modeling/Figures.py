from abc import ABC, abstractmethod


class twoDfigure(ABC):
    def __init__(self):
        self.base = 0
        self.width = 0
        self.height = 0

    @property
    def base(self):
        return self.base

    @base.setter
    def base(self, value):
        self._base = value

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        self._height = value

    @abstractmethod
    def get_perimetr(self):
        pass

    @abstractmethod
    def get_square(self):
        pass


class threeDfigure(twoDfigure, ABC):
    def __init__(self):
        super().__init__()
        self.area = []

    @abstractmethod
    def get_area(self):
        pass


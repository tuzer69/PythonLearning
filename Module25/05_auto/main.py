from base import Transport


class Bus(Transport):
    def __init__(self, X, Y, angle):
        super().__init__(X, Y, angle)
        self.__money = 0
        self.__passengers = 0
        self.__distance = 0

    def enter(self):
        self.__passengers += 1

    def exit(self):
        if self.__passengers > 0:
            self.__passengers -= 1

    def move(self):
        self.__distance += 5
        self.__money += self.__distance * self.__passengers
        print(self.__passengers, self.__money)

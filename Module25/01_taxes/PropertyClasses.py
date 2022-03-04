from BaseClass import Property


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calc_tax(self):
        return round(self.worth / 1000, 2)


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calc_tax(self):
        return round(self.worth / 200, 2)


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calc_tax(self):
        return round(self.worth / 500, 2)

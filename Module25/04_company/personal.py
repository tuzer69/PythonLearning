class Person:
    __name = ''
    __surname = ''
    __age = 0


class Employee(Person):
    pass


class Manager(Employee):
    def get_salary(self):
        return 13000


class Agent(Employee):
    def __init__(self, sales=4000):
        self.__sales = sales

    def get_salary(self):
        return round(5000 + self.__sales * 0.05)


class Worker(Employee):
    def __init__(self, hours=120):
        self.__hours = hours

    def get_salary(self):
        return round(100 * self.__hours)

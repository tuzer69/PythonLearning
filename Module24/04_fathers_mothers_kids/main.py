class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.childs = []

    def reassure(self, child):
        child.calm = True

    def feed(self, child):
        child.hunger = False

    def add_child(self, child):
        self.childs.append(child)


class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.calm = True
        self.hunger = False


parent = Parent('John', 59)
child = Child('Sem', 18)
parent.add_child(child)

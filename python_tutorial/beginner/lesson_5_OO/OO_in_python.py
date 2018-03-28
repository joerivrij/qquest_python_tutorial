class Animal:

    def __init__(self, name, ):
        self.name = name

    def talk(self):
        raise NotImplementedError("Not valid")

    def show_name(self):
        print(self.name)


class Duck(Animal):

    def talk(self):
        print("Quack")


class Dog(Animal):

    def talk(self):
        print("woof")


a1 = Animal("Bert")
a1.show_name()
#a1.talk()

d1 = Duck("Donald")
d1.show_name()
d1.talk()

g1 = Dog("Laika")
g1.show_name()
g1.talk()

# ====================================== Polymorphism in Python ================================================
#
#
# class Animal:
#     def speak(self):
#         pass
#
#
# class Dog(Animal):
#     def speak(self):
#         print("Woof")
#
#
# class Cat(Animal):
#     def speak(self):
#         print("Meoww")
#
#
# class Cow(Animal):
#     def speak(self):
#         print("Moo!")
#
#
# d1 = Dog()
# d1.speak()
#
# c1 = Cat()
# c1.speak()


# Avengers
class Avenger:
    def __init__(self, name):
        self.name = name

    def attack(self):
        pass


class IronMan(Avenger):
    def attack(self): # Method Overriding
        print(f"{self.name} attacks with Repulsor Beams")


class Thor(Avenger):
    def attack(self):
        print(f"{self.name} attacks with Hammer")


class Hulk(Avenger):
    def attack(self):
        print(f"{self.name} attacks with Green Fist and raw strength")


# avenger = Hulk("Hulk")
# avenger.attack()


avenger = IronMan("IronMan")
avenger.attack()






















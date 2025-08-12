
from os import name


class Dog:
    name = None
    age = None

    def bark(self):
        print("멍")

    def show_info(self):
        print(self.name, self.age)

d = Dog()
d.name = "만득이"
d.age = 3
d.show_info()

d2 = Dog()
d2.name = "후추"
d2.age = 2
d2.show_info()

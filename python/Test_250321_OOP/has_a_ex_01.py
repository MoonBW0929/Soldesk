
class Dog:

    def __init__(self, name, age, clothes):
        self.name = name
        self.age = age
        self.clothes = clothes

    def show_info(self):
        print(self.name, self.age)
        self.clothes.show_info()

class Human:

    def __init__(self, name, home, dog):
        self.name = name
        self.home = home
        self.dog = dog

    def show_info(self):
        print(self.name, self.home)
        self.dog.show_info()

class Clothes:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def show_info(self):
        print(self.name, self.color)

clothes = Clothes("개 목걸이", "Red")
dog = Dog("만득이", 2, clothes)
h = Human("홍길동", "인천", dog)

h.show_info()

print(h.name)
print(h.dog.name)
h.dog.show_info()
print(h.dog.clothes.name)
h.dog.clothes.show_info()

class Avengers:
    def __init__(self, n, a):
        self.name = n
        self.age = a
    
    def attack(self):
        print("공격")

    def print_info(self):
        print(self.name)
        print(self.age)

class Human:
    def __init__(self, n, addr):
        self.name = n
        self.addr = addr

    def eating(self):
        print("밥 먹기")

    def print_info(self):
        print(self.name)
        print(self.addr)

class IronMan(Avengers, Human):
    def __init__(self, n, a, addr):
        super().__init__(n, a)
        self.addr = addr

    def print_info(self):
        super().print_info()
        print(self.addr)

i = IronMan("tony", 20, "주소")
i.attack()
i.eating()
i.print_info()

class Product:

    def __init__(self, n, p):
        self.name = n
        self.price = p

    def show_info(self):
        print(self.name)
        print(self.price)

class Pen(Product):
    
    def __init__(self, n, p, c):
        super().__init__(n, p)
        self.color = c

    def show_info(self):
        super().show_info()
        print(self.color)

p1 = Product("삼성123", 500000)
# p1.show_info()

pen = Pen("모나미153", 500, "빨강")
# pen.show_info()

class Shoes(Product):
    def __init__(self, n, p, s):
        super().__init__(n, p)
        self.size = s

    def show_info(self):
        super().show_info()
        print(self.size)

class Computer(Product):
    def __init__(self, n, p, ls):
        super().__init__(n, p)
        self.com_info = ls
    
    def show_info(self):
        super().show_info()
        print(self.com_info)

class Notebook(Computer):
    def __init__(self, n, p, ls, w):
        super().__init__(n, p, ls)
        self.weight = w

    def show_info(self):
        super().show_info()
        print(self.weight)

s = Shoes("조던123", 100000, 250)
c = Computer("매직스테이션123", "200만원",
             ["cpu i5-1234", 16, 500])
n = Notebook("그램123", "250만원",
             ["cpu i7-4567", 32, 250], 3)

s.show_info()
print()
c.show_info()
print()
n.show_info()
print()
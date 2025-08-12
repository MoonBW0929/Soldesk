class Pen:
    # name = None
    # color = None
    # price = None

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def __del__(self):
        print("없어짐")

    def print_info(self):
        print(self.name, self.color, self.price)

p1 = Pen("모나미153", "Red", 500)
Pen.print_info(p1)

p2 = Pen("모나미153", "Blue", 1000)
Pen.print_info(p2)

p3 = p1
Pen.print_info(p3)

p1.price = 300

p1 = None

Pen.print_info(p3)

class Phone:
    model_name = None
    maker = None
    price = None

    def __init__(self):
        print("핸드폰 입고됨")

    def print_info(self):
        print(self.model_name)
        print(self.maker)
        print(self.price)

# p1 = Phone()
# p1.model_name = "Galaxy S25"
# p1.maker = "SamSung"
# p1.price = "120"

# Phone.print_info(p1)

#################################################

class Computer:
    cpu = None
    ram = None
    hdd = None

    def __init__(self, cpu, ram, hdd):
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd

    def print_info(self):
        print(self.cpu ,self.ram, self.hdd)

c1 = Computer("i9_11th", 16, 500)
Computer.print_info(c1)

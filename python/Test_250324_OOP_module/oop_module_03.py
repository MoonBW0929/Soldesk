class Book:
    def __init__(self, n, p):
        self.name = n
        self.price = p
    
    def print_info(self):
        print(self.name)
        print(self.price)

if __name__ == "__main__":
    from oop_module_02 import BoardMarker
    bm1 = BoardMarker("pen", "black")
    bm1.print_info()
class BoardMarker:
    def __init__(self, n, c):
        self.name = n
        self.color = c
    
    def print_info(self):
        print(self.name)
        print(self.color)

if __name__ == "__main__":
    from oop_module_03 import Book
    b1 = Book("동화책", 10000)
    b1.print_info()
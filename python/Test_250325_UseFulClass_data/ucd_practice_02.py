file = open("C:\\moon\\snack.csv", "r", encoding="utf-8")

class Snack:
    def __init__(self, str):
        str = str.replace("\n", "")
        str = str.split(",")
        self.name = str[0]
        self.price = int(str[1])
        self.weight = int(str[2])

    def print_info(self):
        print(self.name)
        print(self.price)
        print(self.weight)
        print("--------------")

s_ls = file.readlines()
snacks = []
for i in s_ls:
    s = Snack(i)
    snacks.append(s)

snacks.sort(key=lambda x : x.price / x.weight)
for snack in snacks:
    snack.print_info()

file.close()
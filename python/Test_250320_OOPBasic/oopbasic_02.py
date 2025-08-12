
class Cat:
    name = None
    age = None

    def meow(self, cnt):
        print("냥" * cnt)

    def show_info(self):
        print("이름 : %s" % self.name)
        print("나이 : %d" % self.age)

c1 = Cat()
c1.name = "후추"
c1.age = 2

# c1.meow(3)
Cat.meow(c1, 3)
Cat.show_info(c1)

c1.weight = 10
print(c1.weight)
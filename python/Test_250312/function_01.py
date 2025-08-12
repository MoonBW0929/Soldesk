
def buy_cigarette():
    print("돈을 건내줌")
    print("슈퍼 가기")
    print("담배 사기")
    print("담배 가져다 주기")

def test():
    pass

def print_sum(x, y=10):
    print("%d + %d = %d" % (x, y, x+y))

def print_sum_3(x, y, z):
    print("%d + %d + %d = %d" % (x, y, z, x+y+z))

buy_cigarette()
print_sum(10, 20)
print_sum(y=20, x=10)
print_sum(x=10)
print_sum_3(10, 20, 30)
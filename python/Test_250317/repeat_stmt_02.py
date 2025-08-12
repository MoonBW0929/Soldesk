
from random import randint


for i in range(9, 0, -2):
    print(i)

print("--------------")


a = 0
for i in range(1, 6):
    a += i

print(a)
print("--------------")


a = 0
for i in range(1, 20, 2):
    a += i

print(a)
print("--------------")


for i in range(1, 10):
    print("2 x %d = %d" % (i, 2*i))

print("--------------")


for i in range(2, 10):
    for j in range(1, 10):
        print("%d x %d = %d" % (i, j, i*j))
    print()

print("--------------")


for i in range(1, 10):
    for j in range(2, 10):
        print("%d x %d = %d" % (j, i, j*i), end="\t")
    print()

print("--------------")


for i in range(1, 6):
    for j in range(i):
        print("ㅋ", end="")
    print()
    
print("--------------")


for i in range(5, 0, -1):
    for j in range(i):
        print("ㅋ", end="")
    print()
    
print("--------------")


for i in range(0, 5):
    for j in range(i):
        print("  ", end="")
    print("ㅋ")
    
print("--------------")


for i in range(5):
    if i % 2 == 0 :
        s = "ㅋ"
    else:
        s = "ㅎ"
    for j in range(i * 2 + 1):
        print(s, end="")
    print()
    
print("--------------")

a = 0
i = 0
while a < 100:
    i += 1
    a += i

print(i)

print("--------------")


c = 0
while c != 4:
    c = randint(1, 5)
    print(c)

print("--------------")


c = 0
while c != 10:
    c = int(input("입력 : "))
    print("출력 : %d" % c)

print("--------------")
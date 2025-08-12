
x = int(input("x : "))
y = int(input("y : "))
print("--------------")

try:
    print("%d" % (x/y))

    e = [54, 123, 3]
    print(e[y])
except Exception as a:
    print("잘못 됨")
    print(type(a))
else:
    print("문제 없음")
finally:
    print("종료")
a = [10, 20]
b = [30, 40]

c = a + b
print(c)

d = a * 3
print(d)

print("---------------------------------------")

import numpy as np
aa = np.array([10, 20])
bb = np.array([30, 40])

cc = aa + bb
print(cc)

dd = aa * 3
print(dd)

print("---------------------------------------")

name = np.array(["홍길동", "김길동", "이길동"])
kor = np.array([100, 90, 60])
eng = np.array([10, 60, 80])
mat = np.array([50, 40, 100])

avg = (kor + eng + mat) / 3
print(avg)

over60 = avg > 60
print(over60)
print(name[over60])
print(name[kor == 100])

print(name[(eng > 50) & (eng < 70)])
import numpy as np

a = np.random.randint(1, 11, [10])
print(a)
print("----------------------")

a[1] = 99
a[2:5] = 100
print(a)
print("----------------------")

# 조건부 변경 (조건식, 값, 대상)
a = np.where(a % 2 == 0, 222, a)
print(a)
print("----------------------")
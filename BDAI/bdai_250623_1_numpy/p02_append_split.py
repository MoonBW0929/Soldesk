import numpy as np

a = np.random.randint(1, 101, [3, 5])
b = np.random.randint(1, 101, [3, 5])
print(a)
print(b)
print("--------------------------")

c = a + b
print(c)
print("--------------------------")

d = np.concatenate([a, b])
print(d)
print("--------------------------")

e = np.append(a, b)
print(e)
print("--------------------------")

# concatenate 옵션 / axis = 0 : 행, axis = 1 : 열
# axis = 0 기본 옵션
f = np.concatenate([a, b], axis=1)
print(f)
print("--------------------------")

# 특정 기준 없이 2등분
g = np.array_split(a, 2)
print(g)
print("--------------------------")

# 정확하게 x등분, 개수가 나누려는 x로 맞아 떨어져야 가능
h = np.split(a, 3)
print(h)
print("--------------------------")
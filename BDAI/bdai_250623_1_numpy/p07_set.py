import numpy as np

a = np.random.randint(1, 11, [2, 3])
b = np.random.randint(1, 11, [2, 3])
print(a)
print(b)
print("---------------------------------")

# 교집합
c = np.intersect1d(a, b)
print(c)
print("---------------------------------")

# 합집합
d = np.union1d(a, b)
print(d)
print("---------------------------------")

# a에서 b에 있는 거 빼고 나머지
e = np.setdiff1d(a, b)
print(e)
print("---------------------------------")

# a와 b의 중복을 뺀 나머지
f = np.setxor1d(a, b)
print(f)
print("---------------------------------")

# 중복 제거
g = np.unique(a)
print(g)
print("---------------------------------")
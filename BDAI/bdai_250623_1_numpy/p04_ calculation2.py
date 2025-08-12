import numpy as np

a = np.random.rand(2, 3)
print(a)
print("--------------------")

# 소수점 올림
b = np.ceil(a)
print(b)
print("--------------------")

# 소수점 버림
c = np.floor(a)
print(c)
print("--------------------")

# 반올림
d = np.rint(a)
print(d)
print("--------------------")

# 자리수 지정 반올림
e = np.round(a, 2)
print(e)
print("--------------------")

# 소수점 이하 셋째 자리에서 올림
f = np.ceil(a * 100) / 100
print(f)
print("--------------------")

g = np.array([1, np.nan, 123, np.inf, 33])
print(g)
print("--------------------")

h = np.isnan(g)
print(h)
print("--------------------")

i = np.isinf(g)
print(i)
print("--------------------")

j = np.random.randint(-5, 6, [2, 3])
print(j)
print("--------------------")

k = np.abs(j)
print(k)
print("--------------------")

l = np.sqrt(j)
print(l)
print("--------------------")

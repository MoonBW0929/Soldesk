import numpy as np

a = np.random.randint(1, 11, [2, 3])
print(a)
print("-------------------------")

b = np.sum(a)
print(b)
print("-------------------------")

c = np.mean(a)
print(c)
print("-------------------------")

d = a - c
d = d ** 2
d = np.mean(d)
print(d)
print("-------------------------")

e = np.var(a)
print(e)
print("-------------------------")

f = np.sqrt(d)
print(f)
print("-------------------------")

g = np.std(a)
print(g)
print("-------------------------")

h = np.max(a)
print(h)
i = np.min(a)
print(i)
print("-------------------------")

j = np.max(a, axis=1)
print(j)
print("-------------------------")

k = np.min(a, axis=0)
print(k)
print("-------------------------")

# 가장 큰 값이 나온 index 반환
l = np.argmax(a)
print(l)
print("-------------------------")

m = np.argmin(a)
print(m)
print("-------------------------")

n = np.argmax(a, axis=1)
print(n)
print("-------------------------")

o = np.argmin(a, axis=0)
print(o)
print("-------------------------")
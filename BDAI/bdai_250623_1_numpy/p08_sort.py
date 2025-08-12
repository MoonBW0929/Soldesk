import numpy as np

a = np.random.randint(1, 101, [10])
print(a)
print("-----------------------")

b = np.sort(a)
print(b)
print("-----------------------")

c = np.sort(a)
print(c[::-1])
print("-----------------------")

d = np.random.randint(1, 101, [3, 5])
print(d)
print("-----------------------")

e = np.sort(d)
print(e)
print("-----------------------")

f = np.sort(d, axis=0)
print(f)
print("-----------------------")

g = np.sort(d, axis=0)[::-1]
print(g)
print("-----------------------")

h = []
for v in np.sort(d):
    h.append(v[::-1])
h = np.array(h)

print(h)
print("-----------------------")

i = []
for v in d:
    i = np.append(i, v)
i = np.split(np.sort(i), len(d))
print(i)
print("-----------------------")
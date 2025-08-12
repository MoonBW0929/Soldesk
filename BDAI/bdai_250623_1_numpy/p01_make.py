import numpy as np

a = np.zeros([3, 2])
print(a, a.dtype)

b = np.ones([3, 2])
print(b, b.dtype)

c = np.empty([3, 2])
print(c, c.dtype)

d = np.arange(2, 10, 3)
print(d)

# 0.0 ~ 0.9999 랜덤
e = np.random.rand(3, 2)
print(e)

# 평균 0, 표준편차 1 랜덤
f = np.random.randn(3, 2)
print(f)

# 지정한 범위 안에서 랜덤
g = np.random.randint(1, 10 ,[3, 2])
print(g)
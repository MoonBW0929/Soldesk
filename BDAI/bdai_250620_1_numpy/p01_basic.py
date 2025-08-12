score = [[100, 90, 80], [50, 60, 100]]
print(score)
print(type(score))
print(score[0])

print(score[0][1])

score[1][2] = 0
print(score)

print(score[1][0:3])
print("------------------------------------------------------")

import numpy as np

score2 = np.array([[100, 90, 80], [50, 60, 100]])
print(score2)
print(type(score2))
print(score2[0])

# print(score2[0][1])
print(score2[0, 1])

# score2[1][2] = 0
score2[1, 2] = 0
print(score2)

score2[1, 0:3] = 0
print(score2)

# 행/열 개수
print(score2.shape)
# 리스트에 있는 데이터의 자료형
print(score2.dtype)
# 총 데이터의 개수
print(score2.size)
print("------------------------------------------------------")
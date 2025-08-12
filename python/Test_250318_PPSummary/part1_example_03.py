# 로또 번호 생성기

from random import randint


lotto_num = []

def get_lotto_num(lotto_num):
    num = randint(1, 45)
    for i in range(len(lotto_num)):
        if num == lotto_num[i]:
            return get_lotto_num(lotto_num)
    return num

for j in range(0, 6):
    lotto_num.append(get_lotto_num(lotto_num))

print(lotto_num)
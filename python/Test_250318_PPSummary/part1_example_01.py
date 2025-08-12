# 숫자 맞추기 (up, down)

from random import randint

def judge(gameAns, userAns):

    if gameAns > userAns: print("UP\n")
    elif gameAns < userAns: print("DOWN\n")
    else: return True

    return False

def getAns():
    userAns = int(input("추측 : "))
    if 0 < userAns < 10001:
        return userAns
    return getAns()

def pickGameAns():
    return randint(1, 10000)

gameAns = pickGameAns()
turn = 0

while True:
    userAns = getAns()
    turn += 1

    if judge(gameAns, userAns): break

print("%d번만에 정답" % turn)


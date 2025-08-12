# 가위바위보

from random import randint

def get_com_RSP():
    global RSP

    comRSP = randint(1, 3)
    print("컴 : %s" % RSP[comRSP-1])
    return comRSP

def get_user_RSP():
    global RSP

    userRSP = int(input("선택 : "))
    if 0 < userRSP < 4:
        print("나 : %s" % RSP[userRSP-1])
        return userRSP
    
    return get_user_RSP()

def get_RSP_result(userRSP, comRSP):

    result = userRSP - comRSP

    if result == -1 or result == 2:
        print("패")
        return 0
    elif result == 0:
        print("무승부")
        return 2
    else: 
        print("승")
        return 1

comRSP = 0
wins = 0
RSP = ["가위", "바위", "보"]

print("1) %s\n2) %s\n3) %s" % (RSP[0], RSP[1], RSP[2]))
print("-----------------")

while True:
    userRSP = get_user_RSP()
    comRSP = get_com_RSP()

    result = get_RSP_result(userRSP, comRSP)
    if result == 0:
        break
    elif result == 1: wins += 1

    print("-----------------")

print("%d연승" % wins)
print("-----------------")

    
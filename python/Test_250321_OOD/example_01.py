# 숫자 맞추기 (up, down)

from random import randint
import re


class Human_q:
    
    def ready(self):
        print("랜덤한 숫자 생각")
        self.gameAns = randint(1, 10000)
        print(self.gameAns)
        self.turn = 0

        callenger = self.get_callenger()

        self.game_start(callenger)

    def get_callenger(self):
        print("up down 게임 참가자 받음")
        return Human_c()

    def game_start(self, callenger):
        print("게임 시작")
        print("---------------")
        while True:
            while True:
                userAns = callenger.callenge()
                if 0 < userAns < 10001: break
                print("잘못된 숫자 범위")
                
            self.turn += 1

            if self.judge(userAns):
                self.tell_result()
                break

    def judge(self, userAns):

        if self.gameAns > userAns: print("UP\n")
        elif self.gameAns < userAns: print("DOWN\n")
        else:
            print("---------------")
            return True

        return False
    
    def tell_result(self):
        print("%d번만에 정답" % self.turn)


class Human_c:
    
    def callenge(self):
        return int(input("추측 : "))

# human = Human_q()
# human.ready()

################################################

class Enemy:
    def thinkAns(self):
        return randint(1, 10000)
    
    def ask(self, u):
        userAns = u.tell()
        if 0 < userAns < 10001:
            return userAns
        return self.ask()

    def gameStart(self , u):
        turn = 0
        gameAns = self.thinkAns()
        while True:
            turn += 1
            userAns = self.ask(u)
            end = self.judge(gameAns, userAns)
            if end:
                self.tellResult(turn)
                break


    def judge(self, gameAns, userAns):
        if gameAns == userAns:
            print("정답")
            return True
        elif gameAns > userAns:
            print("UP")
        else:
            print("DOWN")
        return False
    
    def tellResult(self, turn):
        print("%d번만에 정답" % turn)

class User:
    def tell(self):
        return int(input("뭐 : "))

e = Enemy()
u = User()

e.gameStart(u)
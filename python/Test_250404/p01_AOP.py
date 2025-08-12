# 프로그래밍 패러다임
#   Procedural Programming
#       절차 지향 프로그래밍
#       순서대로 잘 써서 결과 내자
#   Object Oriented Programming
#       객체 지향 프로그래밍
#       실생활을 표현해서 유지보수 쉽게 하자
#   Aspect Oriented Programming
#       관점 지향 프로그래밍
#       OOP를 다른 관점에서 보자
#       메소드들의 공통된 부분이 보일텐데
#       공통된 부분 정리하자

# 홍길동, 30살인 사람
# 정보 출력
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def showInfo(self):
        print(self.name)
        print(self.age)

    def ready(self):
        print("씻고, 옷 입고")
        print("나가서 엘베 타고 내려가")
    def goSchool(self):
        self.ready()
        print("버스 타고 학교로")
    def goMart(self):
        self.ready()
        print("걸어서 마트로")
    def goPark(self):
        self.ready()
        print("자전거 빌려서 공원으로")


h = Human("홍길동", 30)
h.showInfo()
h.goMart()
h.goPark()
h.goSchool()
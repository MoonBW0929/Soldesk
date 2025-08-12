
class Student:

    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def print_grade(self):
        print("%s 성적" % self.name)
        print("국어 : %d" % self.kor)
        print("영어 : %d" % self.eng)
        print("수학 : %d" % self.math)


s1 = Student("홍길동", 100, 50, 50)

score = [
    s1,
    Student("김길동", 30, 50, 60),
    Student("이길동", 70, 50, 40),
    Student("최길동", 80, 80, 20)
]

# print(score[1].kor)
# Student.print_grade(score[2])

# score.sort(key=(lambda s: s.kor + s.eng + s.math))
# score.sort(key=(lambda s: s.name), reverse=True)
score.sort(key=(lambda s: s.kor))

for i in score:
    i.print_grade()
    print("---------------")
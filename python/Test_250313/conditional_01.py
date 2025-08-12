
F_grade = input("중간고사 : ")
S_grade = input("기말고사 : ")
F_grade = int(F_grade)
S_grade = int(S_grade)

avg = (F_grade+S_grade)/2

print("----------------")
print("평균점수 : %.1f" % avg)

if avg > 80:
    print("잘했다")
else:
    print("야")
    if avg > 70:
        print("다음에는 노력좀")

if avg >= 90:
    print("수")
elif avg >= 80:
    print("우")
elif avg >= 70:
    print("미")
elif avg >= 60:
    print("양")
else:
    print("가")


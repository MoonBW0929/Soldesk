
def get_height():
    h = input("키 : ")
    h = float(h)
    if(h > 3):
        print("cm 단위로 적으세요")
        return get_height()
    return h

name = input("이름 : ")
# height = float(input("키 : ")) / 100
height = get_height()
weight = float(input("몸무게 :"))

print("----------------")
bmi = (weight) / (height*height)

print("BMI : %.1f" % bmi)

if bmi >= 39:
    print("%s씨는 고도 비만" % name)
elif bmi >= 32:
    print("%s씨는 중도 비만" % name)
elif bmi >= 30:
    print("%s씨는 경도 비만" % name)
elif bmi >= 24:
    print("%s씨는 과체중" % name)
elif bmi >= 10:
    print("%s씨는 정상" % name)
else:
    print("%s씨는 저체중" % name)

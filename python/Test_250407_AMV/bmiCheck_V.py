from Guest_M import Guest


class ConsoleScreen:
    def get_info():
        print("환자 정보 입력")
        print("--------------------")
        name = input("이름 : ")
        height = float(input("키 : "))
        weight = float(input("몸무게 : "))
        print("--------------------")

        return Guest(name, height, weight)

    def printResult(guest):
        print("BMI : %.1f" % guest.bmi)
        print("%s씨는 %s" % (guest.name, guest.result))
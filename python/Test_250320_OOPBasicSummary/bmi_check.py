
class Doctor:
    
    def __init__(self):
        pass

    def start(self):
        print("진료 시작")
        guest = self.call_guest()
        self.ask(guest)
        self.bmi_check(guest)
        self.tell_result(guest)

    def call_guest(self):
        print("손님을 부름")
        return Guest()
    
    def ask(self, guest):
        print("환자 정보 입력")
        print("--------------------")
        guest.tell()
        print("--------------------")
        
    def bmi_check(self, guest):
        guest.bmi = (guest.weight) / (guest.height*guest.height)

        if guest.bmi >= 39:
            guest.result = "고도 비만"
        elif guest.bmi >= 32:
            guest.result = "중도 비만"
        elif guest.bmi >= 30:
            guest.result = "경도 비만"
        elif guest.bmi >= 24:
            guest.result = "과체중"
        elif guest.bmi >= 10:
            guest.result = "정상"
        else:
            guest.result = "저체중"
    
    def tell_result(self, guest):

        print("BMI : %.1f" % guest.bmi)
        print("%s씨는 %s" % (guest.name, guest.result))


class Guest:

    def __init__(self):
        pass

    def tell(self):
        self.name = input("이름 : ")
        self.height = float(input("키 : ")) / 100
        self.weight = float(input("몸무게 : "))

doc = Doctor()
doc.start()

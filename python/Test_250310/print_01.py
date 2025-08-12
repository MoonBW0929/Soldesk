
age = 30
eye = 1.2
addr = "강동"
hungry = False
humi = 30.123123
temp = 10

print("나이 : %d살" % age)
print("나이 : %05d살" % age)
print("시력 : %.2f" % eye)
print("주소 : %s" % addr)
# print("배고픔 : %b" % hungry)
print("습도 : %.1f%%" % humi)
print("기온은 %d도고, 습도는 %.1f%%다" % (temp, humi))

today = "기온은 %d도고, 습도는 %.1f%%다" % (temp, humi)
print(today)
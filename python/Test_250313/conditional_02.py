
value = 13

# if (value & 1):
#     print("와이파이")
# if (value & 2):
#     print("주차장")
# if (value & 4):
#     print("흡연실")
# if (value & 8):
#     print("24시간")

# if ((value >> 0) % 2):
#     print("와이파이")
# if ((value >> 1) % 2):
#     print("주차장")
# if ((value >> 2) % 2):
#     print("흡연실")
# if ((value >> 3) % 2):
#     print("24시간")

ls = ["와이파이", "주차장", "흡연실", "24시간"]

for i in range(len(ls)):
    if ((value >> i) % 2):
        print(ls[i])
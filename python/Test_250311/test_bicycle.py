
wheel_round = input("바퀴 둘레 : ")
F_gear = input("앞 기어 톱니 수 : ")
B_gear = input("뒷 기어 톱니 수 : ")
F_cycle_num = input("발 구른 횟수 : ")
print("------------------------------")

wheel_round = int(wheel_round)
F_gear = int(F_gear)
B_gear = int(B_gear)
F_cycle_num = int(F_cycle_num)

B_cycle_num = F_gear * F_cycle_num / B_gear
total_dist = B_cycle_num * wheel_round

print("이동 거리 : %d" % total_dist)
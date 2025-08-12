total = 0
cnt = 0

ls = input("입력 : ")
ls = ls.split(",")

for i in range(len(ls)):
    try:
        var = int(ls[i])
    except:
        pass
    else:
        total += var
        cnt += 1

print("------------------------------------")
print("합계 : %d" % total)
print("평균 : %.1f" % (total/cnt))
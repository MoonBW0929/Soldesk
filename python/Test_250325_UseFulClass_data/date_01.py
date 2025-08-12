from datetime import datetime
from time import strftime

now = datetime.today()
# print(now)
# print(now.year)
# print(now.month)
# print(now.day)

d = datetime(2000, 1, 1)
# print(d)

#####################################################################

d2 = "1999,12,31"
ls = d2.split(",")
for i in range(len(ls)):
    ls[i] = int(ls[i])

date = datetime(ls[0], ls[1], ls[2])
# print(date)

#####################################################################

d3 = "2002,02,02"
d3 = datetime.strptime(d3,"%Y,%m,%d")
# print(d3)

# help(strftime)

#####################################################################

d4 = datetime.today()
# print("%d.%d.%d" % (d4.year, d4.month, d4.day))

#####################################################################

d5 = datetime.today()
d5 = datetime.strftime(d5, "%Y.%m.%d")
# print(d5)

#####################################################################

# birth = input("생일(yyyy-MM-dd) : ")
# print("----------------------------")
# birth = datetime.strptime(birth, "%Y-%m-%d")

# age = datetime.today().year - birth.year + 1
# print("한국나이 : %d" % age)

#####################################################################

birth = "2001/09/29"
birth = datetime.strptime(birth, "%Y/%m/%d")
birth = datetime.strftime(birth, "%A")
print(birth)
# print(birth.weekday())
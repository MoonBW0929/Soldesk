f = open("C:\\moon\\test.txt", "r", encoding="utf-8")

# data1 = f.read()
# print(data1)

# data2 = f.readline()
# print(data2)
# data2 = f.readline()
# print(data2)
# data2 = f.readline()
# print(data2)

data3 = f.readlines()
for i in data3:
    i = i.replace("\n", "")
    print(i)

f.close()
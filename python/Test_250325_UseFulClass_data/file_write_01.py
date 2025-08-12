txt = input("입력 : ")

file = open("C:\\moon\\test.txt", "a", encoding="utf-8")
file.write(txt + "\r\n")
file.close()
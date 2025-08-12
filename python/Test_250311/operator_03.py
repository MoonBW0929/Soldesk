
height = float(input("키 : "))
age = int(input("나이 : "))
print("----------------------")

print("키는 %.1fcm, 나이는 %d살" % (height, age))

a = height > 140
print(a)

b = age <= 10
print(b)

c = age == 5
print(c)

d = (height >= 200) and (age >= 5)
print(d)

e = (height >= 120) or (age >= 80)
print(e)

f = (age >= 20)
print(f)

g = (height <= 130) and (height >= 100)
print(g)

#h = ((age >= 5) and (height > 130)) or ((age < 4) and (height <= 130))
h = (age >= 5) ^ (height <= 130)
print(h)

i = not h
print(i)


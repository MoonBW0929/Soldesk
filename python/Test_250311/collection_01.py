
kor = 80
s = "문자열 자료형 변수"
eng = [80, 30, 54, 12, 10, 60, 70, 95, 100, 40]

print(eng)
print(type(eng))
print(len(eng))
print(eng[1])
print(eng[1:3])
print(eng[3:9:2])
print(eng[:8:2])
print(eng[::2])
print(eng[::-1])
print(eng.index(30))

del eng[2]
print(eng)

mat = {100, 80, 50, 80, 70, 100, 50, 90}
print(mat)
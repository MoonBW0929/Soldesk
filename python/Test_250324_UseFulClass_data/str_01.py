# a = "abc"
# print(a)
# print(type(a))
# print(id(a))

# b = """aaa
# bbb"""
# print(b)
# print(type(b))
# print(id(b))

# class Dog:

#     """
#     abc
#     """

#     def bark():
#         print("멍")

# def get_add(a, b):
#     """
#     plus return fuction
#     """
#     return a+b

c = "그니까 이제 알아서 해봐요"
# help(str)

print(c.startswith("그니까"))

c = c.replace("이제", "다음부터")
print(c)

print(c.find("까"))

print(c[2])

print(c.find("해봐요") != -1)

print(len(c))

d = "저기"
print(d)
print(id(d))
d += " 뒤에다가"
print(d)
print(id(d))
d += " 이렇게"
print(d)
print(id(d))

e = "홍길동,김길동,이길동"
ls = e.split(",")
print(ls)

f = "    zzzz    "
print(f.strip())

g = "~~~~~ㅎㅎㅎ~~~~~"
print(g.strip("~"))

# a = [1, 7, 12, 60, 4, 4]

# for i in a:
#     print(i)


# for i in range(1,6):
#     print(i)


# a = 1
# for i in range(1,11):
#     a *= i

# print(a)


# b = [1, 231, 2, 3]
# for i in range(len(b)):
#     print(b[i])

b = [1, 231, 2, 3]
for i in enumerate(b):
    print(i, type(i))


c = {"기온":20, "미세먼지":"심함"}
for i in c.items():
    print(i, type(i))
from random import randint

# while True:
#     a = int(input("입력 : "))
#     print("출력 : %d\n" % a)
#     if a == 10: break


# while True:
#     a = randint(1, 5)
#     print(a)
#     if a == 4: break

a = False
for i in range(5):
    for j in range(5):
        for k in range(5):
            
            if k == 2:
                a = True
                break

            print(i, j, k)

        if a: break
    if a: break
    
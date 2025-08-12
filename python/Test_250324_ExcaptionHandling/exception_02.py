def get_divied(x, y):
    try:
        z = x / y
        return z
    except:
        print("?")
        return -999
    finally:
        print("ㅋㅋㅋ")

x = 10
y = int(input("y : "))
z = get_divied(x, y)
print(z)

# def print_odd(num):
#     b = (1 == (num % 2))
#     print(b)

# print_odd(10)

def is_odd(num):
    return (1 == (num % 2))

odd = is_odd(5)
print(odd)

def multi_2(num):
    return num * 2

res = multi_2(4)
print(res)

def get_cal(x, y):

    a = x + y
    b = x - y
    c = x * y
    d = x / y
    return (a, b, c, d)

(aa, bb, _, dd) = get_cal(20, 30)
print(aa)
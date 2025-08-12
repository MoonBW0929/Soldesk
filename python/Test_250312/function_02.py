a = 10
b = [10, 20]
c = [10, 20]
d = 10
e = 10

def test(a, b, c):
    global e
    print(a, b[0], c[0])
    a = 100
    b[0] = 100
    c = [100, 200]
    d = 100
    e = 100
    print(a, b[0], c[0], d, e)

print(a, b[0], c[0])
test(a, b, c)
print(a, b[0], c[0], d, e)
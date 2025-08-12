
max = 10

def range_sum(num):
    if num == 1:
        return 1
    return range_sum(num - 1) + num

def factorial(num):
    if num == 1:
        return 1
    return factorial(num - 1) * num

def fibo(num):
    if num <= 2:
        return 1
    return fibo(num - 2) + fibo(num - 1)

print(range_sum(max))
print(factorial(max))
print(fibo(max))
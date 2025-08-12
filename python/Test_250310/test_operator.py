
price = input("구매한 물건가 : ")
pay_money = input("낸 돈 : ")
print("--------------------")

price = int(price)
pay_money = int(pay_money)

b_money = pay_money - price
total_b_money = b_money

pay_50000 = b_money // 50000
b_money %= 50000

pay_10000 = b_money // 10000
b_money %= 10000

pay_5000 = b_money // 5000
b_money %= 5000

pay_1000 = b_money // 1000
b_money %= 1000

pay_500 = b_money // 500
b_money %= 500

pay_100 = b_money // 100
b_money %= 100

pay_50 = b_money // 50
b_money %= 50

pay_10 = b_money // 10
b_money %= 10

print("거스름돈 : %d" % total_b_money)
print("5만원 : %d" % pay_50000)
print("1만원 : %d" % pay_10000)
print("5천원 : %d" % pay_5000)
print("1천원 : %d" % pay_1000)
print("500원 : %d" % pay_500)
print("100원 : %d" % pay_100)
print("50원 : %d" % pay_50)
print("10원 : %d" % pay_10)
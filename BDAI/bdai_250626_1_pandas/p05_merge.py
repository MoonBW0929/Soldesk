import pandas as pd

data1 = pd.read_csv("C:/moon/data/titanic.csv")
data2 = pd.read_csv("C:/moon/data/titanic.csv")

# 열로 이어 붙이기 (세로)
data3 = pd.concat([data1, data2])
print(data3)
print("---------------------------------")

# 행으로 이어 붙이기 (가로)
data4 = pd.concat([data1, data2], axis=1)
print(data4)
print("---------------------------------")

# join
snack = pd.DataFrame()
snack["이름"] = ["새우깡", "양파링"]
snack["가격"] = [3000, 2000]
snack["제조사"] = ["농심", "롯데"]

company = pd.DataFrame()
company["회사명"] = ["농심", "롯데"]
company["위치"] = ["서울", "수원"]

# 양쪽의 중복되는 필드를 기준으로 붙여줌
# sc = pd.merge(snack, company)
# print(sc)
# print("---------------------------------")

# 양쪽의 중복되는 필드가 여러개라면 기준을 따로 선정
# sc = pd.merge(snack, company, on="제조사")
# print(sc)
# print("---------------------------------")

# 양쪽에 필드명이 다르고 동일한 기능을 하는 필드를 기준으로 할 경우
sc = pd.merge(snack, company, left_on="제조사", right_on="회사명")
print(sc)
print("---------------------------------")
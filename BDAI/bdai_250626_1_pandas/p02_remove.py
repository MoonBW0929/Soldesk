import pandas as pd

data = pd.read_csv("C:/moon/data/titanic.csv")
print(data)
print("-----------------------------------------------")

# 필드 삭제 (해당 필드를 뺀 나머지만 추출)
data = data.drop("Survived", axis=1)
print(data)
print("-----------------------------------------------")

data = data.drop(["Pclass", "Cabin"], axis=1)
print(data)
print("-----------------------------------------------")

# Name과 Fare 빼고 다 삭제
data = data[["Name", "Fare"]]
print(data)
print("-----------------------------------------------")

# 데이터 삭제
data = data.drop(890)
data = data.set_index("Name")
print(data)
print("-----------------------------------------------")

# 요금 30 미만 삭제
data = data[data["Fare"] >= 30]
print(data)
print("-----------------------------------------------")

# 모기
data = pd.read_csv("C:/moon/data/mosquito3.csv", names=["날짜", "물가", "집", "공원"])

# 물가, 공원 필드 없애기
data = data.drop(["물가", "공원"], axis=1)
print(data)
print("-----------------------------------------------")

# 미측정 없애기
data = data[data["집"] != "미측정"]
print(data)
print("-----------------------------------------------")

# 집 모기지수 평균값
data["집"] = pd.to_numeric(data["집"])
print(data["집"].mean())
print("-----------------------------------------------")

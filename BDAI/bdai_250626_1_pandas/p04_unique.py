import pandas as pd

data = pd.read_csv("C:/moon/data/titanic.csv")
print(data)
print("------------------------------------------")

# 등급별로 산/죽은 사람 수
print(data.groupby(["Pclass", "Survived"])["PassengerId"].count())
print("------------------------------------------")

# 등급별 평균 요금
print(data.groupby(["Pclass"])["Fare"].mean())
print("------------------------------------------")

# 성별별 산/죽은 사람 수
print(data.groupby(["Sex", "Survived"])["PassengerId"].count())
print("------------------------------------------")

# 객실 중복 제거
print(data["Cabin"].unique())
print("------------------------------------------")

# 중복 제거한 객실 개수
print(data["Cabin"].nunique())
print("------------------------------------------")

# 객실별 손님 수
print(data["Cabin"].value_counts())
print("------------------------------------------")

# 물가
data = pd.read_csv("C:/moon/data/lnps2.csv", names=["마트이름", "품명", "가격", "날짜", "종류", "구"])
print(data)
print("------------------------------------------")

# 마트의 종류
print(data["마트이름"].unique())
print("------------------------------------------")

# 마트가 몇종류 있는지
print(data["마트이름"].nunique())
print("------------------------------------------")

# 구별로 데이터가 몇개씩 있는지
print(data["구"].value_counts())
print("------------------------------------------")
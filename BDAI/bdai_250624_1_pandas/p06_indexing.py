import pandas as pd

a = pd.read_csv("C:/moon/titanic.csv")
print(a)
print("---------------------")

# 기본 정보 확인
print(a.shape)
print("---------------------")

print(a.columns)
print("---------------------")

print(a.head(2))
print("---------------------")
print(a.tail(3))
print("---------------------")

# 조회

# 열 기준 조회 (특정 필드 조회)
print(a["Name"])
print("---------------------")
print(a.Name)
print("---------------------")

print(a[["Name", "Age"]])
print("---------------------")

# 행 기준 조회 (특정 데이터 조회)
print(a.iloc[1])
print("---------------------")
print(a.iloc[1:5])
print("---------------------")

# 행 조회 기준 변경 (기존 0,1,2,3.... → 변경 Name)
a = a.set_index(a["Name"])
print(a)
print("---------------------")
print(a.loc["Futrelle, Mrs. Jacques Heath (Lily May Peel)"])
print("---------------------")
print(a.loc["Braund, Mr. Owen Harris":"Futrelle, Mrs. Jacques Heath (Lily May Peel)"])
print("---------------------")

# 행 / 열 기준 조회 (특정 필드의 특정 데이터 조회)
print(a.loc["Braund, Mr. Owen Harris"]["Age"])
print("---------------------")
print(a.loc["Braund, Mr. Owen Harris", "Age"])
print("---------------------")
print(a.loc["Braund, Mr. Owen Harris", ["Age", "Pclass"]])
print("---------------------")

# 조건 조회
print(a["Age"] > 30)
print("---------------------")
print(a[a["Age"] > 30])
print("---------------------")
print(a[(a["Age"] >= 20) & (a["Age"] <= 29)])
print("---------------------")
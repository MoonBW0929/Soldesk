from math import nan
import pandas as pd
import numpy as np

data = pd.read_csv("C:/moon/data/titanic.csv")
print(data)

data = data[["Name", "Sex"]]
# male -> 남자, female -> 여자
data["Sex"] = data["Sex"].replace(["male", "female"], ["남자", "여자"])

def change_Mr(str):
    return str.replace("Mr.", "미스터")

# 이름필드에서 Mr. -> 미스터
data["Name"] = data["Name"].apply(change_Mr)

# 이름필드에서 성 부분을 없애기
data["Name"] = data["Name"].apply(lambda x : x.split(",")[0])

print(data)
print("-------------------------------------------------")



data = pd.read_csv("C:/moon/data/titanic.csv")
data = data[["Name", "Age", "Survived"]]

# 나이 -> 10대, 20대...
data["Age"] = data["Age"].fillna(0)
data["Age"] = data["Age"].apply(lambda x : "%d0대" % (x // 10) if x >= 10 else "미상")

print(data)
print("-------------------------------------------------")
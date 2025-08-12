import pandas as pd
import numpy as np

data = pd.read_csv("C:/moon/data/mosquito3.csv", names=["날짜", "물가", "집", "공원"])
print(data)
print("----------------------------------------")

# null 값은 없으나, 측정되지 않은 데이터는 '미측정'일 경우 -> 모든 데이터가 숫자형이 아니기에 Object type
print(data[data["물가"].isnull()])
print(data[data["물가"] == "미측정"])
print(data["물가"].dtype)
print("----------------------------------------")

# '미측정' -> nan
data["물가"] = data["물가"].replace("미측정", np.nan)
data["집"] = data["집"].replace("미측정", np.nan)
data["공원"] = data["공원"].replace("미측정", np.nan)

# object -> 숫자
data["물가"] = pd.to_numeric(data["물가"])
data["집"] = pd.to_numeric(data["집"])
data["공원"] = pd.to_numeric(data["공원"])
print(data["물가"].mean())
print("----------------------------------------")

# 숫자 -> 글자
# data["물가"] = data["물가"].astype(str)

# 미측정 데이터를 평균값으로
data["물가"] = data["물가"].fillna(data["물가"].mean())
data["집"] = data["집"].fillna(data["집"].mean())
data["공원"] = data["공원"].fillna(data["공원"].mean())

# 물가, 집, 공원의 평균치
data["평균"] = (data["물가"] + data["집"] + data["공원"]) / 3
print(data)
print("----------------------------------------")

# 가장 모기가 심했을 때
print(data[data["평균"] == data["평균"].max()])
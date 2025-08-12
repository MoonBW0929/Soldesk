import pandas as pd
import numpy as np

data = pd.read_csv("C:/moon/data/lnps2.csv", names=["마트이름", "품명", "가격", "날짜", "종류", "구역"])
print(data)

print(data["품명"].isnull())
print(data[data["품명"].isnull()])

# 빈 공간 채우기
data["품명"] = data["품명"].fillna("몰라")
print(data[data["품명"].isnull()])

# 값 없애기
data["품명"] = data["품명"].replace("몰라", np.nan)
print(data[data["품명"].isnull()])
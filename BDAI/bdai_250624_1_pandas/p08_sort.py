import pandas as pd

df = pd.read_csv("C:/moon/titanic.csv")
df = df.set_index(df["Name"])
print(df)
print("------------------------------------")

# index 기준으로 정렬
df = df.sort_index(ascending=False)
print(df)
print("------------------------------------")

# 필드명 순 정렬
df = df.sort_index(axis=1)
print(df)
print("------------------------------------")

# 기타 필드로 정렬
df = df.sort_values(by=["Pclass", "Age"], ascending=[True, False])
print(df[["Pclass", "Age"]])
print("------------------------------------")

# for문 사용
for n in df.index:
    print(df.loc[n])
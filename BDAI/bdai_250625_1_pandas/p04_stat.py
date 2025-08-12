import pandas as pd

data = pd.read_csv("C:/moon/lnps.csv", names=["마트이름", "품명", "가격", "날짜", "종류", "구역"])

print(data["가격"].max())
print(data.loc[data["가격"] == data["가격"].max()])
print(data["가격"].min())
print(data.loc[data["가격"] == data["가격"].min()])
print(data["가격"].mean())
print(data["가격"].median())
# 최빈값 ex) 0 0 -> 번호 최빈값
print(data["가격"].mode())
print(data["가격"].sum())
print(data["가격"].count())
# 분산 -> 모든 값의 (값 - 평균)^2 들의 평균값
print(data["가격"].var())
# 표준 편차
print(data["가격"].std())
print("--------------------------------------------")

# 갖고 있는 미세먼지 데이터
# 미세 + 초미세
data = pd.read_csv("C:/moon/seoulDust 1.csv", names=["년", "월", "일", "시간", "권역", "구", "미세", "초미세", "상태"])

data["총미세먼지"] = data["미세"] + data["초미세"]
print(data)
print("--------------------------------------------")

# 평균
print(data["총미세먼지"].mean())
print("--------------------------------------------")

# 최소값
print(data["총미세먼지"].min())
print("--------------------------------------------")

# 가장 먼지가 적은 곳
print(data[data["총미세먼지"] == data["총미세먼지"].min(), ["권역", "구"]])
print("--------------------------------------------")
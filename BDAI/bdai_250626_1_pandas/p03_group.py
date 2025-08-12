import pandas as pd

# 물가
data = pd.read_csv("C:/moon/data/lnps2.csv", names=["마트이름", "품명", "가격", "날짜", "종류", "구역"])

# 이상한 가격 삭제
data = data[data["가격"] < 34902990]

# 평균가
print(data["가격"].mean())
print("----------------------------------------")

# 종류별 평균가
print(data.groupby("종류")["가격"].mean())
print("----------------------------------------")

# 구의 종류별 평균가
print(data.groupby(["구역", "종류"])["가격"].mean())
print("----------------------------------------")

# 미세먼지
data = pd.read_csv("C:/moon/data/seoulDust 1.csv", names=["년", "월", "일", "시간", "권역", "구", "미세", "초미세", "상태"])
data["먼지평균"] = data["미세"] + data["초미세"]

# 구별 PM10 + PM25 평균
print(data.groupby("구")["먼지평균"].mean())
print("----------------------------------------")

# 권역별 PM10 + PM25 평균
print(data.groupby("권역")["먼지평균"].mean())
print("----------------------------------------")

# 권역의 구별 PM10 + PM25 평균
print(data.groupby(["권역", "구"])["먼지평균"].mean())
print("----------------------------------------")
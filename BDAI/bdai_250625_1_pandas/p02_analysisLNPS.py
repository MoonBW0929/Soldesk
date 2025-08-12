import pandas as pd

lnps = pd.read_csv("C:/moon/lnps.csv", names=["마트이름", "품명", "가격", "날짜", "종류", "구역"])
print(lnps)
print("-----------------------------")

# 마트 이름으로 찾게 세팅
lnps = lnps.set_index(lnps["마트이름"])
# 마트 이름 가나다순 정렬
lnps = lnps.sort_index()
# 출력
print(lnps)
print("-----------------------------")

# 통인 시장 데이터만
print(lnps.loc["통인시장"])
print("-----------------------------")

# 마트 명에 '농협'이 들어간 데이터만
print(lnps[lnps["마트이름"].str.contains("농협")])
print("-----------------------------")

# 사과는 어떤 마트에서 구매 가능한가
print(lnps.loc[lnps["품명"].str.contains("사과"), ["마트이름", "품명"]])
print("-----------------------------")

# 품명 가나다순, 가격 비싼순 정렬
lnps = lnps.sort_values(by=["품명", "가격"], ascending=[True, False])
print(lnps)
print("-----------------------------")

# 30000원 이상인 제품의 품명, 가격
print(lnps.loc[lnps["가격"] >= 30000, ["품명", "가격"]])
print("-----------------------------")

# 종로구 데이터만 반복문으로 하나씩 출력
print(lnps[lnps["구역"] == "종로구"].index)
for i, j in enumerate(lnps[lnps["구역"] == "종로구"].index):
    print(lnps.iloc[j])
    break
print("-----------------------------")

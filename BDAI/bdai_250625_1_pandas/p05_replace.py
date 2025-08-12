import pandas as pd

data = pd.read_csv("C:/moon/lnps.csv", names=["마트이름", "품명", "가격", "날짜", "종류", "구역"])
print(data)

# 전통시장 -> 시장
# data = data.replace("전통시장", "시장")
data["종류"] = data["종류"].replace("전통시장", "시장")

# 구로구 -> ㄱㄹㄱ, 성동구 -> ㅅㄷㄱ
data["구역"] = data["구역"].replace(["구로구", "성동구"], ["ㄱㄹㄱ", "ㅅㄷㄱ"])
data["구역"] = data["구역"].replace({"ㄱㄹㄱ" : "구로구", "ㅅㄷㄱ" : "성동구"})

# 구역 필드에서 구로구, 성동구 -> 서울
data["구역"] = data["구역"].replace(["구로구", "성동구"], "서울")

# 필드명 수정 (마트 -> 시장명, 품명 -> 상품명)
data = data.rename(columns={"마트이름" : "시장명", "품명" : "상품명"})

print(data)
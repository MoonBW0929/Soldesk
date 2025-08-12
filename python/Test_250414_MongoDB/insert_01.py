from pymongo import MongoClient


# MongoDB 서버 연결
con = MongoClient("195.168.9.125")
# DB에 moon영역 접속
db = con.moon

# 데이터 확보
name = input("과자 이름 : ")
price = int(input("과자 가격 : "))

# 데이터 삽입 + 결과 받기
result = db.apr14_snack.insert_one({"s_name" : name, "s_price" : price})

# 결과 확인
if result.acknowledged:
    print("성공")

con.close()
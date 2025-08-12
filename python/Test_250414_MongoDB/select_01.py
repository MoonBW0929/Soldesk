from pymongo import ASCENDING, DESCENDING, MongoClient


# MongoDB 서버 연결
con = MongoClient("195.168.9.125")
# DB에 moon영역 접속
db = con.moon

# 데이터 조회 + 정렬
snack = db.apr14_snack.find().sort([("s_price", DESCENDING), ("s_name", ASCENDING)])

# 데이터 확인
for i in snack:
    print(i["s_name"], end="")
    print(i["s_price"])

con.close()
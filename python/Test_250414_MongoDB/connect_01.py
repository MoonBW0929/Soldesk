from pymongo import MongoClient


# MongoDB 서버 연결
con = MongoClient("195.168.9.125")
# DB에 moon영역 접속
db = con.moon

con.close()
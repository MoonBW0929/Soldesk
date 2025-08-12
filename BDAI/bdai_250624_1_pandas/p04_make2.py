from sqlite3 import connect
import pandas as pd

a = pd.read_csv("C:\\moon\\titanic.csv")
print(a)
print("------------------------------------------")

b = pd.read_csv(
    "C:\\moon\\seoulDust 1.csv",
    names=["년", "월", "일", "시", "권역", "구", "미세먼지", "초미세먼지", "상태"],
)
print(b)
print("------------------------------------------")

c = pd.read_csv("C:/moon/naverNews/naverNews.txt", sep="\t", names=["제목", "내용"])
print(c)
print("------------------------------------------")

# con = connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")
# sql = "SELECT * FROM seoul_dust"
# d = pd.read_sql(sql, con)
# print(d)
# print("------------------------------------------")
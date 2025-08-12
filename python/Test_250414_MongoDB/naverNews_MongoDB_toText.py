from pymongo import MongoClient
from moon_library.moon_string_clear import MoonStringClear

con = MongoClient("195.168.9.125")
db = con.moon

news_txt = open("C:\\moon\\naverNews\\naverNews.txt", "a", encoding="utf-8")

news = db.naver_News.find()

for n in news:
    news_txt.write(n["title"])
    news_txt.write("\t")
    news_txt.write(n["description"])
    news_txt.write("\n")

news_txt.close()
con.close()
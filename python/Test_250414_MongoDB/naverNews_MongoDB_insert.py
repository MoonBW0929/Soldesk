from http.client import HTTPSConnection
from urllib.parse import quote
from xml.etree.ElementTree import fromstring

from pymongo import MongoClient
from moon_library.moon_string_clear import MoonStringClear

quest = quote("취업")
cl_info = {"X-Naver-Client-Id":"nntI_nxnVB4ezKsEAuia", "X-Naver-Client-Secret":"l4v1cM4ruS"}

Ns = HTTPSConnection("openapi.naver.com")
Ns.request("GET", "/v1/search/news.xml?query=" + quest, headers=cl_info)

res_data = Ns.getresponse().read()
str_data = fromstring(res_data)

con = MongoClient("195.168.9.125")
db = con.moon

news_data = str_data.iter("item")
for news in news_data:
    title = MoonStringClear.clear(news.find("title").text)
    des = MoonStringClear.clear(news.find("description").text)
    db.naver_News.insert_one({"title" : title, "description" : des})

con.close()
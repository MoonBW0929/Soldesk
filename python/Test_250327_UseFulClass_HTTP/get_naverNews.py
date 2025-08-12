# 네이버 뉴스 가져오기
# client ID : nntI_nxnVB4ezKsEAuia
# client secret : l4v1cM4ruS
# Domain : https://openapi.naver.com/v1/search/news.xml

from http.client import HTTPSConnection
from urllib.parse import quote
from xml.etree.ElementTree import fromstring
from moon.moon_string_clear import MoonStringClear

quest = quote("산불")
cl_info = {"X-Naver-Client-Id":"nntI_nxnVB4ezKsEAuia", "X-Naver-Client-Secret":"l4v1cM4ruS"}

Ns = HTTPSConnection("openapi.naver.com")
Ns.request("GET", "/v1/search/news.xml?query=" + quest, headers=cl_info)

res_data = Ns.getresponse().read()
str_data = fromstring(res_data)

news_data = str_data.iter("item")
for news in news_data:
    print(MoonStringClear.clear(news.find("title").text))
    print(MoonStringClear.clear(news.find("description").text))
    print("---------------------------------------------------")
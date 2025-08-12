# https://news.daum.net/

from http.client import HTTPSConnection

from bs4 import BeautifulSoup


h_con = HTTPSConnection("news.daum.net")
h_con.request("GET", "/")

res_data = h_con.getresponse().read()

data = BeautifulSoup(res_data, "html.parser", from_encoding="utf-8")
tit_txt = data.select(".item_newsblock .tit_txt, .item_newsheadline2 .tit_txt")

for s in tit_txt:
    print(s.text)

h_con.close()
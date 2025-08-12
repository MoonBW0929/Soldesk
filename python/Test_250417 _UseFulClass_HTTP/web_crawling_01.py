# https://sd-beanmouse.duckdns.org

from http.client import HTTPSConnection

from bs4 import BeautifulSoup


h_con = HTTPSConnection("sd-beanmouse.duckdns.org")
h_con.request("GET", "/")

res_data = h_con.getresponse().read()

cafe_data = BeautifulSoup(res_data, "html.parser", from_encoding="utf-8")
txtTd = cafe_data.select(".txtTd")

for s in txtTd:
    print(s.text)

h_con.close()
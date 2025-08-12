# 현재 날씨 데이터 받아오기
# https://openweathermap.org/current
# lat : 위도
# lon : 경도
# q : 도시 이름
# units : 표현 단위
# lang : 언어
from http.client import HTTPConnection, HTTPSConnection
from json import loads

lat = "37.5602892"
lon = "127.178839"

wc = HTTPSConnection("api.openweathermap.org")
wc.request("GET",
"/data/2.5/weather?lat=%s&lon=%s&units=metric&lang=kr&appid=baff8f3c6cbc28a4024e336599de28c4" % (lat, lon))

res_data = wc.getresponse().read()

# JSON 데이터를 Python 컬렉션(dictionary)으로
weth_data = loads(res_data)

print(weth_data["weather"][0]["description"])
print(weth_data["main"]["temp"])
print(weth_data["main"]["humidity"])

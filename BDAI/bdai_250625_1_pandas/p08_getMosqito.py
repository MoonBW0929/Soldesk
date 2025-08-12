# 2016 ~ 2024
# 5/1 ~ 10/31
# 날짜,물가,집,공원

from datetime import datetime, timedelta
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

data = HTTPConnection("openapi.seoul.go.kr:8088")
csv = open("C:/moon/data/seoulMosquito.csv", "a", encoding="utf-8")

date = datetime(2016, 4, 30)

while True:

    date = date + timedelta(1)

    if date > datetime(2024, 10, 31):
        break
    if date < datetime(date.year, 5, 1) or date > datetime(date.year, 10, 31):
        continue

    data.request("GET", "/575a4655496b636839386f58586542/xml/MosquitoStatus/1/5/%s" % date.strftime("%Y-%m-%d"))
    res_data = fromstring(data.getresponse().read())
    row_data = res_data.iter("row")

    for d in row_data:
        csv.write(d.find("MOSQUITO_DATE").text + ",")
        csv.write(d.find("MOSQUITO_VALUE_WATER").text + ",")
        csv.write(d.find("MOSQUITO_VALUE_HOUSE").text + ",")
        csv.write(d.find("MOSQUITO_VALUE_PARK").text + "\n")

csv.close()
data.close()
# 서울시 실시간 미세먼지데이터를 저장하는
# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/xml/RealtimeCityAir/1/25/

from datetime import datetime
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring


Gs = HTTPConnection("openapi.seoul.go.kr:8088")
Gs.request("GET", "/575a4655496b636839386f58586542/xml/RealtimeCityAir/1/25/")

Gs_res = Gs.getresponse()
res_data = fromstring(Gs_res.read())

row_data = res_data.iter("row")
Dust_log = open("C:\\moon\\seoulDust.csv", "a", encoding="utf-8")

date = datetime.today()
date = date.strftime("%Y,%m,%d,%H,")

for d in row_data:
        Dust_log.write(date)
        Dust_log.write(d.find("MSRRGN_NM").text + ",")
        Dust_log.write(d.find("MSRSTE_NM").text + ",")
        Dust_log.write(d.find("PM10").text + ",")
        Dust_log.write(d.find("PM25").text + ",")
        try:
            Dust_log.write(d.find("IDEX_NM").text + "\n")
        except:
            Dust_log.write("None" + "\n")

Dust_log.close()
Gs.close()
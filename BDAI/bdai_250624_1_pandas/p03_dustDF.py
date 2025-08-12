# 서울시 실시간 미세먼지데이터를 저장하는
# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/xml/RealtimeCityAir/1/25/

from json import loads
import pandas as pd
from datetime import datetime
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring


Gs = HTTPConnection("openapi.seoul.go.kr:8088")
Gs.request("GET", "/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25/")

res_data = Gs.getresponse().read()
dust_data = loads(res_data)

pd_dust = pd.DataFrame(dust_data["RealtimeCityAir"]["row"])
print(pd_dust)

Gs.close()
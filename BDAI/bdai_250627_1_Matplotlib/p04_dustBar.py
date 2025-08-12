# 실시간 미세먼지
# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25/

from json import loads
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# plt 기본 폰트 변경
fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False

Gs = HTTPConnection("openapi.seoul.go.kr:8088")
Gs.request("GET", "/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25/")

res_data = Gs.getresponse().read()
dust_data = loads(res_data)

pd_dust = pd.DataFrame(dust_data["RealtimeCityAir"]["row"])
print(pd_dust)

xdata = pd_dust["MSRSTE_NM"].to_numpy()
ydata1 = pd_dust["PM10"].to_numpy()
ydata2 = pd_dust["PM25"].to_numpy()

plt.bar(xdata, ydata1, color="green")
plt.bar(xdata, ydata2, bottom=ydata1)
plt.title("서울시 미세먼지")

plt.show()

Gs.close()
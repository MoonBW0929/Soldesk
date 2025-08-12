# 실시간 미세먼지
# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/json/CardSubwayPayFree/1/1/201501

from json import load, loads
from http.client import HTTPConnection

Gs = HTTPConnection("openapi.seoul.go.kr:8088")
csv = open("C:/moon/data/cspf.csv", "a", encoding="utf-8")
year = 2015
month = 1

while True:
    if month < 10:
        s_month = "0%d" % month
    else:
        s_month = "%d" % month
    Gs.request("GET", "/575a4655496b636839386f58586542/json/CardSubwayPayFree/1/1000/%d%s" % (year, s_month))

    res_data = Gs.getresponse().read()

    for d in loads(res_data)["CardSubwayPayFree"]["row"]:
        csv.write(d["USE_MM"] + ",")
        csv.write(d["SBWY_ROUT_LN_NM"] + ",")
        csv.write(d["STTN"] + ",")
        csv.write("%d," % d["RMIO_GTON_NOPE"])
        csv.write("%d," % d["FREECHRG_GTON_NOPE"])
        csv.write("%d," % d["RMIO_GTOFF_NOPE"])
        csv.write("%d\n" % d["FREECHRG_GTOFF_NOPE"])

    month += 1
    if month > 12:
        if year == 2024:
            break
        month = 1
        year += 1

csv.close()
Gs.close()
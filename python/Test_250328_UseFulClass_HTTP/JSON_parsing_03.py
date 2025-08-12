# 버스 운행 정보 저장
# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/json/CardBusStatisticsServiceNew/1/5/20151101/
 

from datetime import datetime, timedelta
from http.client import HTTPConnection
from json import loads

start_n = 1
end_n = 1000
start_year = 2018
date = datetime(start_year,1,1)

bc = HTTPConnection("openapi.seoul.go.kr:8088")
bus_log = open(("C:\\moon\\bus_data\\%d_bus.csv" % start_year), "a", encoding="utf-8")

while True:

    bc.request("GET", "/575a4655496b636839386f58586542/json/CardBusStatisticsServiceNew/%s/%s/%s/"
           % (str(start_n), str(end_n), date.strftime("%Y%m%d")))

    res_data = bc.getresponse().read()
    bus_data = loads(res_data)

    try:
        if bus_data["RESULT"]:
            print(date.strftime("%Y_%m_%d end"))
            date += timedelta(1)
            start_n = 1
            end_n = 1000
    except:
        for bus in bus_data["CardBusStatisticsServiceNew"]["row"]:
            y = bus["USE_YMD"][0:4]
            m = bus["USE_YMD"][4:6]
            d = bus["USE_YMD"][6:8]
            rte_nm = bus["RTE_NM"].replace(",", ".")
            sb_nm = bus["SBWY_STNS_NM"].replace(",", ".")
            on_tnope = int(bus["GTON_TNOPE"])
            off_tnope = int(bus["GTOFF_TNOPE"])
            bus_log.write("%s,%s,%s,%s,%s,%d,%d\n" % (y, m, d, rte_nm, sb_nm, on_tnope, off_tnope))

        start_n += 1000
        end_n += 1000

    if date == datetime(start_year+1,1,1):
        break

bus_log.close()
bc.close()

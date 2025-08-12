# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/xml/CardSubwayStatsNew/1/5/20151101/
# 2015/01/01 ~ 2024/12/31 전체 지하철 운행정보 저장
# 2015,01,01,1호선,서울역,45000,30000

from datetime import datetime, timedelta
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

date = datetime(2015,1,1)

sub_connect = HTTPConnection("openapi.seoul.go.kr:8088")
sub_log = open("C:\\moon\\subway.csv", "a", encoding="utf-8")

while True:
    sub_connect.request("GET", "/575a4655496b636839386f58586542/xml/CardSubwayStatsNew/1/1000/" + date.strftime("%Y%m%d") + "/")

    res_data = sub_connect.getresponse().read()
    sub_data = fromstring(res_data).iter("row")

    for sub in sub_data:
        l = sub.find("SBWY_ROUT_LN_NM").text.replace(",", ".")
        st = sub.find("SBWY_STNS_NM").text.replace(",", ".")
        on_tnope = sub.find("GTON_TNOPE").text
        off_tnope = sub.find("GTOFF_TNOPE").text
        sub_log.write("%s,%s,%s,%s,%s\n" % (date.strftime("%Y,%m,%d"), l, st, on_tnope, off_tnope))
    sub_log.write("\n")

    if date == datetime(2024,12,31):
        break
    
    date += timedelta(1)

sub_log.close()
sub_connect.close()
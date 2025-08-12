# data.seoul.go.kr
# 서울시 생필품 농수축산물 가격, 생필품으로 검색
# M_NAME, A_NAME, A_PRICE, P_DATE, M_TYPE_NAME, M_GU_NAME

from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring


data = HTTPConnection("openapi.seoul.go.kr:8088")
csv = open("C:/moon/lnps.csv", "a", encoding="utf-8")

for i in range(1, 893739, 1000):
    data.request("GET", "/575a4655496b636839386f58586542/xml/ListNecessariesPricesService/%d/%d" % (i, i+999))

    res_data = fromstring(data.getresponse().read())
    row_data = res_data.iter("row")

    for d in row_data:
        csv.write(d.find("M_NAME").text.replace(",", "") + ",")
        csv.write(d.find("A_NAME").text.replace(",", "") + ",")
        csv.write(d.find("A_PRICE").text + ",")
        csv.write(d.find("P_DATE").text + ",")
        csv.write(d.find("M_TYPE_NAME").text + ",")
        csv.write(d.find("M_GU_NAME").text + "\n")

csv.close()
data.close()
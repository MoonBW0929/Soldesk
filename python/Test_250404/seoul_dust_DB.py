# 서울시 실시간 미세먼지데이터
# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/xml/RealtimeCityAir/1/25/

from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring
from oracledb import connect

# DB connect
db_con = connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")

# http connect
hp_con = HTTPConnection("openapi.seoul.go.kr:8088")
hp_con.request("GET", "/575a4655496b636839386f58586542/xml/RealtimeCityAir/1/25/")

# GET Dust data
dust_data = fromstring(hp_con.getresponse().read())
row_data = dust_data.iter("row")

# insert to DB
for d in row_data:
    rgn_nm = d.find("MSRRGN_NM").text
    ste_nm = d.find("MSRSTE_NM").text
    pm25 = d.find("PM25").text
    pm10 = d.find("PM10").text
    sts = d.find("IDEX_NM").text

    # SQL
    sql = "INSERT INTO seoul_dust " \
    "VALUES(sysdate, '%s', '%s', %s, %s, '%s')" % (rgn_nm, ste_nm, pm25, pm10, sts)
    cur = db_con.cursor()
    cur.execute(sql)
    cur.close()

db_con.commit()
db_con.close()
hp_con.close()
from http.client import HTTPSConnection
from xml.etree.ElementTree import fromstring
# https://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1111061500 기상청 데이터

# https, Domain
hc = HTTPSConnection("www.kma.go.kr")

# 통신 방식(GET), w/index.do
hc.request("GET", "/wid/queryDFSRSS.jsp?zone=1111061500")

# 응답
res = hc.getresponse()
# 응답 내용 읽기 (XML)
res_body = res.read()
# print(res_body.decode())

res_data = fromstring(res_body)
# 데이터들 찾기 (리스트 형태로 반환)
weather_data = res_data.iter("data")

wea_log = open("C:\\moon\\kmaWeather.csv", "a", encoding="utf-8")

for w in weather_data:
    if w.find("day").text == "1": break
    print(w.find("hour").text) # 데이터 찾기
    print(w.find("temp").text)
    print(w.find("wfKor").text)
    wea_log.write(w.find("hour").text + ",")
    wea_log.write(w.find("temp").text + ",")
    wea_log.write(w.find("wfKor").text + "\n")
    print("--------------")

wea_log.close()
hc.close()
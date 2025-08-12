from http.client import HTTPSConnection
from xml.etree.ElementTree import fromstring
# https://www.weather.go.kr/w/index.do 기상청
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

for w in weather_data:
    print(w.find("hour").text) # 데이터 찾기
    print(w.find("temp").text)
    print(w.find("wfKor").text)
    print("--------------")

hc.close()
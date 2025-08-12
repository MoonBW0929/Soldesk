# 카카오 정보를 받아와 키워드로 장소 검색하기
# https://dapi.kakao.com/v2/local/search/keyword.${FORMAT}
# x : 경도
# y : 위도

from http.client import HTTPSConnection
from json import loads
from urllib.parse import quote

header = {"Authorization": "KakaoAK c1f71dc8cc391306ea455cf2e1513ed3"}
x = "127.178839"
y = "37.5602892"

query = quote(input("검색 : "))

kc = HTTPSConnection("dapi.kakao.com")
kc.request("GET", "/v2/local/search/keyword.JSON?x=%s&y=%s&query=%s" % (x, y, query), headers=header)

res_data = kc.getresponse().read()
map_data = loads(res_data)

for ls in map_data["documents"]:

    print("------------------------------")
    print("상호명 : %s" % ls["place_name"])
    print("주소 : %s" % ls["address_name"])
    print("거리 : %s" % ls["road_address_name"])
    print("연락처 : %s" % ls["phone"])
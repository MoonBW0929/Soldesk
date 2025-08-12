# 네이버 뉴스 가져오기
# client ID : nntI_nxnVB4ezKsEAuia
# client secret : l4v1cM4ruS
# Domain : https://openapi.naver.com/v1/search/news.xml

from http.client import HTTPSConnection
from urllib.parse import quote

class NaverNewsDAO:

    def get_news(self, keyword):
        query = quote(keyword)
        cl_info = {"X-Naver-Client-Id":"nntI_nxnVB4ezKsEAuia", "X-Naver-Client-Secret":"l4v1cM4ruS"}

        Ns = HTTPSConnection("openapi.naver.com")
        Ns.request("GET", "/v1/search/news.xml?query=" + query, headers=cl_info)

        res_data = Ns.getresponse().read()

        Ns.close()
        
        return res_data
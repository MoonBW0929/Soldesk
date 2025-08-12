from fastapi import FastAPI, Response
from get_naverNews import NaverNewsDAO


news_DAO = NaverNewsDAO()

app = FastAPI()

@app.get("/naver.get.news")
def naver_news(query):

    res_body = news_DAO.get_news(query)
    res_header = {"Access-Control-Allow-Origin" : "*"}

    return Response(res_body, media_type="application/json", headers=res_header)
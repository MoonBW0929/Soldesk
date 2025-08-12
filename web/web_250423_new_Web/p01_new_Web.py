from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse


app = FastAPI()

@app.get("/xml.test")
def test():

    # xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
    # xml += "<snacks>"
    # xml += "<snack>"
    # xml += "<s_name>빼빼로</s_name>"
    # xml += "<s_price>2000</s_price>"
    # xml += "</snack>"
    # xml += "<snack>"
    # xml += "<s_name>포카칩</s_name>"
    # xml += "<s_price>2500</s_price>"
    # xml += "</snack>"
    # xml += "</snacks>"

    # return Response(xml, media_type="application/xml")

    json = [
        {
            "s_name" : "빼빼로",
            "s_price" : 2000
        },
        {
            "s_name" : "포카칩",
            "s_price" : 2500
        }
    ]

    header = {"Access-Control-Allow-Origin" : "*"}

    return JSONResponse(json, headers=header)
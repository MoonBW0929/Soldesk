from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.get("/html.test")
def html_test():
    html = "<html><head><meta charset=\"utf-8\"><title>html_Res_02</title></head>"
    html += "<body>ㅋㅋㅋㅋㅋ</body></html>"
    return HTMLResponse(html)
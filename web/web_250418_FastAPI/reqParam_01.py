from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.get("/calculate.do")
def cal_do(x:int, y:int):
    html = "<html><head><meta charset=\"utf-8\"><title>html_Res_02</title></head><body>"
    html += "<table border=\"1\">"
    html += "<tr><td>%d + %d = %d</td></tr>" % (x, y, x+y)
    html += "<tr><td>%d - %d = %d</td></tr>" % (x, y, x-y)
    html += "<tr><td>%d x %d = %d</td></tr>" % (x, y, x*y)
    html += "<tr><td>%d / %d = %.1f</td></tr>" % (x, y, x/y)
    html += "</table>"
    html += "</body></html>"
    return HTMLResponse(html)

@app.post("/gugudan.show")
def gugudan(start:int=Form(), end:int=Form()):
    html = "<html><head><meta charset=\"utf-8\"><title>html_Res_02</title></head><body>"
    for j in range(start,end+1):
        html += "<table border=\"1\" style=\"float:left;\">"
        html += "<tr><th>%d단</th></tr>" % j
        for i in range(1,10):
            html += "<tr><td>%d x %d = %d</td></tr>" % (j, i, j*i)
    html += "</table>"
    html += "</body></html>"
    return HTMLResponse(html)
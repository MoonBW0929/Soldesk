from flask import Flask, request

app = Flask(__name__)

@app.get("/te.st")
def test():
    html = "<html><head><meta charset=\"utf-8\"><title>html_Res_02</title></head>"
    html += "<body>ㅋㅋㅋㅋㅋ</body></html>"
    return html

@app.get("/xy.calculate")
def cal():
    a = 10
    b = 20
    html = "<html><head><meta charset=\"utf-8\"><title>html_Res_02</title></head><body>"
    html += "<h1>%d</h1>" % (a+b)
    html += "</body></html>"
    return html

@app.post("/gugudan.show")
def gugudan():
    start = int(request.form["start"])
    end = int(request.form["end"])
    html = "<html><head><meta charset=\"utf-8\"><title>html_Res_02</title></head><body>"
    for j in range(start,end+1):
        html += "<table border=\"1\" style=\"float:left;\">"
        html += "<tr><th>%d단</th></tr>" % j
        for i in range(1,10):
            html += "<tr><td>%d x %d = %d</td></tr>" % (j, i, j*i)
    html += "</table>"
    html += "</body></html>"
    return html

@app.get("/calculate.do")
def cal_do():
    x = int(request.args.get("x"))
    y = int(request.args.get("y"))
    html = "<html><head><meta charset=\"utf-8\"><title>html_Res_02</title></head><body>"
    html += "<table border=\"1\">"
    html += "<tr><td>%d + %d = %d</td></tr>" % (x, y, x+y)
    html += "<tr><td>%d - %d = %d</td></tr>" % (x, y, x-y)
    html += "<tr><td>%d x %d = %d</td></tr>" % (x, y, x*y)
    html += "<tr><td>%d / %d = %.1f</td></tr>" % (x, y, x/y)
    html += "</table>"
    html += "</body></html>"
    return html

if __name__ == "__main__":
    app.run(
        "0.0.0.0",      # 접속 허용 주소
        4567,           # 포트 번호
        debug=True
    )
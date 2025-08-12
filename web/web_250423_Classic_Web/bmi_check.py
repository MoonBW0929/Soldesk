from uuid import uuid4
from fastapi import FastAPI, Form, UploadFile
from fastapi.responses import FileResponse, HTMLResponse


app = FastAPI()

@app.post("/bmicheck.result")
async def file_update(photo:UploadFile, name:str=Form(), height:int=Form(), weight:int=Form()):

    folder = "./photo/"
    content = await photo.read()
    type = photo.filename[-4:]
    file_name = photo.filename.replace(type, "")
    file_name = file_name + str(uuid4()) + type

    f = open(folder + file_name, "wb")
    f.write(content)
    f.close()

    h = height / 100
    bmi = weight / (h * h)

    html = "<html><head><meta charset=\"utf-8\"><title>input</title></head>"
    html += "<body>"
    html += "<h1>비만도 검사 결과</h1><hr>"
    html += "이름 : %s<br>" % name
    html += "키 : %d<br>" % height
    html += "몸무게 : %d<br>" % weight
    html += "bmi : %.1f<br>" % bmi
    html += "<img src=\"file.get?fname=%s\">" % file_name
    html += "</body></html>"

    return HTMLResponse(html)

@app.get("/file.get")
def file_get(fname):
    folder = "./photo/"
    return FileResponse(folder + fname, filename=fname)
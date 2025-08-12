from uuid import uuid4
from fastapi import FastAPI, Form, UploadFile
from fastapi.responses import FileResponse, HTMLResponse


app = FastAPI()

@app.post("/file.up")
async def file_update(photo:UploadFile, title:str=Form("")):
    folder = "./photo/"
    content = await photo.read()
    type = photo.filename[-4:]
    file_name = photo.filename.replace(type, "")
    file_name = file_name + str(uuid4()) + type

    f = open(folder + file_name, "wb")
    f.write(content)
    f.close()

    html = "<html><head><meta charset=\"utf-8\"><title>input</title></head>"
    html += "<body>"
    html += "<h1>%s</h1>" % title
    html += "<img src=\"file.get?fname=%s\">" % file_name
    html += "<hr>"
    html += "<a href=\"file.get?fname=%s\">%s</a>" % (file_name, title)
    html += "</body></html>"
    return HTMLResponse(html)

@app.get("/file.get")
def file_get(fname):
    folder = "./photo/"
    return FileResponse(folder + fname, filename=fname)
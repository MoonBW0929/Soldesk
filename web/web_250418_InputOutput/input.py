from typing import Optional
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.post("/member.sign.up")
def member_sign_up(id:str=Form(), pw:str=Form(),
                   gender:str=Form(), addr:str=Form(),
                   hobby:Optional[list[str]]=Form(None),
                   comment:str=Form()):
    html = "<html><head><meta charset=\"utf-8\"><title>input</title></head>"
    html += "<body>%s %s %s %s" % (id, pw, gender, addr)
    if hobby != None:
        for h in hobby:
            html += " %s" % h
    html += " %s" % comment.replace("\r\n", "<br>")
    html += "</body></html>"
    return HTMLResponse(html)
from fastapi import FastAPI, Form, UploadFile
from fastapi.responses import JSONResponse
from calculation import Calculation
from photo_upload import Photo_upload

app = FastAPI()

photo_uploader = Photo_upload()

@app.get("/calculation")
def calculation(x, y):
    res_body = Calculation.cal(x, y)

    res_header = {"Access-Control-Allow-Origin" : "*"}

    return JSONResponse(res_body, headers=res_header)

@app.post("/calculation.post")
def calculation(x:int=Form(), y:int=Form()):
    res_body = Calculation.cal(x, y)

    res_header = {
        "Access-Control-Allow-Origin" : "http://195.168.9.125:3000",
        "Access-Control-Allow-Credentials" : "true",
    }

    return JSONResponse(res_body, headers=res_header)

@app.post("/photo.upload")
async def photo_upload(photo:UploadFile, title:str=Form()):

    res_body = await photo_uploader.upload(title, photo)

    res_header = {
        "Access-Control-Allow-Origin" : "http://195.168.9.125:3000",
        "Access-Control-Allow-Credentials" : "true",
    }

    return JSONResponse(res_body, headers=res_header)

@app.post("/photo.download")
def photo_download(photo):

    res_body = photo_uploader.download(photo)

    res_header = {
        "Access-Control-Allow-Origin" : "http://195.168.9.125:3000",
        "Access-Control-Allow-Credentials" : "true",
    }

    return JSONResponse(res_body, headers=res_header)
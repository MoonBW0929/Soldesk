from fastapi import FastAPI, Form, UploadFile
from weather.Weather_Photo import Weather_Photo

app = FastAPI()
weather_uploader = Weather_Photo()

@app.post("/weather.reg")
async def reg_weather(img:UploadFile, sts:str=Form(), temp:int=Form()):
    return await weather_uploader.reg_weather(sts, temp, img)

@app.get("/weather.get.img")
def get_weahter_img(img):
    return weather_uploader.get_weather_img(img)
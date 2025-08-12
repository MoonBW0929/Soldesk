from datetime import datetime
from fastapi.responses import FileResponse, JSONResponse


class Weather_Photo:
    def __init__(self):
        self.dir = "./weather/img/"

    async def reg_weather(self, sts, temp, img):

        date = datetime.strftime(datetime.today(), "%Y%m%d%H%M%S")

        file = await img.read()
        file_name = img.filename
        type = img.filename[-4:]
        file_name = img.filename.replace(type, "")
        file_name += date + type

        f = open(self.dir + file_name, "wb")
        f.write(file)
        f.close()

        res_body = {
            "result": True,
            "sts": sts,
            "temp": temp,
            "img": file_name,
        }

        res_header = {
            "Access-Control-Allow-Origin" : "http://195.168.9.125:3000",
            "Access-Control-Allow-Credentials" : "true",
        }

        return JSONResponse(res_body, headers=res_header)
    
    def get_weather_img(self, img):

        return FileResponse(self.dir + img, filename=img)
from fastapi import FastAPI, Form, UploadFile
from fastapi.responses import JSONResponse
from consumption_manage_DAO import Consumption_manage_DAO


app = FastAPI()
c_dao = Consumption_manage_DAO()

@app.get("/te.st")
def test(price, detail, date):

    max = c_dao.get_consumption_reg_cnt()

    res_body = {
        "max_no" : max,
        "price" : price,
        "detail" : detail,
        "date" : date.replace("T", " ")
    }
    res_header = {"Access-Control-Allow-Origin" : "*"}

    return JSONResponse(res_body, headers=res_header)


@app.post("/consumption.reg")
async def reg_consumption(img:UploadFile, detail:str=Form(), price:str=Form(), date:str=Form()):

    if await c_dao.reg_consumption(detail, price, date, img):
        res_body = {
            "result" : True
        }
    else :
        res_body = {
            "result" : False
        }
    
    res_header = {
        "Access-Control-Allow-Origin" : "http://195.168.9.125:3000",
        "Access-Control-Allow-Credentials" : "true",
    }

    return JSONResponse(res_body, headers=res_header)


@app.get("/consumption.get")
def get_consumption(page):

    list = c_dao.get_consumption(page)

    if list != False:

        res_body = {
            "result" : True,
            "month_cnt" : c_dao.month_cnt,
            "consumption" : list
        }
    else :
        res_body = {
            "result" : False
        }
    
    res_header = {"Access-Control-Allow-Origin" : "*"}

    return JSONResponse(res_body, headers=res_header)

@app.get("/consumption.month.cnt.get")
def get_consumption():

    cnt = c_dao.get_consumption_month_cnt()

    if list != False:

        res_body = {
            "result" : True,
            "month_cnt" : cnt,
        }
    else :
        res_body = {
            "result" : False
        }
    
    res_header = {"Access-Control-Allow-Origin" : "*"}

    return JSONResponse(res_body, headers=res_header)

@app.get("/consumption.get.all")
def get_all_consumption():

    list = c_dao.get_all_consumption()

    if list != False:

        res_body = {
            "result" : True,
            "consumption" : list
        }
    else :
        res_body = {
            "result" : False
        }
    
    res_header = {"Access-Control-Allow-Origin" : "*"}

    return JSONResponse(res_body, headers=res_header)


@app.get("/consumption.get.img")
def get_consumption_img(img):
    return c_dao.get_consumption_img(img)


@app.get("/consumption.search")
def search_consumption(keyword):

    list = c_dao.search_consumption(keyword)

    if list != False:

        res_body = {
            "result" : True,
            "consumption" : list
        }
    else :
        res_body = {
            "result" : False
        }
    
    res_header = {"Access-Control-Allow-Origin" : "*"}

    return JSONResponse(res_body, headers=res_header)


@app.get("/consumption.search.detail")
def search_detail_consumption(no):

    list = c_dao.search_detail_consumption(no)

    if list != False:

        res_body = {
            "result" : True,
            "consumption" : list
        }
    else :
        res_body = {
            "result" : False
        }
    
    res_header = {"Access-Control-Allow-Origin" : "*"}

    return JSONResponse(res_body, headers=res_header)


@app.get("/consumption.del")
def del_consumption(no):

    if c_dao.del_consumption(no):
        res_body = {
            "result" : True
        }
    else :
        res_body = {
            "result" : False
        }
    
    res_header = {"Access-Control-Allow-Origin" : "*"}

    return JSONResponse(res_body, headers=res_header)

@app.get("/consumption.mdf")
def modify_consumption(no, detail, price, date):

    if c_dao.modify_consumption(no, detail, price, date):
        res_body = {
            "result" : True
        }
    else :
        res_body = {
            "result" : False
        }
    
    res_header = {"Access-Control-Allow-Origin" : "*"}

    return JSONResponse(res_body, headers=res_header)
from fastapi import FastAPI
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


@app.get("/consumption.reg")
def reg_consumption(price, detail, date):

    if c_dao.reg_consumption(price, detail, date):
        res_body = {
            "execute_ok" : True
        }
    else :
        res_body = {
            "execute_ok" : False
        }
    
    res_header = {"Access-Control-Allow-Origin" : "*"}

    return JSONResponse(res_body, headers=res_header)


@app.get("/consumption.get")
def get_consumption(page):

    list = c_dao.get_consumption(page)

    if list != False:

        res_body = {
            "execute_ok" : True,
            "month_cnt" : c_dao.month_cnt,
            "consumption" : list
        }
    else :
        res_body = {
            "execute_ok" : False
        }
    
    res_header = {"Access-Control-Allow-Origin" : "*"}

    return JSONResponse(res_body, headers=res_header)


@app.get("/consumption.search")
def search_consumption(keyword):

    list = c_dao.search_consumption(keyword)

    if list != False:

        res_body = {
            "execute_ok" : True,
            "consumption" : list
        }
    else :
        res_body = {
            "execute_ok" : False
        }
    
    res_header = {"Access-Control-Allow-Origin" : "*"}

    return JSONResponse(res_body, headers=res_header)


@app.get("/consumption.search.detail")
def search_detail_consumption(no):

    list = c_dao.search_detail_consumption(no)

    if list != False:

        res_body = {
            "execute_ok" : True,
            "consumption" : list
        }
    else :
        res_body = {
            "execute_ok" : False
        }
    
    res_header = {"Access-Control-Allow-Origin" : "*"}

    return JSONResponse(res_body, headers=res_header)


@app.get("/consumption.del")
def del_consumption(no):

    if c_dao.del_consumption(no):
        res_body = {
            "execute_ok" : True
        }
    else :
        res_body = {
            "execute_ok" : False
        }
    
    res_header = {"Access-Control-Allow-Origin" : "*"}

    return JSONResponse(res_body, headers=res_header)

@app.get("/consumption.mdf")
def modify_consumption(no, detail, price, date):

    if c_dao.modify_consumption(no, detail, price, date):
        res_body = {
            "execute_ok" : True
        }
    else :
        res_body = {
            "execute_ok" : False
        }
    
    res_header = {"Access-Control-Allow-Origin" : "*"}

    return JSONResponse(res_body, headers=res_header)
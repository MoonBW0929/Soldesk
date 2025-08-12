from fastapi import FastAPI, Form, UploadFile
from fastapi.responses import JSONResponse
from eat_log_DAO import EatLog_DAO


app = FastAPI()
c_dao = EatLog_DAO()


@app.post("/eatLog.reg")
async def reg_eatLog(img:UploadFile, detail:str=Form(), price:str=Form(), date:str=Form()):

    if await c_dao.reg_eatLog(detail, price, date, img):
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


@app.get("/eatLog.get.today")
def get_eatLog_today(table):

    list = c_dao.get_eatLog_today(table)

    if list != False:

        res_body = {
            "result" : True,
            "month_cnt" : c_dao.month_cnt,
            "eatLog" : list
        }
    else :
        res_body = {
            "result" : False
        }
    
    res_header = {"Access-Control-Allow-Origin" : "*"}

    return JSONResponse(res_body, headers=res_header)


@app.get("/eatLog.get.month")
def get_eatLog_month(page):

    list = c_dao.get_eatLog_month(page)

    if list != False:

        res_body = {
            "result" : True,
            "month_cnt" : c_dao.month_cnt,
            "eatLog" : list
        }
    else :
        res_body = {
            "result" : False
        }
    
    res_header = {"Access-Control-Allow-Origin" : "*"}

    return JSONResponse(res_body, headers=res_header)


@app.get("/eatLog.monthCnt.get")
def get_eatLog():

    cnt = c_dao.get_eatLog_month_cnt()

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


@app.get("/eatLog.get.all")
def get_all_eatLog():

    list = c_dao.get_all_eatLog()

    if list != False:

        res_body = {
            "result" : True,
            "eatLog" : list
        }
    else :
        res_body = {
            "result" : False
        }
    
    res_header = {"Access-Control-Allow-Origin" : "*"}

    return JSONResponse(res_body, headers=res_header)


@app.get("/eatLog.get.img")
def get_eatLog_img(img):
    return c_dao.get_eatLog_img(img)


@app.get("/eatLog.del")
def del_eatLog(no):

    if c_dao.del_eatLog(no):
        res_body = {
            "result" : True
        }
    else :
        res_body = {
            "result" : False
        }
    
    res_header = {"Access-Control-Allow-Origin" : "*"}

    return JSONResponse(res_body, headers=res_header)


@app.post("/account.reg")
async def account_reg(img:UploadFile, id:str=Form(), pw:str=Form(), name:str=Form(), birth:str=Form()):
    
    if await c_dao.reg_account(id, pw, name, birth, img):
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

@app.get("/account.duplicate")
def account_duplicate(txt, type):

    if c_dao.dupli_check_account(txt, type):
        res_body = {
            "result" : True
        }
    else :
        res_body = {
            "result" : False
        }

    res_header = {"Access-Control-Allow-Origin" : "*"}

    return JSONResponse(res_body, headers=res_header)


@app.get("/account.login")
def login_account(id, pw):
    return c_dao.login_account(id, pw)


@app.get("/account.get.info")
def get_Info_account(token):

    res_body = c_dao.get_Info_account(token)

    res_header = {"Access-Control-Allow-Origin" : "*"}

    return JSONResponse(res_body, headers=res_header)

@app.get("/account.login.update")
def login_update_account(token):
    return c_dao.login_update_account(token)

@app.get("/account.update")
def update_account(id, content, value):
    return c_dao.update_account(id, content, value)

@app.post("/account.update.profile")
async def update_account(img:UploadFile, id:str=Form(), prevImg:str=Form()):
    return await c_dao.update_account_img(id, img, prevImg)

@app.get("/account.delete")
def delete_account(id, table):
    return c_dao.delete_account(id, table)

# @app.get("/eatLog.search")
# def search_eatLog(keyword):

#     list = c_dao.search_eatLog(keyword)

#     if list != False:

#         res_body = {
#             "result" : True,
#             "eatLog" : list
#         }
#     else :
#         res_body = {
#             "result" : False
#         }
    
#     res_header = {"Access-Control-Allow-Origin" : "*"}

#     return JSONResponse(res_body, headers=res_header)


# @app.get("/eatLog.search.detail")
# def search_detail_eatLog(no):

#     list = c_dao.search_detail_eatLog(no)

#     if list != False:

#         res_body = {
#             "result" : True,
#             "eatLog" : list
#         }
#     else :
#         res_body = {
#             "result" : False
#         }
    
#     res_header = {"Access-Control-Allow-Origin" : "*"}

#     return JSONResponse(res_body, headers=res_header)
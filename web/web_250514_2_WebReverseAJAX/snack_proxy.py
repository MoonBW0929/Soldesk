from fastapi import FastAPI
from fastapi.responses import JSONResponse
from snack_DAO import Snack_DAO


app = FastAPI()
s_dao = Snack_DAO()

@app.get("/snack.reg")
def reg_snack(name, price):

    if s_dao.reg_snack(name, price):
        res_body = {
            "execute_ok" : True
        }
    else :
        res_body = {
            "execute_ok" : False
        }
    
    res_header = {"Access-Control-Allow-Origin" : "*"}

    return JSONResponse(res_body, headers=res_header)


@app.get("/snack.get")
def get_snack():

    list = s_dao.get_snack()

    if list != False:

        res_body = {
            "execute_ok" : True,
            "snack" : list
        }
    else :
        res_body = {
            "execute_ok" : False
        }
    
    res_header = {"Access-Control-Allow-Origin" : "*"}

    return JSONResponse(res_body, headers=res_header)


# @app.get("/snack.search")
# def search_snack(keyword):

#     list = c_dao.search_snack(keyword)

#     if list != False:

#         res_body = {
#             "execute_ok" : True,
#             "snack" : list
#         }
#     else :
#         res_body = {
#             "execute_ok" : False
#         }
    
#     res_header = {"Access-Control-Allow-Origin" : "*"}

#     return JSONResponse(res_body, headers=res_header)


# @app.get("/snack.search.detail")
# def search_detail_snack(no):

#     list = c_dao.search_detail_snack(no)

#     if list != False:

#         res_body = {
#             "execute_ok" : True,
#             "snack" : list
#         }
#     else :
#         res_body = {
#             "execute_ok" : False
#         }
    
#     res_header = {"Access-Control-Allow-Origin" : "*"}

#     return JSONResponse(res_body, headers=res_header)


# @app.get("/snack.del")
# def del_snack(no):

#     if c_dao.del_snack(no):
#         res_body = {
#             "execute_ok" : True
#         }
#     else :
#         res_body = {
#             "execute_ok" : False
#         }
    
#     res_header = {"Access-Control-Allow-Origin" : "*"}

#     return JSONResponse(res_body, headers=res_header)

# @app.get("/snack.mdf")
# def modify_snack(no, detail, price, date):

#     if c_dao.modify_snack(no, detail, price, date):
#         res_body = {
#             "execute_ok" : True
#         }
#     else :
#         res_body = {
#             "execute_ok" : False
#         }
    
#     res_header = {"Access-Control-Allow-Origin" : "*"}

#     return JSONResponse(res_body, headers=res_header)
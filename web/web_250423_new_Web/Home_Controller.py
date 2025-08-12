from fastapi import FastAPI
from fastapi.responses import JSONResponse
from product.product_DAO import Product_DAO


app = FastAPI()
p_dao = Product_DAO()

@app.get("/product.get")
def product_get():

    res_body = p_dao.get_product()

    res_header = {"Access-Contor-Allow-Origin" : "*"}

    return JSONResponse(res_body, headers=res_header)

@app.get("/product.reg")
def product_reg(name, price):

    res_body = p_dao.reg_product(name, price)
    res_header = {"Access-Contor-Allow-Origin" : "*"}

    return JSONResponse(res_body, headers=res_header)

@app.get("/product.del")
def product_del(price_t, price_b):

    res_body = p_dao.del_product(price_t, price_b)
    res_header = {"Access-Contor-Allow-Origin" : "*"}

    return JSONResponse(res_body, headers=res_header)
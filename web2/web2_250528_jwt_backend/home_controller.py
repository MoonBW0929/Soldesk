from fastapi import FastAPI

from menu_manage import MenuManage

menu_manager = MenuManage()
app = FastAPI()

@app.get("/menu.reg")
def reg_menu(name, price):
    return menu_manager.reg_menu(name, price)

@app.get("/menu.get")
def get_menu(token):
    return menu_manager.get_menu(token)

@app.get("/menu.update")
def update_menu(token):
    return menu_manager.update_menu(token)
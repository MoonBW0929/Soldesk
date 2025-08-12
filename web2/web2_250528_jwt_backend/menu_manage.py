from datetime import datetime, timedelta, timezone
from fastapi.responses import JSONResponse
import jwt


class MenuManage:

    def __init__(self):
        self.jwt_key = "abcd"
        self.jwt_al = "HS256"

    def reg_menu(self, name, price):

        data = {
            "name" : name,
            "price" : price,
            "exp" : datetime.now(timezone.utc) + timedelta(seconds=10)
        }

        jwtr = jwt.encode(data, self.jwt_key, self.jwt_al)
        
        res_body = {
            "result" : True,
            "jwt" : jwtr
        }

        res_header = {"Access-Control-Allow-Origin" : "*"}

        return JSONResponse(res_body, headers=res_header)
    
    def get_menu(self, token):

        try: 
            menu = jwt.decode(token, self.jwt_key, self.jwt_al)

            res_body = {
                "result" : True,
                "name" : menu["name"],
                "price" : menu["price"],
            }

        except jwt.ExpiredSignatureError:
            res_body = {
                "result" : False,
                "comment" : "이미 만료된 데이터입니다."
            }

        except jwt.DecodeError:
            res_body = {
                "result" : False,
                "comment" : "존재하지 않는 데이터입니다."
            }

        res_header = {"Access-Control-Allow-Origin" : "*"}

        return JSONResponse(res_body, headers=res_header)
    
    def update_menu(self, token):

        try: 
            menu = jwt.decode(token, self.jwt_key, self.jwt_al)

            data = {
                "name" : menu["name"],
                "price" : menu["price"],
                "exp" : datetime.now(timezone.utc) + timedelta(seconds=10)
            }

            jwtr = jwt.encode(data, self.jwt_key, self.jwt_al)
            
            res_body = {
                "result" : True,
                "jwt" : jwtr
            }

        except jwt.ExpiredSignatureError:
            res_body = {
                "result" : False,
                "comment" : "이미 만료된 데이터입니다."
            }

        except jwt.DecodeError:
            res_body = {
                "result" : False,
                "comment" : "존재하지 않는 데이터입니다."
            }

        res_header = {"Access-Control-Allow-Origin" : "*"}

        return JSONResponse(res_body, headers=res_header)
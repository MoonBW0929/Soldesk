from datetime import datetime, timedelta, timezone
from os import remove
from fastapi.responses import FileResponse, JSONResponse
from moon_library.moon_DBManager import MoonDBManager
from moon_library.moon_FileNameGenerator import MoonFileNameGenerator
import jwt


class EatLog_DAO:

    def __init__(self):
        self.reg_cnt = self.get_eatLog_reg_cnt()
        if self.reg_cnt == None: self.reg_cnt = -1

        self.month_cnt = self.get_eatLog_month_cnt()

        self.profile_dir = "./member/profile/"

        self.jwt_key = "abcd"
        self.jwt_al = "HS256"


    def get_eatLog_reg_cnt(self):
        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")
            sql = "SELECT max(c_no) FROM MAY25_CONSUMP"

            db_cur.execute(sql)

            max = 0
            for d in db_cur:
                max = d[0]

            return max

        except Exception:
            return False

        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)


    def get_eatLog_month_cnt(self):
        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")
            sql = "SELECT c_date FROM MAY25_CONSUMP ORDER BY c_date desc"

            db_cur.execute(sql)

            cnt = 0
            month = ""
            for d in db_cur:
                date = datetime.strftime(d[0],"%Y%m%d %H%M")
                
                if (cnt == 0) or (month != date[4:6]):
                    month = date[4:6]
                    cnt += 1

            return cnt

        except Exception as e:
            print(e)
            return False

        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)


    async def reg_eatLog(self, detail, price, date, img):
        
        try:
            file = await img.read()
            if len(file) > 30 * 1024 * 1024:
                raise

            file_name = img.filename
            file_name = MoonFileNameGenerator.generate(file_name, "date")

            f = open(self.profile_dir + file_name, "wb")
            f.write(file)
            f.close()
        
        except:
            return False
        

        try:

            date = date.replace("T", " ")

            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")
            sql =   "INSERT INTO MAY25_CONSUMP " \
                    "values(%d, '%s', %s, to_date('%s', 'YYYY-MM-DD HH24:MI'), '%s')" \
                    "" % (self.reg_cnt+1, detail, price, date, file_name)
            
            db_cur.execute(sql)

            if db_cur.rowcount == 1:
                db_con.commit()
                self.reg_cnt += 1
                return True
            else :
                return False

        except:
            remove(self.profile_dir + file_name)
            return False

        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)


    def get_eatLog_today(self, table):
        try:
            today = datetime.today()

            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")
            sql =   "SELECT * FROM %s " \
                    "ORDER BY c_date desc, c_no asc" \
                    "" % table

            db_cur.execute(sql)

            list = []
            cnt = 0
            month = ""
            page = int(page)
            for no, detail, price, d, img in db_cur:

                date = datetime.strftime(d,"%Y%m%d %H%M")

                if month != date[4:6]:
                    cnt += 1

                if cnt == page:
                    eatLog = {
                        "no" : no,
                        "date" : date,
                        "detail" : detail,
                        "price" : price,
                        "img" : img,
                    }
                    list.append(eatLog)

                elif cnt > page:
                    break

                month = date[4:6]

            return list

        except Exception as e:
            print(e)
            return False

        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)


    def get_eatLog_month(self, page):
        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")
            sql =   "SELECT * FROM MAY25_CONSUMP " \
                    "ORDER BY c_date desc, c_no asc"

            db_cur.execute(sql)

            list = []
            cnt = 0
            month = ""
            page = int(page)
            for no, detail, price, d, img in db_cur:

                date = datetime.strftime(d,"%Y%m%d %H%M")

                if month != date[4:6]:
                    cnt += 1

                if cnt == page:
                    eatLog = {
                        "no" : no,
                        "date" : date,
                        "detail" : detail,
                        "price" : price,
                        "img" : img,
                    }
                    list.append(eatLog)

                elif cnt > page:
                    break

                month = date[4:6]

            return list

        except Exception as e:
            print(e)
            return False

        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)


    def get_eatLog_img(self, img):

        return FileResponse(self.profile_dir + img, filename=img)
    

    def get_eatLog_table_cnt(self):
        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")
            sql = "SELECT count(*) FROM account"

            db_cur.execute(sql)

            cnt = 0
            for d in db_cur:
                cnt = d[0]

            return cnt

        except Exception:
            return False

        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)


    async def reg_account(self, id, pw, name, birth, img):

        
        try:
            file = await img.read()
            if len(file) > 30 * 1024 * 1024:
                raise

            file_name = img.filename
            file_name = MoonFileNameGenerator.generate(file_name, "date")

            f = open(self.profile_dir + file_name, "wb")
            f.write(file)
            f.close()
        
        except:
            return False

        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")

            table_cnt = int(self.get_eatLog_table_cnt())
            if table_cnt == None : table_cnt = 0

            table_name = "eatlog_%d" % (table_cnt+1)

            sql =   "INSERT INTO account " \
                    "values('%s', '%s', '%s', to_date('%s', 'YYYY-MM-DD'), '%s', '%s')" \
                    "" % (id, pw, name, birth, table_name, file_name)
            
            db_cur.execute(sql)

            if db_cur.rowcount == 1:
                db_con.commit()
                self.reg_cnt -= 1
            else :
                return False

        except:
            MoonDBManager.db_disconnect(db_con, db_cur)
            return False
        
        try:
            sql =   "CREATE TABLE %s("\
                        "c_no number(4) PRIMARY KEY, "\
                        "c_store varchar2(100 char) NOT NULL, " \
                        "c_addr varchar2(100 char) NOT NULL, "\
                        "c_price number(10) NOT NULL, "\
                        "c_menu varchar2(50 char) NOT NULL, "\
                        "c_date date NOT NULL, "\
                        "c_img varchar2(300 char) NOT NULL "\
                    ")" % (table_name)
            
            db_cur.execute(sql)

            return True

        except Exception as e:
            print(e)
            return False
        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)

    def dupli_check_account(self, txt, type):
        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")
            sql =   "SELECT count(*) FROM account "\
                    "WHERE %s = '%s'" % (type, txt)

            db_cur.execute(sql)

            cnt = 0
            for d in db_cur:
                cnt = d[0]

            return (cnt == 0)

        except Exception:
            return False

        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)


    def login_account(self, id, password):
        
        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")
            sql =   "SELECT * FROM account " \
                    "WHERE a_id = '%s' " \
                    "" % (id)
            
            db_cur.execute(sql)

            id_check = False
            pw_check = False
            data = {}

            for _, pw, name, birth, table, img in db_cur:
                id_check = True
                if pw == password:
                    pw_check = True
                    birth_s = datetime.strftime(birth,"%Y%m%d")

                    data = {
                        "id" : id,
                        "pw" : password,
                        "name": name,
                        "birth": birth_s,
                        "table": table,
                        "img": img,
                        "exp" : datetime.now(timezone.utc) + timedelta(minutes=20)
                    }

            if not id_check:
                res_body = {
                    "result": False,
                    "err": "존재하지 않는 아이디입니다."
                }
            elif not pw_check :
                res_body = {
                    "result": False,
                    "err": "비밀번호가 일치하지 않습니다."
                }
            else:

                jwtr = jwt.encode(data, self.jwt_key, self.jwt_al)

                res_body = {
                    "result": True,
                    "jwt": jwtr,
                }

            res_header = {"Access-Control-Allow-Origin" : "*"}

            return JSONResponse(res_body, headers=res_header)

        except:
            ex_result = {
                "result": False,
                "err": "서버에 이상이 있습니다, 잠시후 다시 시도해 주십시오."
            }
            return ex_result

        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)

    def get_Info_account(self, token):

        try: 
            info = jwt.decode(token, self.jwt_key, self.jwt_al)

            res_body = {
                "result" : True,
                "id" : info["id"],
                "pw" : info["pw"],
                "name": info["name"],
                "birth": info["birth"],
                "table": info["table"],
                "img": info["img"],
            }

        except jwt.ExpiredSignatureError:
            res_body = {
                "result" : False,
                "err" : "로그인 정보가 만료되었습니다, 다시 로그인하세요"
            }

        except jwt.DecodeError:
            res_body = {
                "result" : False,
                "err" : "",
            }

        return res_body
    

    def login_update_account(self, token):

        try: 
            info = jwt.decode(token, self.jwt_key, self.jwt_al)

            data = {
                "id" : info["id"],
                "pw" : info["pw"],
                "name": info["name"],
                "birth": info["birth"],
                "table": info["table"],
                "img": info["img"],
                "exp" : datetime.now(timezone.utc) + timedelta(minutes=20)
            }

            jwtr = jwt.encode(data, self.jwt_key, self.jwt_al)
            
            res_body = {
                "result" : True,
                "jwt" : jwtr
            }

        except jwt.ExpiredSignatureError:
            res_body = {
                "result" : False,
                "err" : "로그인 정보가 만료되었습니다, 다시 로그인하세요"
            }

        except jwt.DecodeError:
            res_body = {
                "result" : False,
                "err" : "존재하지 않는 데이터입니다."
            }

        res_header = {"Access-Control-Allow-Origin" : "*"}

        return JSONResponse(res_body, headers=res_header)



    def update_account(self, id, content, value):
        
        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")
            sql =   "UPDATE account " \
                    "SET a_%s = '%s' " \
                    "WHERE a_id = '%s' " \
                    "" % (content, value, id)
            
            db_cur.execute(sql)

            if db_cur.rowcount == 1:
                db_con.commit()
            else:
                return {
                    "result": False,
                    "err": "잘못된 요청입니다."
                }
            
        except Exception as e:
            print(e)
            MoonDBManager.db_disconnect(db_con, db_cur)
            return {
                "result": False,
                "err": "서버에 이상이 있습니다, 잠시후 다시 시도해 주세요."
            }

        try:
            sql =   "SELECT * FROM account " \
                    "WHERE a_id = '%s' " \
                    "" % (id)
            
            db_cur.execute(sql)

            data = {}
            for _, pw, name, birth, table, img in db_cur:

                birth_s = datetime.strftime(birth,"%Y%m%d")

                data = {
                    "id" : id,
                    "pw" : pw,
                    "name": name,
                    "birth": birth_s,
                    "table": table,
                    "img": img,
                    "exp" : datetime.now(timezone.utc) + timedelta(minutes=20)
                }

            jwtr = jwt.encode(data, self.jwt_key, self.jwt_al)

            res_body = {
                "result": True,
                "jwt": jwtr,
            }

            res_header = {"Access-Control-Allow-Origin" : "*"}

            return JSONResponse(res_body, headers=res_header)

        except:
            return {
                "result": False,
                "err": "서버에 이상이 있습니다, 잠시후 다시 시도해 주세요."
            }

        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)


    async def update_account_img(self, id, img, prevImg):
        
        try:
            file = await img.read()
            if len(file) > 30 * 1024 * 1024:
                raise

            file_name = img.filename
            file_name = MoonFileNameGenerator.generate(file_name, "date")

            f = open(self.profile_dir + file_name, "wb")
            f.write(file)
            f.close()
        
        except:
            return {
                "result": False,
                "err": "알맞지 않은 파일입니다."
            }


        try:

            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")
            sql =   "UPDATE account " \
                    "SET a_img = '%s' " \
                    "WHERE a_id = '%s' " \
                    "" % (file_name, id)
            
            db_cur.execute(sql)

            if db_cur.rowcount == 1:
                db_con.commit()
            else :
                raise

        except:
            remove(self.profile_dir + file_name)
            return {
                "result": False,
                "err": "서버에 이상이 있습니다, 잠시후 다시 시도해 주세요."
            }


        try:
            sql =   "SELECT * FROM account " \
                    "WHERE a_id = '%s' " \
                    "" % (id)
            
            db_cur.execute(sql)

            data = {}
            for id, pw, name, birth, table, _ in db_cur:

                birth_s = datetime.strftime(birth,"%Y%m%d")

                data = {
                    "id" : id,
                    "pw" : pw,
                    "name": name,
                    "birth": birth_s,
                    "table": table,
                    "img": file_name,
                    "exp" : datetime.now(timezone.utc) + timedelta(minutes=20)
                }

            jwtr = jwt.encode(data, self.jwt_key, self.jwt_al)

            res_body = {
                "result": True,
                "jwt": jwtr,
            }

            res_header = {
                "Access-Control-Allow-Origin" : "http://195.168.9.125:3000",
                "Access-Control-Allow-Credentials" : "true",
            }

            remove(self.profile_dir + prevImg)

            return JSONResponse(res_body, headers=res_header)

        except:
            return {
                "result": False,
                "err": "서버에 이상이 있습니다, 잠시후 다시 시도해 주십시오."
            }

        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)


    def delete_account(self, id, table):
        
        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")
            sql =   "DELETE FROM account " \
                    "WHERE a_id = '%s' " \
                    "" % (id)
            
            db_cur.execute(sql)

            if db_cur.rowcount == 1:
                db_con.commit()
            else:
                return {
                    "result": False,
                    "err": "잘못된 요청입니다."
                }
            
        except:
            MoonDBManager.db_disconnect(db_con, db_cur)
            return {
                "result": False,
                "err": "서버에 이상이 있습니다, 잠시후 다시 시도해 주십시오."
            }

        try:
            sql =   "DROP TABLE %s " \
                    "CASCADE CONSTRAINT purge " \
                    "" % (table)
            
            db_cur.execute(sql)

            res_body = {
                "result": True
            }

            res_header = {"Access-Control-Allow-Origin" : "*"}

            return JSONResponse(res_body, headers=res_header)

        except:
            return {
                "result": False,
                "err": "서버에 이상이 있습니다, 잠시후 다시 시도해 주십시오."
            }

        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)


    # def search_eatLog(self, keyword):
    #     try:
    #         db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")
    #         sql =   "SELECT * FROM MAY25_CONSUMP " \
    #                 "WHERE c_detail LIKE '%%%s%%' " \
    #                 "ORDER BY c_date DESC" % keyword

    #         db_cur.execute(sql)

    #         list = []
    #         for no, d, detail, price in db_cur:

    #             date = datetime.strftime(d,"%Y%m%d %H%M")

    #             eatLog = {
    #                 "no" : no,
    #                 "date" : date,
    #                 "detail" : detail,
    #                 "price" : price
    #             }
    #             list.append(eatLog)

    #         return list

    #     except Exception as e:
    #         print(e)
    #         return False

    #     finally:
    #         MoonDBManager.db_disconnect(db_con, db_cur)


    # def search_detail_eatLog(self, no):
    #     try:
    #         db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")
    #         sql =   "SELECT * FROM MAY25_CONSUMP " \
    #                 "WHERE c_no = %s" % no

    #         db_cur.execute(sql)

    #         list = []
    #         for no, d, detail, price in db_cur:

    #             date = datetime.strftime(d,"%Y%m%d %H%M")

    #             eatLog = {
    #                 "no" : no,
    #                 "date" : date,
    #                 "detail" : detail,
    #                 "price" : price
    #             }
    #             list.append(eatLog)

    #         return list

    #     except Exception as e:
    #         print(e)
    #         return False

    #     finally:
    #         MoonDBManager.db_disconnect(db_con, db_cur)


    # def del_eatLog(self, no):

    #     db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")
        
    #     try:
    #         sql =   "SELECT c_img FROM MAY25_CONSUMP " \
    #                 "WHERE c_no = %s" % (no)
            
    #         db_cur.execute(sql)
    #         img_name = ""
    #         for d in db_cur:
    #             img_name = d[0]

    #         os.remove(self.profile_dir + img_name)

    #     except:
    #         return False

    #     try:
    #         sql =   "DELETE FROM MAY25_CONSUMP " \
    #                 "WHERE c_no = %s" % (no)
            
    #         db_cur.execute(sql)

    #         if db_cur.rowcount == 1:
    #             db_con.commit()
    #             self.reg_cnt -= 1
    #             return True
    #         else :
    #             return False

    #     except Exception as e:
    #         print(e)
    #         return False

    #     finally:
    #         MoonDBManager.db_disconnect(db_con, db_cur)
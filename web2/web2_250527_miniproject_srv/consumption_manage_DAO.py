from datetime import datetime
from os import remove
import os

from fastapi.responses import FileResponse
from moon_library.moon_DBManager import MoonDBManager
from moon_library.moon_FileNameGenerator import MoonFileNameGenerator


class Consumption_manage_DAO:

    def __init__(self):
        self.reg_cnt = self.get_consumption_reg_cnt()
        if self.reg_cnt == None: self.reg_cnt = -1

        self.month_cnt = self.get_consumption_month_cnt()

        self.dir = "./img/"


    def get_consumption_reg_cnt(self):
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


    def get_consumption_month_cnt(self):
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


    async def reg_consumption(self, detail, price, date, img):
        
        try:
            file = await img.read()
            if len(file) > 30 * 1024 * 1024:
                raise

            file_name = img.filename
            file_name = MoonFileNameGenerator.generate(file_name, "date")

            f = open(self.dir + file_name, "wb")
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
            remove(self.dir + file_name)
            return False

        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)


    def get_consumption(self, page):
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
                    consumption = {
                        "no" : no,
                        "date" : date,
                        "detail" : detail,
                        "price" : price,
                        "img" : img,
                    }
                    list.append(consumption)

                elif cnt > page:
                    break

                month = date[4:6]

            return list

        except Exception as e:
            print(e)
            return False

        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)


    def get_all_consumption(self):
        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")
            sql =   "SELECT * FROM MAY25_CONSUMP " \
                    "ORDER BY c_no asc"

            db_cur.execute(sql)

            list = []
            for no, d, detail, price in db_cur:

                date = datetime.strftime(d,"%Y%m%d %H%M")

                consumption = {
                    "no" : no,
                    "date" : date,
                    "detail" : detail,
                    "price" : price
                }
                list.append(consumption)

            return list

        except Exception as e:
            print(e)
            return False

        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)


    def search_consumption(self, keyword):
        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")
            sql =   "SELECT * FROM MAY25_CONSUMP " \
                    "WHERE c_detail LIKE '%%%s%%' " \
                    "ORDER BY c_date DESC" % keyword

            db_cur.execute(sql)

            list = []
            for no, d, detail, price in db_cur:

                date = datetime.strftime(d,"%Y%m%d %H%M")

                consumption = {
                    "no" : no,
                    "date" : date,
                    "detail" : detail,
                    "price" : price
                }
                list.append(consumption)

            return list

        except Exception as e:
            print(e)
            return False

        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)


    def search_detail_consumption(self, no):
        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")
            sql =   "SELECT * FROM MAY25_CONSUMP " \
                    "WHERE c_no = %s" % no

            db_cur.execute(sql)

            list = []
            for no, d, detail, price in db_cur:

                date = datetime.strftime(d,"%Y%m%d %H%M")

                consumption = {
                    "no" : no,
                    "date" : date,
                    "detail" : detail,
                    "price" : price
                }
                list.append(consumption)

            return list

        except Exception as e:
            print(e)
            return False

        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)


    def del_consumption(self, no):

        db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")
        
        try:
            sql =   "SELECT c_img FROM MAY25_CONSUMP " \
                    "WHERE c_no = %s" % (no)
            
            db_cur.execute(sql)
            img_name = ""
            for d in db_cur:
                img_name = d[0]

            os.remove(self.dir + img_name)

        except:
            return False

        try:
            sql =   "DELETE FROM MAY25_CONSUMP " \
                    "WHERE c_no = %s" % (no)
            
            db_cur.execute(sql)

            if db_cur.rowcount == 1:
                db_con.commit()
                self.reg_cnt -= 1
                return True
            else :
                return False

        except Exception as e:
            print(e)
            return False

        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)


    def modify_consumption(self, no, detail, price, date):
        try:

            date = date.replace("T", " ")

            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")
            sql =   "UPDATE MAY25_CONSUMP " \
                    "SET c_price = %s, c_date = to_date('%s', 'YYYY-MM-DD HH24:MI'), c_detail = '%s' " \
                    "WHERE c_no = %s" % (price, date, detail, no)
            
            db_cur.execute(sql)

            if db_cur.rowcount == 1:
                db_con.commit()
                self.reg_cnt += 1
                return True
            else :
                return False

        except Exception as e:
            print(e)
            return False

        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)

    def get_consumption_img(self, img):

        return FileResponse(self.dir + img, filename=img)
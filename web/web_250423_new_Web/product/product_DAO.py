from moon_library.moon_DBManager import MoonDBManager

class Product_DAO:

    def __init__(self):
        pass

    def get_product(self):
        
        try:

            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")

            sql = "SELECT * FROM apr23_product"

            db_cur.execute(sql)

            list = []
            for name, price in db_cur:
                list.append({"name" : name, "price" : price})
            
            return list

        except:
            return None

        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)

    def reg_product(self, name, price):
        
        try:

            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")

            sql = "INSERT INTO apr23_product VALUES('%s', %s)" % (name, price)

            db_cur.execute(sql)

            if db_cur.rowcount == 1:
                db_con.commit()
                return {"result" : "등록 성공"}

            return {"result" : "등록 실패"}

        except:
            return {"result" : "등록 실패"}

        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)
    
    def del_product(self, price_t, price_b):
        
        try:

            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")

            sql =   "DELETE FROM apr23_product WHERE " \
                    "p_price > %s AND p_price < %s" % (price_b, price_t)

            db_cur.execute(sql)

            if db_cur.rowcount > 0:
                db_con.commit()
                return {"result" : "삭제 성공"}

            return {"result" : "삭제 실패"}

        except:
            return {"result" : "삭제 실패"}

        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)
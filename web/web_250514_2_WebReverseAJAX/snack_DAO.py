from datetime import datetime
from moon_library.moon_DBManager import MoonDBManager


class Snack_DAO:

    def __init__(self):
        self.reg_cnt = self.get_snack_reg_cnt()
        if self.reg_cnt == None: self.reg_cnt = -1


    def get_snack_reg_cnt(self):
        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")
            sql = "SELECT max(s_no) FROM may14_snack"

            db_cur.execute(sql)

            max = 0
            for d in db_cur:
                max = d[0]

            return max

        except Exception:
            return False

        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)


    def reg_snack(self, name, price):
        try:

            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")
            sql =   "INSERT INTO may14_snack " \
                    "values(%d, '%s', %s)" \
                    "" % (self.reg_cnt+1, name, price)
            
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


    def get_snack(self):
        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")
            sql =   "SELECT * FROM may14_snack " \
                    "ORDER BY s_no asc"

            db_cur.execute(sql)

            list = []
            for no, name, price in db_cur:
                    
                snack = {
                    "no" : no,
                    "name" : name,
                    "price" : price
                }

                list.append(snack)

            return list

        except Exception as e:
            print(e)
            return False

        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)


    # def search_snack(self, keyword):
    #     try:
    #         db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")
    #         sql =   "SELECT * FROM may07_pay " \
    #                 "WHERE p_pay_detail LIKE '%%%s%%' " \
    #                 "ORDER BY p_date DESC" % keyword

    #         db_cur.execute(sql)

    #         list = []
    #         for no, d, detail, price in db_cur:

    #             date = datetime.strftime(d,"%Y%m%d %H%M")

    #             snack = {
    #                 "no" : no,
    #                 "date" : date,
    #                 "detail" : detail,
    #                 "price" : price
    #             }
    #             list.append(snack)

    #         return list

    #     except Exception as e:
    #         print(e)
    #         return False

    #     finally:
    #         MoonDBManager.db_disconnect(db_con, db_cur)


    # def search_detail_snack(self, no):
    #     try:
    #         db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")
    #         sql =   "SELECT * FROM may07_pay " \
    #                 "WHERE p_no = %s" % no

    #         db_cur.execute(sql)

    #         list = []
    #         for no, d, detail, price in db_cur:

    #             date = datetime.strftime(d,"%Y%m%d %H%M")

    #             snack = {
    #                 "no" : no,
    #                 "date" : date,
    #                 "detail" : detail,
    #                 "price" : price
    #             }
    #             list.append(snack)

    #         return list

    #     except Exception as e:
    #         print(e)
    #         return False

    #     finally:
    #         MoonDBManager.db_disconnect(db_con, db_cur)


    # def del_snack(self, no):
    #     try:
    #         db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")
    #         sql =   "DELETE FROM may07_pay " \
    #                 "WHERE p_no = %s" % (no)
            
    #         db_cur.execute(sql)

    #         if db_cur.rowcount == 1:
    #             db_con.commit()
    #             self.reg_cnt += 1
    #             return True
    #         else :
    #             return False

    #     except Exception as e:
    #         print(e)
    #         return False

    #     finally:
    #         MoonDBManager.db_disconnect(db_con, db_cur)


    # def modify_snack(self, no, detail, price, date):
    #     try:

    #         date = date.replace("T", " ")

    #         db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")
    #         sql =   "UPDATE may07_pay " \
    #                 "SET p_price = %s, p_date = to_date('%s', 'YYYY-MM-DD HH24:MI'), p_pay_detail = '%s' " \
    #                 "WHERE p_no = %s" % (price, date, detail, no)
            
    #         db_cur.execute(sql)

    #         if db_cur.rowcount == 1:
    #             db_con.commit()
    #             self.reg_cnt += 1
    #             return True
    #         else :
    #             return False

    #     except Exception as e:
    #         print(e)
    #         return False

    #     finally:
    #         MoonDBManager.db_disconnect(db_con, db_cur)
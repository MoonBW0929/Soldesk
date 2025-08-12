from datetime import datetime
from moon_library.moon_DBManager import MoonDBManager


class Consumption_manage_DAO:

    def __init__(self):
        self.reg_cnt = self.get_consumption_reg_cnt()
        if self.reg_cnt == None: self.reg_cnt = -1

        self.month_cnt = self.get_consumption_month_cnt()


    def get_consumption_reg_cnt(self):
        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")
            sql = "SELECT max(p_no) FROM MAY07_PAY"

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
            sql = "SELECT p_date FROM MAY07_PAY ORDER BY p_date desc"

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


    def reg_consumption(self, price, detail, date):
        try:

            date = date.replace("T", " ")

            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")
            sql =   "INSERT INTO may07_pay " \
                    "values(%d, to_date('%s', 'YYYY-MM-DD HH24:MI'), '%s', %s)" \
                    "" % (self.reg_cnt+1, date, detail, price)
            
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


    def get_consumption(self, page):
        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")
            sql =   "SELECT * FROM MAY07_PAY " \
                    "ORDER BY p_date desc, p_no asc"

            db_cur.execute(sql)

            list = []
            cnt = 0
            month = ""
            page = int(page)
            for no, d, detail, price in db_cur:

                date = datetime.strftime(d,"%Y%m%d %H%M")

                if month != date[4:6]:
                    cnt += 1

                if cnt == page:
                    consumption = {
                        "no" : no,
                        "date" : date,
                        "detail" : detail,
                        "price" : price
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


    def search_consumption(self, keyword):
        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")
            sql =   "SELECT * FROM may07_pay " \
                    "WHERE p_pay_detail LIKE '%%%s%%' " \
                    "ORDER BY p_date DESC" % keyword

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
            sql =   "SELECT * FROM may07_pay " \
                    "WHERE p_no = %s" % no

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
        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")
            sql =   "DELETE FROM may07_pay " \
                    "WHERE p_no = %s" % (no)
            
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


    def modify_consumption(self, no, detail, price, date):
        try:

            date = date.replace("T", " ")

            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.68:1521/xe")
            sql =   "UPDATE may07_pay " \
                    "SET p_price = %s, p_date = to_date('%s', 'YYYY-MM-DD HH24:MI'), p_pay_detail = '%s' " \
                    "WHERE p_no = %s" % (price, date, detail, no)
            
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
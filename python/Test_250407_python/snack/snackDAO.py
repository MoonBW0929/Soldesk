from math import ceil
from company.company import Company
from snack.snack import Snack
from snack.snakc2 import Snack2
from moon_library.moon_DBManager import MoonDBManager


class SnackDAO:
    
    def __init__(self):
        self.get_snack_count_db()
        self.snack_page = 3

    def add_snack_db(self, sn):
        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")

            sql = "INSERT INTO apr07_snack " \
            "VALUES(%d, '%s', to_date('%s', 'YYYY-MM-DD'), %d, %d, '%s')" % (sn.no, sn.name, sn.date, sn.price, sn.weight, sn.cp)

            db_cur.execute(sql)
            if db_cur.rowcount == 1:
                self.snack_cnt += 1
                db_con.commit()
                return "등록 성공"
            else:
                return "등록 실패"

        except Exception as e:
            print(e)
            return "등록 실패"
        
        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)

    def get_all_snack_db(self):

        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")
            sql = "SELECT * FROM apr07_snack ORDER BY s_no"

            db_cur.execute(sql)

            list = []
            for no, name, date, price, weight, cp in db_cur:
                list.append(Snack(no, name, date, price, weight, cp))

            return list

        except Exception as e:
            print(e)
            return None
        
        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)

    def get_snack_db(self, c_page, keyword):

        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")
            sql =   "SELECT rn, s_no, s_name, s_date, s_price, s_weight, s_company " \
                    "FROM (" \
                        "SELECT rownum AS rn, s_no, s_name, s_date, s_price, s_weight, s_company " \
                        "FROM apr07_snack " \
                        "WHERE s_name LIKE '%%%s%%' " \
                        "ORDER BY s_no" \
                    ") " \
                    "WHERE rn > %d AND rn <= %d" % (keyword, (c_page-1)*self.snack_page, c_page*self.snack_page)

            db_cur.execute(sql)

            list = []
            for _, s_no, s_name, s_date, s_price, s_weight, s_company in db_cur:
                list.append(Snack(s_no, s_name, s_date, s_price, s_weight, s_company))

            return list

        except Exception as e:
            print(e)

        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)

    def get_snack_count_db(self):
        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")
            sql = "SELECT count(*) FROM apr07_snack"

            db_cur.execute(sql)

            count = 0
            for i in db_cur:
                count = i[0]

            self.snack_cnt = count

        except Exception as e:
            print(e)

        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)

    def get_snack_page_db(self, keyword):
        if keyword == "":
            snack_cnt = self.snack_cnt
        else:
            snack_cnt = self.get_snack_search_count_db(keyword)

        page = ceil(snack_cnt / self.snack_page)

        return page
    
    def get_snack_lastNum_db(self):

        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")
            sql = "SELECT max(s_no) FROM apr07_snack"

            db_cur.execute(sql)

            no = 0
            for i in db_cur:
                no = i[0]

            return no
        
        except Exception as e:
            print(e)
        
        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)

    def get_snack_search_count_db(self, keyword):
        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")
            sql =   "SELECT count(*) FROM apr07_snack " \
                    "WHERE s_name LIKE '%%%s%%' OR s_company LIKE '%%%s%%'" % (keyword, keyword)
            
            db_cur.execute(sql)

            count = 0
            for i in db_cur:
                count = i[0]

            return count

        except Exception as e:
            print(e)

        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)

    # def get_snack_info_db(self, c_page, keyword):
    #     try:
    #         db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")
    #         sql =   "SELECT rn, c_name, c_addr, c_ceo, c_employee " \
    #                 "FROM (" \
    #                     "SELECT rownum AS rn, c_name, c_addr, c_ceo, c_employee " \
    #                     "FROM apr07_company " \
    #                     "WHERE c_name = (" \
    #                         "SELECT DISTINCT s_company " \
    #                         "FROM apr07_snack " \
    #                         "WHERE s_name LIKE '%%%s%%' " \
    #                     ") "\
    #                 ") " \
    #                 "WHERE rn > %d AND rn <= %d" % (keyword, (c_page-1)*self.snack_page, c_page*self.snack_page)

    #         db_cur.execute(sql)

    #         list = []
    #         for _, c_name, c_addr, c_ceo, c_emp in db_cur:
    #             list.append(Company(c_name, c_addr, c_ceo, c_emp))

    #         return list

    #     except Exception as e:
    #         print(e)

    #     finally:
    #         MoonDBManager.db_disconnect(db_con, db_cur)

    def get_snack_info_db(self, c_page, keyword):
        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")
            sql =   "SELECT s_no, s_name, s_date, s_price, s_weight, c_name, c_addr, c_ceo, c_employee " \
                    "FROM (" \
                        "SELECT * " \
                        "FROM (" \
                        "SELECT rownum AS rn, s_no, s_name, s_date, s_price, s_weight, s_company " \
                        "FROM apr07_snack " \
                        "WHERE s_name LIKE '%%%s%%' " \
                    ")" \
                    "WHERE rn > %d AND rn <= %d" \
                "), (" \
                        "SELECT * " \
                        "FROM (" \
                        "SELECT rownum AS rn, c_name, c_addr, c_ceo, c_employee " \
                        "FROM apr07_company " \
                        "WHERE c_name in (" \
                            "SELECT DISTINCT s_company " \
                            "FROM apr07_snack " \
                            "WHERE s_name LIKE '%%%s%%'" \
                        ")" \
                    ")" \
                    "WHERE rn > %d AND rn <= %d" \
                ")" \
                "WHERE s_company = c_name" \
                "" % (keyword, (c_page-1)*self.snack_page, c_page*self.snack_page, keyword, (c_page-1)*self.snack_page, c_page*self.snack_page)

            db_cur.execute(sql)

            list = []
            for s_no, s_name, s_date, s_price, s_weight, c_name, c_addr, c_ceo, c_employee in db_cur:
                list.append(Snack2(s_no, s_name, s_date, s_price, s_weight, c_name, c_addr, c_ceo, c_employee))

            return list

        except Exception as e:
            print(e)

        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)

    def update_snack_db(self, keyword, up_num, up_data):
        try:
            if up_num == "1":
                update = "s_name"
            elif up_num == "2":
                update = "s_date"
            elif up_num == "3":
                update = "s_price"
                up_data = int(up_data)
            elif up_num == "4":
                update = "s_weight"
                up_data = int(up_data)
            elif up_num == "5":
                update = "s_company"

            if type(up_data) == int:
                sql =   "UPDATE apr07_snack " \
                    "SET %s = %d " \
                    "WHERE s_name = '%s'" % (update, up_data, keyword)
            else:
                sql =   "UPDATE apr07_snack " \
                    "SET %s = '%s' " \
                    "WHERE s_name = '%s'" % (update, up_data, keyword)

            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")

            db_cur.execute(sql)

            if db_cur.rowcount == 1:
                db_con.commit()
                return "업데이트 성공"
            else:
                return "업데이트 실패"

        except Exception as e:
            print(e)

        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)

    def delete_snack_db(self, keyword):
        try:

            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")
            sql =   "DELETE FROM apr07_snack " \
                    "WHERE s_name = '%s'" % (keyword)
            
            db_cur.execute(sql)

            if db_cur.rowcount == 1:
                db_con.commit()
                return "삭제 성공"
            else:
                return "삭제 실패"

        except Exception as e:
            print(e)

        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)
from math import ceil
from company.company import Company
from moon_library.moon_DBManager import MoonDBManager


class CompanyDAO:
    
    def __init__(self):
        self.get_company_count_db()
        self.company_page = 3

    def add_company_db(self, cp):
        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")

            sql = "INSERT INTO apr07_company " \
            "VALUES('%s', '%s', '%s', %d)" % (cp.name, cp.addr, cp.ceo, cp.emp)

            db_cur.execute(sql)
            if db_cur.rowcount == 1:
                db_con.commit()
                self.company_cnt += 1
                return "등록 성공"
            else:
                return "등록 실패"
            
        except Exception as e:
             print(e)
             return "등록 실패"
        
        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)

    def get_all_company_db(self):

        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")
            sql = "SELECT * FROM apr07_company ORDER BY c_name"

            db_cur.execute(sql)

            list = []
            for name, addr, ceo, emp in db_cur:
                list.append(Company(name, addr, ceo, emp))

            return list

        except Exception as e:
            print(e)

        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)

    def get_company_db(self, c_page, keyword):

        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")
            sql =   "SELECT rn, c_name, c_addr, c_ceo, c_employee " \
                    "FROM (" \
                        "SELECT rownum AS rn, c_name, c_addr, c_ceo, c_employee " \
                        "FROM apr07_company " \
                        "WHERE c_name LIKE '%%%s%%' " \
                        "ORDER BY c_name" \
                    ") " \
                    "WHERE rn > %d AND rn <= %d" % (keyword, (c_page-1)*self.company_page, c_page*self.company_page)

            db_cur.execute(sql)

            list = []
            for _, name, addr, ceo, emp in db_cur:
                list.append(Company(name, addr, ceo, emp))

            return list

        except Exception as e:
            print(e)

        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)

    def get_company_count_db(self):
        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")
            sql = "SELECT count(*) FROM apr07_company"

            db_cur.execute(sql)

            count = 0
            for i in db_cur:
                count = i[0]

            self.company_cnt = count

        except Exception as e:
            print(e)

        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)

    def get_company_page_db(self, keyword):
        if keyword == "":
            company_cnt = self.company_cnt
        else:
            company_cnt = self.get_company_search_count_db(keyword)

        page = ceil(company_cnt / self.company_page)

        return page
    
    def get_company_search_count_db(self, keyword):
        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")
            sql =   "SELECT count(*) FROM apr07_company " \
                    "WHERE c_name LIKE '%%%s%%'" % (keyword)

            db_cur.execute(sql)

            count = 0
            for i in db_cur:
                count = i[0]

            return count

        except Exception as e:
            print(e)

        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)
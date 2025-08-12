from moon_library.moon_DBManager import MoonDBManager


class Account_DAO:

    def login_account(id, pw):
        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")

            sql =   "SELECT count(*) " \
                    "FROM apr09_account " \
                    "WHERE a_id = '%s' AND a_pw = '%s'" % (id, pw)

            db_cur.execute(sql)
            
            ac = None
            for i in db_cur:
                ac = i[0]

            if ac:
                return True
            else : 
                return False

        except Exception as e:
            print(e)
        
        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)

    def create_new_accont(ac):
        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")

            sql = "INSERT INTO apr09_account " \
            "VALUES('%s', '%s', '%s')" % (ac.id, ac.pw, ac.name)

            db_cur.execute(sql)
            if db_cur.rowcount == 1:
                db_con.commit()
                return "계정 등록 성공"
            else:
                return "계정 등록 실패"

        except Exception as e:
            return "계정 등록 실패"
        
        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)

    def check_create_account(ac):
        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")

            sql1 =   "SELECT count(*) " \
                    "FROM apr09_account " \
                    "WHERE a_name = '%s'" % (ac.name)
            
            sql2 =   "SELECT count(*) " \
                    "FROM apr09_account " \
                    "WHERE a_id = '%s'" % (ac.id)

            db_cur.execute(sql1)
            check = []
            for i in db_cur:
                check.append(i[0])

            db_cur.execute(sql2)
            for i in db_cur:
                check.append(i[0])

            if check[0] == 0 and check[1] == 0:
                return 1
            elif check[0] != 0 and check[1] == 0:
                return "계정 등록 실패, 중복된 닉네임입니다"
            elif check[0] == 0 and check[1] != 0:
                return "계정 등록 실패, 중복된 id입니다"
            else:    
                return "계정 등록 실패, 닉네임과 id 모두 중복되었습니다"
        
        except Exception as e:
            print(e)
        
        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)

    def delete_accont(id, pw):
        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")

            sql =   "DELETE FROM apr09_account " \
                    "WHERE a_id = '%s' AND a_pw = '%s'" % (id, pw)

            db_cur.execute(sql)
            if db_cur.rowcount == 1:
                db_con.commit()
                return "계정 삭제 성공"
            else:
                return "계정 삭제 실패"

        except Exception as e:
            return "계정 등록 실패"
        
        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)

    def check_delete_account(id, pw):
        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")

            sql =   "SELECT count(*) " \
                    "FROM apr09_account " \
                    "WHERE a_id = '%s' AND a_pw = '%s'" % (id, pw)

            db_cur.execute(sql)

            check = None
            for i in db_cur:
                check = i[0]

            if check == 1:
                return 1
            else:    
                return "해당 계정이 존재하지 않습니다"
        
        except Exception as e:
            print(e)
        
        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)
    
    def get_account_nickname(id, pw):
        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")

            sql =   "SELECT a_name " \
                    "FROM apr09_account " \
                    "WHERE a_id = '%s' AND a_pw = '%s'" % (id, pw)

            db_cur.execute(sql)

            name = None
            for i in db_cur:
                name = i[0]

            return name
        
        except Exception as e:
            print(e)
        
        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)
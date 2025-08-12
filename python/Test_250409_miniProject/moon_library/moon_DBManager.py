from oracledb import connect


class MoonDBManager:

    def db_connect(url):
        db_con = connect(url)
        db_cur = db_con.cursor()

        return db_con, db_cur
    
    def db_disconnect(db_con, db_cur):
        db_cur.close()
        db_con.close()
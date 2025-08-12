from oracledb import connect
from moon_library.moon_DBManager import MoonDBManager


class Doctor:

    def bmi_check(guest):

        db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")

        height = guest.height / 100
        guest.bmi = (guest.weight) / (height*height)

        if guest.bmi >= 39:
            guest.result = "고도 비만"
        elif guest.bmi >= 32:
            guest.result = "중도 비만"
        elif guest.bmi >= 30:
            guest.result = "경도 비만"
        elif guest.bmi >= 24:
            guest.result = "과체중"
        elif guest.bmi >= 10:
            guest.result = "정상"
        else:
            guest.result = "저체중"

        sql = "INSERT INTO apr07_bmi " \
        "VALUES('%s', %f, %f, %f, '%s')" % (guest.name, guest.height, guest.weight, guest.bmi, guest.result)

        db_cur.execute(sql)

        if db_cur.rowcount == 1:
            db_con.commit()

        MoonDBManager.db_disconnect(db_con, db_cur)
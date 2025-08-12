from datetime import datetime
from oracledb import connect


db_con = connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")
sql = "SELECT * FROM seoul_dust"

dust_csv = open("C:\\moon\\seoul_dust.csv", "a", encoding="utf-8")

cur = db_con.cursor()
cur.execute(sql)

for dust in cur:
    date = dust[0].strftime("%Y,%m,%d,%H,%M,%S")
    rgn = dust[1]
    ste = dust[2]
    pm25 = dust[3]
    pm10 = dust[4]
    sts = dust[5]

    dust_csv.write("%s,%s,%s,%s,%s,%s\n" % (date, rgn, ste, pm25, pm10, sts))

cur.close()
db_con.close()
dust_csv.close()

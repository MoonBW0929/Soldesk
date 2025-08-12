from oracledb import connect


conn = connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")

sql = "SELECT AVG(p_price) FROM apr03_prod"

cur = conn.cursor()
cur.execute(sql)

for a in cur:
    print(a)

cur.close()
conn.close()
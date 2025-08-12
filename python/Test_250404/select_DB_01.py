from oracledb import connect


conn = connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")

sql = "SELECT * FROM apr03_prod"

cur = conn.cursor()
cur.execute(sql)

for n, p in cur:
    print(n)
    print(p)
    print("-------")

cur.close()
conn.close()
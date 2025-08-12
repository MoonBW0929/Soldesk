from oracledb import connect

conn = connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")

p_name = input("상품 이름 : ")
p_price = input("상품 가격 : ")
sql = "UPDATE apr03_prod SET p_price = %s WHERE p_name = '%s'" % (p_price, p_name)

cur = conn.cursor()
cur.execute(sql)

if cur.rowcount == 1:
    print("업데이터 완료")
    conn.commit()
else:
    print("업데이터 실패")
    conn.rollback()

cur.close()
conn.close()
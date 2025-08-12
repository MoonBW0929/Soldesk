from oracledb import connect, init_oracle_client

conn = connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")

name = input("상품 이름 : ")
price = int(input("상품 가격 : "))

# sql = "INSERT INTO apr03_prod values('%s', %d)" % (name, price)
# sql = "DELETE FROM apr03_prod WHERE p_name = '%s' AND p_price = %d" % (name, price)
sql = "UPDATE apr03_prod SET p_price = %d WHERE p_name = '%s'" % (price, name)

# DB 관련 작업을 해주는 객체
cur = conn.cursor()

# sql문을 DB서버로 전송, 전송한 sql을 원격실행
cur.execute(sql)

# 전송 결과 확인
if cur.rowcount:
    print("sql 성공")

    # 결과 확인 후 DB에 반영
    conn.commit()
else:
    # 결과 확인 후 DB에 반영 안함
    conn.rollback()

# cursor 사용 끝
cur.close()
conn.close()

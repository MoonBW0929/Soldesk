from oracledb import connect, init_oracle_client

# instant client 불러오기
# 구버전 DB일 경우 init_oracle_client(lib_dir="instantclient폴더경로")

# DB 아이디/비밀번호@주소:포트/sid
conn = connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")

print(conn)

conn.close()

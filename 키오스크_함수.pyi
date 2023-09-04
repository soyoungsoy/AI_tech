import cx_Oracle
## 상품 조회 함수
# def KG_select():





conn=cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
sql = "select * from KIO_GOODS"
cur = conn.cursor()
cur.execute(sql)
for row in cur:
    print(list(row))
cur.close()
conn.close()






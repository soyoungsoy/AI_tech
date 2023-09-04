import cx_Oracle
# #
# # conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE") #우선 연결하고
# # sql = "select * from addr2" #해당 sql 정보를 불러와라
# # cur = conn.cursor() #cur은 conn(연결된 오라클)의 정보를 호출하는 것이다.
# # cur.execute(sql) #execute ~에 전송해라 / (sql)호출
# # for row in cur:
# #     print(list(row)) #리스트값으로 보여줘라 [a,b,c,...]
# # cur.close() #호출 닫고
# # conn.close()
#
#
#

while(True):
    print("==============================================================")
    print(" 1. 전체 메뉴 ", end="\t")
    print(" 2. 메뉴 선택 ", end="\t")
    print(" 3. 카트 조회 ", end="\t")
    print(" 4. 결제 완료 ")
    print("==============================================================")

    cmd = input("전체 메뉴를 보시겠습니까?:")
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = "select * from KIO_GOODS"
    cur = conn.cursor()
    cur.execute(sql)
    for row in cur:
        print(list(row))


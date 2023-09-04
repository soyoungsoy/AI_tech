# pip install cx-oracle(패키지 이름은 하이픈 오라클)
#
import cx_Oracle
#
# ----------------------------------------------------------------안 닫아도 되는 with 형식(복습 완)
# with cx_Oracle.connect("ai","0000","localhost:1521/XE") as conn :
#     if bool(conn): ##bool : T/F
#         print("연결성공")
#     else:
#         print("연결실패")
#
# with conn.cursor() as cur : #--커서(칸?) 정보를 불러와라
#     cur.execute("select * from emp")
#     for row in cur:
#         print(list(row))
#
#
# ----------------------------------------------------연결&닫기(복습 완)
# conn = cx_Oracle.connect("ai","0000","localhost:1521/XE")
# if bool(conn):
#     print("연결성공")
# else:
#     print("연결실패")

#
#
# ---------------------------------연결 된 오라클 값 호출하는 실행(복습 완)
#
conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE") #우선 연결하고
sql = "select * from addr2" #해당 sql 정보를 불러와라
cur = conn.cursor() #cur은 conn(연결된 오라클)의 정보를 호출하는 것이다.
cur.execute(sql) #execute ~에 전송해라 / (sql)호출
for row in cur:
    print(list(row)) #리스트값으로 보여줘라 [a,b,c,...]
cur.close() #호출 닫고
conn.close() #연결 닫아라

#
#
#
# ----------------------------------------------------insert
# insert : 1 row
# ----------------------------------------------------
# conn = cx_Oracle.connect("ai","0000","localhost:1521/XE")
# sql = "insert into addr(seq,name,tel) values(addr_seq.nextval,:1,:2)" #sql에 넣을 값의 키 위치를 지정해줘라 #숫자는 인덱스같은 것
# cur = conn.cursor()
# cur.execute(sql,['아무개','555'])
# cur.execute(sql,['함소영','2525'])
# conn.commit()
# cur.close()
# conn.close()
#
#
#
# conn = cx_Oracle.connect("ai","0000","localhost:1521/XE")
# sql = "insert into addr(seq,name,tel) values(addr_seq.nextval,:vnm,:vtel)"
# cur = conn.cursor()
# vnm = "나변수"
# vtel = "999"
# cur.execute(sql,[vnm,vtel])
# conn.commit()
# cur.close()
# conn.close()
#
#
# conn = cx_Oracle.connect("ai","0000","localhost:1521/XE")
# sql = "insert into addr(seq,name,tel) values(addr_seq.nextval,:vnm,:vtel)"
# cur = conn.cursor()
#
# cur.execute(sql,{"vnm":"나변수2","vtel":"8989"}) #키,값 형식으로 넣기. 변수 설정 안해도 된다.
# conn.commit()
# cur.close()
# conn.close()
#
#
#
# ---------------------------------------------------다량의 데이터를 넣는 방법
# insert : multi rows
# -----------------------------------------------------
#
# datas = [   {"vnm":"나이름1","vtel":"111"},
#             {"vnm":"나이름2","vtel":"222"},
#             {"vnm":"나이름3","vtel":"333"}    ]
#
# conn = cx_Oracle.connect("ai","0000","localhost:1521/XE")
# sql = "insert into addr(seq,name,tel) values(addr_seq.nextval,:vnm,:vtel)"
# cur = conn.cursor()
#
# cur.executemany(sql,datas) #executemany 많은 데이터 불러줘
# conn.commit()
# cur.close()
# conn.close()
#
#
#
# 값만 무작위로 있는 형식
#
# datas = [  ["리스트1","6666"] ,
#            ["리스트2","8888"] ,
#            ["리스트3","9999"] ]
#
# conn = cx_Oracle.connect("ai","0000","localhost:1521/XE")
# sql = "insert into addr(seq,name,tel) values(addr_seq.nextval,:1,:2)"# 키값은 임의로 설정
# cur = conn.cursor()
#
# cur.executemany(sql,datas)
# conn.commit()
# cur.close()
# conn.close()
#
#
#
#
#
# ------------------------------------------------------------
# update
# update addr set name ='홍길순',tel = '999' where seq=1
# ------------------------------------------------------------
#
# conn = cx_Oracle.connect("ai","0000","localhost:1521/XE")
# sql = "update addr set name =:1,tel =: 2 where seq=:3"# 사용자에게 받아올 키 값 설정
# cur = conn.cursor()
# cur.execute(sql,['홍길순','999',1])
# conn.commit()
# cur.close()
# conn.close()
#
#
#
# ------------------------------------------------------------
# delete
# update addr set name ='홍길순',tel = '999' where seq=1
# ------------------------------------------------------------
#
# conn = cx_Oracle.connect("ai","0000","localhost:1521/XE")
# sql = "delete addr where name like :1 or name like :2"# 사용자에게 받아올 키 값 설정
# cur = conn.cursor()
# cur.execute(sql,['%나이름%','%리스트%'])
# conn.commit()
# cur.close()
# conn.close()
#
#
# -------------------조건 있는 값 넣기..?
#
# conn = cx_Oracle.connect("ai","0000","localhost:1521/XE")
# sql = "select * from addr where seq =:1 "# 사용자에게 받아올 키 값 설정
# cur = conn.cursor()
# cur.execute(sql,[5])
# for row in cur:
#     print(list(row))
# conn.commit()
# cur.close()
# conn.close()
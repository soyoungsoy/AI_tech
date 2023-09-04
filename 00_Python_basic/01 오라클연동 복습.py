# import cx_Oracle


#--------------------오라클과 연동 성공 유무
# with cx_Oracle.connect("ai","0000","localhost:1521/XE") as conn :
#     if bool(conn): ##bool : T/F
#         print("연결성공")
#     else:
#         print("연결실패")

#
# with cx_Oracle.connect("ai","0000","localhost:1521/XE") as conn :
#     if bool(conn):
#         print("복습성공")
#     else:
#         print("복습실패")


#---------------------------------연결 된 오라클 값 불러와 실행하기
## 커서 : 여기라고 지목하는 것. 여기로 옮기라구~
# conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE") #우선 연결하고
# sql = "select * from addr2" #해당 sql 정보를 불러와라
# cur = conn.cursor() #cur은 conn(연결된 오라클)의 정보를 호출하는 것이다.
# cur.execute(sql) #execute 실행해라 / 커서로 지목한 (sql)호출을 실행해라
# for row in cur:
#     print(list(row)) #리스트값으로 보여줘라 [a,b,c,...]
# cur.close()
# conn.close()




#------------------------------------------------------------------insert 다양한 방식

# conn = cx_Oracle.connect("ai","0000","localhost:1521/XE")
# sql = "insert into addr2(seq,name,tel) values(addr2_seq.nextval,:1,:2)"
# #sql의 addr2 테이블로 seq,name,tel 컬럼에 values(값)을 seq(시퀀스)는 다음값으로, 1칼럼, 2칼럼은 값으로
# cur = conn.cursor()
# cur.execute(sql,['아무개','555'])넣어라(단수)
# cur.execute(sql,['함소영','2525'])
# conn.commit()
# cur.close()
# conn.close()

# conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
# sql = "insert into addr2(seq, name, tel) values(addr2_seq.nextval, :vnm, :vtel)"
# cur = conn.cursor()
# cur.execute(sql, {"vnm":"나변수2", "vtel":"8989"})
# conn.commit()
# cur.close()
# conn.close()
#
#

# datas = [  ["리스트1","6666"],
#            ["리스트2","8888"],
#            ["리스트3","9999"]
#         ]
# conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
# sql = "insert into addr(seq, name, tel) values(addr_seq.nextval, :1, :2)"
# cur = conn.cursor()
# cur.executemany(sql, datas) 떼거지로 넣어라
# conn.commit()
# cur.close()
# conn.close()



# datas = [  ["리스트1","6666"],
#            ["리스트2","8888"],
#            ["리스트3","9999"]
#         ]
# conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
# sql = "insert into addr2(seq,name,tel) values(addr2_seq.nextval,:a,:b)"
# cur = conn.cursor()
# cur.executemany(sql,datas)
# conn.commit()
# cur.close()
# conn.close()

# conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
# sql = "update addr2 set name=:1, tel=:2 where seq=:3"
# cur = conn.cursor()
# cur.execute(sql, ['홍길순', '999',3])
# conn.commit()
# cur.close()
# conn.close()
#
# conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
# sql = "select * from addr2 where seq = :1 or seq = :2"
# cur = conn.cursor()
# cur.execute(sql, [5, 1])
# for row in cur:
#     print( list(row)  )
# cur.close()
# conn.close()



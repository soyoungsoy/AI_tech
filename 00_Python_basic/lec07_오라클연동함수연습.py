# pip install cx-Oracle

import cx_Oracle

# with cx_Oracle.connect("ai", "0000", "localhost:1521/XE") as conn :
#     if bool(conn) :
#         print("연결성공")
#     else:
#         print("연결실패")
#     with conn.cursor() as cur:
#         cur.execute("select * from emp")
#         for row in cur:
#             print( list(row)  )
#         # cur.close()
# # conn.close()


#1메소드 1커넥션 해야한다.
#한 작업마다 열고 닫지 않으면, 다른 작업에 영향 받아서 안된다.
# 각자 열고 작업하고 각자 닫아야 안전


#--------------------------------------------------
# 연결 & 닫기
#--------------------------------------------------
# conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
# if bool(conn) :
#     print("연결성공")
# else:
#     print("연결실패")
# conn.close()


#--------------------------------------------------
# insert : 1 row
# insert into addr values(addr_seq.nextval, '홍길동', '000');
#--------------------------------------------------

def addr_insert(prm_name, prm_tel):#seq 함수 제외, name과 tel 파라미터만 입력
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = "insert into addr(seq, name, tel) values(addr_seq.nextval, :1, :2)"
    cur = conn.cursor()
    cur.execute(sql, [prm_name, prm_tel])
    conn.commit()
    cur.close()
    conn.close()


#--------------------------------------------------
# insert : multi rows
#--------------------------------------------------
# datas = [  {"vnm":"나이름1", "vtel":"111"} ,
#            {"vnm":"나이름2", "vtel":"222"} ,
#            {"vnm":"나이름3", "vtel":"333"}
#         ]
# conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
# sql = "insert into addr(seq, name, tel) values(addr_seq.nextval, :vnm, :vtel)"
# cur = conn.cursor()
# cur.executemany(sql, datas)
# conn.commit()
# cur.close()
# conn.close()




#--------------------------------------------------
# update
# update addr set name='홍길순', tel='999' where seq=1
#--------------------------------------------------

def addr_update(prm_name, prm_tel, prm_seq):#파라미터로 넣는 값 3개 필요
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = "update addr set name=:1, tel=:2 where seq=:3"
    cur = conn.cursor()
    cur.execute(sql, [prm_name, prm_tel, prm_seq])
    conn.commit()
    cur.close()
    conn.close()




#--------------------------------------------------
# delete
# delete from addr where seq = 1
#--------------------------------------------------

def addr_delete(prm_seq):#파라미터 필요
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = "delete from addr where seq = :1 "
    cur = conn.cursor()
    cur.execute(sql, [prm_seq])
    conn.commit()
    cur.close()
    conn.close()




# --------------------------------------------------
# select
# --------------------------------------------------
def addr_select():
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = "select * from addr"
    cur = conn.cursor()
    cur.execute(sql)
    for row in cur:
        print(list(row))
    cur.close()
    conn.close()



def menu_print():
    print("----------------------------------------------")
    print("1.입력(insert)",end="\t")
    print("2.전체(select)",end="\t")
    print("3.수정(update)",end="\t")
    print("4.삭제(delete)",end="\t")
    print("5.파일저장")
    print("6.종료")
    print("----------------------------------------------")


#
# conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
# while(True):
#     menu_print()
#     cmd = input("명령어 입력:")
#     if cmd == "5":
#         break#5번 종료
#
#     elif cmd == "1":
#         prm_name = input("이름:")
#         prm_tel = input("전화번호:")
#         addr_insert(prm_name, prm_tel)
#         isdel = True
#         if isdel == True:
#             print("입력되었습니다.")
#
#     elif cmd =="2":
#             print(addr_select())
#             print("조회되었습니다.")
#
#     # elif cmd =="3"
#     elif cmd == "4":
#         search_tel = input("수정할 전화번호:")
#         for addr_dic in addr_select():
#             if addr_dic[prm_tel] == search_tel:
#                 update_tel = input("변경할 전화번호:")
#                 addr_dic[prm_tel] = update_tel
#



#--------------------------------------------------
# insert : multi rows
#--------------------------------------------------
# datas = [  {"vnm":"나이름1", "vtel":"111"} ,
#            {"vnm":"나이름2", "vtel":"222"} ,
#            {"vnm":"나이름3", "vtel":"333"}
#         ]
# conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
# sql = "insert into addr(seq, name, tel) values(addr_seq.nextval, :vnm, :vtel)"
# cur = conn.cursor()
# cur.executemany(sql, datas)
# conn.commit()
# cur.close()
# conn.close()
while (True):
    menu_print()
    cmd = input("명령어입력:")
    if cmd == "1":
        print(1)
        name = input("입력할 이름은?:")
        tel = input("입력할 전화번호는?:")
        addr_insert(name,tel)
    elif cmd == "2":
        print(2)
        addr_select()
    elif cmd == "3":
        print(3)
        seq = input("수정할 대상은?:")
        name = input("수정할 이름은?:")
        tel = input("수정할 번호는?:")
        addr_update(name, tel, seq)
    elif cmd == "4":
        print(4)
        seq = input("삭제할 seq는?:")
        addr_delete(seq)
    elif cmd == "5":
        print(5)

    elif cmd == "6":
        break




# 다시
# d =open(file="C:/AI/pythonProject/venv/python_basic/lec06_주소록.txt",
#          mode='r',encoding="utf-8")
# txt_list = d.readlines()
# for i, txt in enumerate(txt_list):
#     txt = txt.strip()
#     if i ==0 :



# conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
# sql = "insert into addr(seq, name, tel) values(addr_seq.nextval, :vnm, :vtel)"
# cur = conn.cursor()
# cur.executemany(sql, datas)
# conn.commit()
# cur.close()
# conn.close()


#논리 이해하기
def file_db_insert(fname) :
    fr = open(file=fname, encoding='UTF-8', mode='r')
    txt_list = fr.readlines()

    data_list = []
    dict_key1 = ""
    dict_key2 = ""
    for i, txt in enumerate(txt_list):
        tlist = txt.strip().split("\t")
        if len(tlist) != 2:
            print("__\t__ 형식의 포맷이 아닙니다")
            break

        if i == 0:
            dict_key1 = tlist[0]
            dict_key2 = tlist[1]
        else:
            data_dict = {dict_key1: tlist[0], dict_key2: tlist[1]}
            data_list.append(data_dict)

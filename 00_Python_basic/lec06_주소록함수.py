# #리스트 값을 실행하려는 함수 위에 둬야 값을 출력한다.
addr_list =  [ {"name":"홍길동",  "tel":"010"},
               {"name":"홍길동",  "tel":"555"},
               {"name":"아무개",  "tel":"111"}]





#--------함수로 변환



#메뉴 보여줘 함수
def menu_print():
    print("----------------------------------------------")
    print("1.입력",end="\t")
    print("2.조회",end="\t")
    print("3.전체",end="\t")
    print("4.삭제",end="\t")
    print("5.수정",end="\t")
    print("6.종료")
    print("----------------------------------------------")

#파일 불러오는 함수(주소록에 있는 특정 자료값을 불러와서)
def addr_file_write():
    with open(file="./lec06_주소록.txt", mode="w", encoding="UTF-8") as fw:
        fw.write("name  tel\n")
        for addr_dic in addr_list:
            temp = addr_dic["name"]+"\t"+addr_dic["tel"]+"\n"
            fw.write(temp)

#입력 함수
def addr_input():
    name = input("이름:")
    tel = input("전화번호:")
    addr_list.append({"name": name, "tel": tel})

#총건 조회 함수
def addr_search_all():
    print("총",len(addr_list),"건")
    for addr_dic in addr_list:
        print(addr_dic["name"],"\t",addr_dic["tel"])

#검색 함수
def addr_search():
    search_name = input("검색이름:")
    search_list = [] #? 다시
    for addr_dic in addr_list:
        if addr_dic["name"] == search_name:
            search_list.append(addr_dic["tel"])
    if len(search_list) == 0:
        print("검색 결과가 없습니다")
    else:
        for search_tel in search_list:
            print(search_tel)

#삭제 함수
def addr_del():
    # isdel = False
    delete_tel = input("삭제할 전화번호:")
    for addr_dic in addr_list:
        if addr_dic["tel"] == delete_tel:
            yn = input("정말 삭제하시겠습니까?(Y/N)")
            if yn.upper() == "Y":
                addr_list.remove(addr_dic)

#수정 함수
def addr_update():
    isupdate = False
    search_tel = input("수정할 전화번호:")
    for addr_dic in addr_list:
        if addr_dic["tel"] == search_tel:
                update_tel = input("변경할 전화번호:")
                addr_dic["tel"] = update_tel
                isupdate = True
        if isupdate == True:
            print("수정되었습니다.")
        elif isupdate == False:
            print("검색 결과가 없습니다")

#전체 실행 함수
def run():
    while (True):
        menu_print()
        cmd = input("명령어입력:")
        if cmd == "6": #6.종료를 실행했을 때, 멈춰라
            break

        elif cmd == "1": # 명령어 1을 누르면
            addr_input() #입력한 name과 tel이 일치하면 추가해라.
            addr_file_write() #수정된 값을 업데이트한 자료가 있는 주소록.txt를 (없다면)생성하고 있으면 수정.
        elif cmd == "3": # 명령어 3을 누르면
            addr_search_all() # for문으로 모든 자료를(list) 조회해라.
            addr_file_write()
        elif cmd == "2": # 명령어 2를 누르면
            addr_search()
            addr_file_write()
        elif cmd == "4":
            addr_del()
            addr_file_write()
        elif cmd == "5":
            addr_update()
            addr_file_write()
    print(addr_list)







#다른데서 호출한거 아니고 내가 직접 돌렸을 때만 런(프로그램 n개 실행되지 않게)
if __name__ == "__main__" :
    print("직접돌려보기")
    run()

# from shutil import copy, copy2, copyfile
#
# infor = open("C:\\AI\\pythonProject\\venv\\python_basic\\lec06_회원정보.py",mode='w')
# lst = open("C:\\AI\\pythonProject\\venv\\python_basic\\lec06_주소록.py",mode='r')
# i = lst.readlines()
# for dd in i :
#     if dd =
#     copyfile(,infor)
#--------------내가 해본거


#주소록에 있는 특정 자료값을 불러온 txt를 만들어라
with open(file="./lec06_주소록.txt",mode='w',encoding="UTF-8") as fw:
    fw.write("name tel\n")
    for addr_dic in addr_list:
        temp = addr_dic["name"]+"\t"+addr_dic["tel"]+"\n"
        fw.write(temp)
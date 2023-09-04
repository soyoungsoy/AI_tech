
# 회원정보 리스트
addr_list =  [ {"name":"홍길동",  "tel":"010"},
               {"name":"홍길동",  "tel":"555"},
               {"name":"아무개",  "tel":"111"}]


#--------함수로 변환
def menu_print():
    print("----------------------------------------------")
    print("1.입력",end="\t")
    print("2.조회",end="\t")
    print("3.전체",end="\t")
    print("4.삭제",end="\t")
    print("5.수정",end="\t")
    print("6.종료")
    print("----------------------------------------------")

def addr_input():
    name = input("이름:")
    tel = input("전화번호:")
    addr_list.append({"name": name, "tel": tel})

def addr_search_all():
    print("총",len(addr_list),"건")
    for addr_dic in addr_list:
        print(addr_dic["name"],"\t",addr_dic["tel"])

def addr_search():
    search_name = input("검색이름:")
    search_list = []
    for addr_dic in addr_list:
        if addr_dic["name"] == search_name:
            search_list.append(addr_dic["tel"])
    if len(search_list) == 0:
        print("검색 결과가 없습니다")
    else:
        for search_tel in search_list:
            print(search_tel)

def addr_del():
    # isdel = False
    delete_tel = input("삭제할 전화번호:")
    for addr_dic in addr_list:
        if addr_dic["tel"] == delete_tel:
            yn = input("정말 삭제하시겠습니까?(Y/N)")
            if yn.upper() == "Y":
                addr_list.remove(addr_dic)

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




while(True):
    menu_print()
    cmd = input("명령어입력:")
    if cmd == "6" :
        break

    elif cmd == "1":
        addr_input()

    elif cmd == "3":
        addr_search_all()

    elif cmd == "2":
        addr_search()

    elif cmd == "4":
        addr_del()

    elif cmd == "5":
        addr_update()

print(addr_list)


#
# #삭제 기능 응용
# # -----------------------------------
# # delete_tel = input("삭제할 전화번호:")
# # for i, addr_dic in enumerate(addr_list):
# #        if addr_dic["tel"] == delete_tel:
# #            del addr_list[i]
# #              isdel=True
# #    if isdel == True:
# #        print("삭제되었습니다.")
# #    elif isdel == False:
# #        print("검색 결과가 없습니다.")
# # --------------------------
# # isdel = False
# # search_tel = input("삭제 전화번호:")
# # for i, addr_dic in enumerate(addr_list):
# #     if addr_dic["tel"] == search_tel:
# #         yn = input("정말 삭제하시겠습니까?(Y/N)")
# #         if yn.upper() == "Y":
# #             # del addr_list[i]
# #             addr_list.pop(i)
# #             isdel = True
# #
# # if isdel == True:
# #     print("삭제되었습니다")
# # elif isdel == False:
# #     print("검색 결과가 없습니다")
#
# # for addr_dict in addr_list:
# #     if addr_dict([0]["name"]) == addr_dict:
# #         print("name")
# #
# #         search_name = input("검색이름:")
# #         search_list = []
# #         for addr_dic in addr_list:
# #             if addr_dic["name"] == search_name:
# #                 search_list.append(addr_dic["tel"])
# #
# #         if len(search_list) == 0:
# #             print("검색 결과가 없습니다")
# #         else:
# #             for search_tel in search_list:
# #                 print(search_tel)
# #
#
#
#
#
# # addr_list = []
# # addr_list.append(1)
# # addr_list.append({"name":"아무개","tel":032})
# # addr_list.append({"name":"홍길동","tel":010})
# # addr_list.append({"name":"박","tel":258})
#
#

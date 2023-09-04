from python_basic.lec06_주소록함수 import run

run()

if __name__ == "__main__" :
    print("직접돌려보기")
    run()  # 불러온 함수가 아닌 직접 정의한 함수라면 "직접돌려보기"가 출력된다.
           # 이 모듈에선 import 해왔기 때문에 직접 정의한 것이 아님

# with open(file="./lec06_주소록.txt", mode="w", encoding="UTF-8") as fw:
#     fw.write("name  tel\n")
#     for addr_dic in addr_list:
#         temp = addr_dic["name"]+"\t"+addr_dic["tel"]+"\n"
#         fw.write(temp)


with open(file="./lec06_주소록.txt", mode="w", encoding="UTF-8") as fw:
    fw.write("name  tel\n")
    for addr_dic in addr_list:
        temp = addr_dic["name"]+"\t"+addr_dic["tel"]+"\n"
        fw.write(temp)
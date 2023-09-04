#-----------복습 완


#빅데이터 DB NoSql
# 마리아DB, 오라클, ms-sql, ... 일반 데이터용
# Hbase, 몽고?, DFS - 빅데이터용

#Hadoop - distribute 분산 파일 서버 써봤어요?? 아니요?? ㅎㅎ 넘 덩치가 커서 운영을 못해요..


#----------------------------------------------------------------
# 파일생성 -> 파일 읽기/쓰기 -> 파일/디렉토리 관리

#<<파일 생성>>-------------------------------
# open(파일경로, 모드)
# r : 읽기모드, w : 쓰기모드, a : 추가모드(기존 파일에 추가로 append, update 느낌)
# 리눅스, 유닉스 = /etc/guest/aa.txt ---슬래시로 경로표시
# 윈도우 = c:\aaa\bb.txt ---역슬래시로 경로표시
# 파이썬 프로그래밍에서 '\' 활용법 = C:\\aaa\\bb.txt(역슬래시 두 번), c:/aaa/bb.txt(그냥 슬래시)
# ㄴ이유 : \n, \t 등 파이선에서 역슬래시를 활용한 기능이 있기 때문에

#데이터를 읽어오는 통로 : 스트림 stream / 문 열어놓으면 계속 할 일 있는 줄 알고 에러

f = open(file="C:\\AI\\pythonProject\\venv\\python_basic\\memo_ansi.txt", mode='r') #f로 바인딩해라
f.close() #스트림 계속 열려있으면 안되니 닫아라

#--------------------------------------------------
#<<파일 읽기>>-------------------------------
# readline() : 라인 1줄
# readlines() : 라인 여러 줄
# read(),readlines() : 전체
# 리스트로 반환해준다
# ANSI ASCII (범용) -- 파이참은 안시를 잘 불러들인다 보이는덴 깨지지만
# CP949 UTF-8 (범용)
#-------------------------------------------------

# txt 파일 한 줄 불러오기
f=open(file="C:\\AI\\pythonProject\\venv\\python_basic\\memo_ansi.txt",mode='r')
t = f.readline()
print(t)
f.close()


# utf8 파일 인코딩해서 한 줄 불러오기
f = open(file="C:\\AI\\pythonProject\\venv\\python_basic\\memo_utf8.txt",
         mode='r', encoding="UTF-8") #--인코딩 안하면 2바이트 처리 못한다는 에러 발생
t = f.readline()
print(t)
f.close()







print("\n", "--"*40)

f=open(file="C:/AI/pythonProject/venv/python_basic/memo_utf8.txt",
       mode='r',encoding="utf-8") #--2바이트 처리 못한다는 에러 발생

#조건이 만족하면  = true(불리언어) = yes # 숫자1 = 숫자0(false)
print(True)
print(1) #=print(bool(1))
print(0)
#while(1):
    #print(1)

while(True): #조건이 만족하면 읽어라 /
             # while(True) or While(False) 구문은 O,X의 만족조건이므로, 디폴트값으로 참값일 때만 루프가 된다.
    t = f.readline()
    if not t:
        break #만약에 t가 없으면 빠져나와라
    print(t, end="")
f.close()


print("\n", "--"*40)

#쌤 정답
f = open(file="C:/AI/pythonProject/venv/python_basic/memo_utf8.txt"
         , mode='r'
         , encoding="UTF-8"
         )
# num = 5
# print(num < 10)  #True
while(True):
    txt = f.readline()
    if not txt:
        break
    print(txt, end="")
f.close()


print("\n", "--"*40)
#-------------------------------------------------
# 전체 값 가져와라

f=open(file="C:/AI/pythonProject/venv/python_basic/memo_utf8.txt",
       mode='r',encoding="utf-8")
txt_list = f.readlines()#전체값 가져오는 readlines
for txt in txt_list: #txt_list의 각 값들을 가져와라 : txt
    #txt = txt.strips() #공백&개행(줄바꿈) 제거
    print(txt, end="")


print("\n","--"*40)


#read-- 보여지는 그대로 읽어와라
f=open(file="C:/AI/pythonProject/venv/python_basic/memo_utf8.txt",mode='r',encoding="utf-8")
txt_list=f.readlines()
for txt in txt_list:
    #txt = txt.strips() #공백&개행(줄바꿈) 제거
    print(txt, end="")
txts = f.read() #위에 readlines 없이 read만 불러와도 가능. 그러나 전체 한꺼번에 불러오는게 너무 커서 비추
print(txts)
f.close() #보이는 방법 그대로 읽어라

print("\n", "--"*40)

# ---------------------------------------
# with open() as f : 자동으로 close()해준다
# ---------------------------------------
with open(file="C:/AI/pythonProject/venv/python_basic/memo_utf8.txt",
          mode='r',encoding="utf-8") as f :
    txts = f.read()
    print(txts)
    #들여쓰기(txt, print) 실행되면 close 안써도 된다.




    #------------------------------
    # 쓰기모드
    # with open(f="파일경로",mode='w'(default는 읽기)) as f :
    #------------------------------
with open(file="C:\\AI\\pythonProject\\venv\\python_basic\\memo_write.txt",mode='w') as f: #해당경로에 메모txt만들어서 열어줘
    f.write(str(1)+"\n")
    f.write("2")
print("======done=======")




#-------- 메모 txt에 1,10까지 출력해서 생성해라
with open(file="C:\\AI\\pythonProject\\venv\\python_basic\\memo_write.txt",mode='w') as f: #해당경로에 메모txt만들어서 열어줘
    for i in range(1,11):
        f.write(str(i)+"\n")#덮어쓰기

print("======done=======")




# -----------------------------------------
# 파일 복사(copy)
# memo_utf8.txt 파일을 memo_write.txt에 복사
# -----------------------------------------
fr = open(file="C:\\AI\\pythonProject\\venv\\python_basic\\memo_utf8.txt",  encoding='UTF-8', mode='r')
fw = open(file="C:\\AI\\pythonProject\\venv\\python_basic\\memo_write.txt", encoding='UTF-8', mode='a')
txt_list = fr.readlines()
for txt in txt_list:
    fw.write(txt) #그냥 쓰기모드는 값을 갱신한다면, a 모드는 쓰기+내용추가 기능이 같이 있다.
fr.close()
fw.close()



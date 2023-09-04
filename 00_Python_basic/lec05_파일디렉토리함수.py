# 남의 함수 꺼내서 쓰는 연습
# copy(원본파일경로, 타켓파일경로)
# copy ("/etc/memo/a.txt", "/etc/memo2/b.txt")
# copy2("/etc/memo/a.txt", "/etc/memo2")  --> /etc/memo2/a.txt

#--------------------------------------------------------------
from shutil import copy, copy2, copyfile  #파이썬이 기본으로 주는 것들
#--------------------------------------------------------------


# copy(원본파일경로, 타겟파일경로) -- 원본파일을 타겟파일로 복사해주세요
orig = "C:/AI/pythonProject/venv/python_basic/memo_utf8.txt"
dest = "C:\\AI\\pythonProject\\venv\\python_basic\\memo_write.txt"
copyfile(orig,dest)




#--------------------------------------
# 파일&디렉토리 내장 함수 *********누구나 다 쓰는 함수
#  절대경로(absolute path) : "C:\\AI\\pythonProject\\venv\\python_basic"
#  상대경로(relative path) : 상대적으로 내가 위치한 폴더를 기준으로 경로를 잡는 것
#     . : 현재폴더
#    .. : 상위폴더
#    /  : 안에 (ex : ./ = .(현재폴더), /(바로 안에))
#--------------------------------------
import os
from os.path import isfile, isdir, join

#v = 내장변수 , f = 내장함수, m = 내가 만든 함수
print(os.getcwd()) #함수 절대경로 찾기
print(os.listdir(os.getcwd()))
print("C:\\AI\\pythonProject\\venv\\python_basic")

pwd = os.getcwd() #바인딩 후 출력해도 된다.
print(os.listdir(pwd))

# from python_basic import lec04_파일입출력함수_lkh as lkh
# lkh.
#
# from python_basic.lec04_파일입출력함수_lkh import CalcClass

for f in os.listdir(pwd) :
    # print(os.getcwd()+ "\\" + f)
    print(join(os.getcwd(),f))

print(join("/aa","bb.txt"))

#-------------------------------------------

for f in os.listdir("C:\\") :
    # print(os.getcwd()+ "\\" + f)
    path = join("C:\\",f)
    if os.path.isdir(f) :
        print("[D]",f)
        if f == "AI" :
            print(join,os.listdir("C:\\AI"))
        else :
            print("[D]", f)
    elif os.path.isfile(f):
        print("\t",f) #내가 한거 망했다

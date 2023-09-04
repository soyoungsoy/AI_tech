
## 암기
# for 조건식 :
#     반복실행문
#
# while(조건식):
#     반복실행문


# 참고------------------------------------------------
#파이썬엔 없는 do ~ while ~
# do :
#     반복실행문
# while(조건식)

emp=[7788,7799,7800]

#for empno in emp: emp 안의 넘버 중 딱 한개만 꺼내서 보여주세요
#
# empno = emp[0]
# empno = emp[1]
# empno = emp[2]

for empno in emp:
    print(empno) #emp안의 empno 반복해서 꺼내서 보여줘 = 다 보여줘

dept=[1,2,3]
for a in dept:
    print(a) # for a in TEST
              #  print(a) -- TEST 안에 있는 값을 다 불러오는 출력 = a로 정의


#--------------------------------------
# range(시작번호 이상, 끝번호 미만, 증감분(기본값 1, 안써도 됨))
# ** 끝번호 미.만
#--------------------------------------

print(list(range(1,6)))#왜 안뜸
print(list(range(1,11,2)))
print(list(range(10,0,-1))) # 10 9 8 7 6 5 4 3 2 1 0

# for문 range 이용 1~10 출력

nums = [1,2,3,4,5]
for n in nums:
    print(n)
#-----------------------
for n in range(1,11):
    print(n,end="\n") #(n,end="  "):스페이스바 두번으로 공백 해도 된다., #\ :역슬래시는 줄바꿈, #(n,end="\t"):공백+Tab
# print(값, end = " "출력방식)

for n in range(100,600,100):
    print(n)#100부터 500까지 100단위로 루프
    for s in range(1,4):
        print(s,end="\t") # 1-3까지 줄바꾸고 탭 루프
    print() #줄바꿈 추가

#------------------------ 모든 프로그래밍 체계는 중첩할 때 구구단을 치라고 한다?
dan = 2
gob = 3
print (dan,"*3=6")
print (dan, "*", gob, "=6")
print (dan, "*", gob, "=", dan*gob)

#2단
#2*1=2 2*2=4 ... 2*9=18

#3단
#3*1=3 3*2=6 ... 9*9=81

#구구단 만들기


for dan in range(2,10):
        for n in range(2,10):
            for g in range(1,10):
                print(n, "  *  ", g, "  =  ", n*g)  #n이 한 번 루프할 때, g는 n조건 안에 있기 때문에 전체 루프한다.

#2,4,6,8단 * 5

for dan in range(2,9,2):
    print(dan,"단")
    for gob in range(1,6):
        print(dan,"  *  ",gob,"  =  ",dan*gob)


# 9,7,5,3 9-5까지 곱하기

for dan in range(9,2,-2):
    print(dan,"단")
    for gob in range(9,4,-1):
        print(dan,"  *  ",gob,"  =  ",dan*gob)

#   *
#  ***
# *****

# s = "*"
#
# for star in s:
#     print("  ",star,"  ",end="\n")
#         for sss in s:
#             print(" ",3*sss," ",end="\n")
#                 for sssss in s:
#                     print(5*sssss) --내가 해본거

#--------------------------------------------------
# (복습)
#   *
#  ***
# *****
print ("복습")

for s in range(3): #0.1.2
    print("  ",'*',end="\n")


print ("복습")
#--------------------------------------------------------------------

for g in range(2,-1,-1):
    print(" "*g,end="")
    print("X"*s)

for i in range(3):
    print(' ' * (2-i), end='')
    print((i * 2 + 1) * '*')


# ****
#  ***
#   **
#    *

for j in range(1,5):
    for k in range(1,5):
        #줄j,칸K if j=1, k=1 2 3 4
        if j <= k:
            print("*",end="")
        else:
            print(" ",end="")
    print()


#    *
#   **
#  ***
# ****

for j in range(1,5):
    for k in range(4,0,-1):
        #줄j,칸K if j=1, k=1 2 3 4
        if j < k:
            print(" ",end="")
        else:
            print("*",end="")
    print() #다시 해보기


for i in range(3): #0,1,2 -> 0부터 2까지 루프 , 3행(줄)
    print(' ' * (2-i),end="") #'공백'값을 2-0,2-1,2-2 로 루프해서 넣어라
    print('*'*(2*i+1)) # '*'값을 2i+1 값만큼 출력해라


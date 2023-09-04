## 암기
# for 조건식 :
#     반복실행문
#
# while(조건식):
#     반복실행문
#----------------------------------------------

# num =5
# while(num<10):
#     print("그렇다") #무한루프  -> 빨간 버튼 정지버튼 누르면 빠져나올 수 있음.

#*** while은 빠져나오는 조건을 잘 생각해야한다.




num =5
while(num<10):
    print("그렇다",num)
    num = num+1

#while 로 구구단

n=2
while(n<10):
    print(n,"단")
    g = 1
    while (g<10):
        print(n,"*", g,"=",n*g)
        g=g+1
    n=n+1
    print()

#------------------------------

print(type(5),5)
print(type("abc"),"abc")
print(type(17.4),17.4)
print(type([1,2,3]),[1,2,3])
print(type((1,2,3)),(1,2,3))
print(type({"empno":777}),{"empno":777})
print(type(True),True)

# True False : 불리언(bool)

#-------------캐스팅 = casting = 형변환 = 타입 변환
# print(3+"4")--> 오류
print(3+int("4")) # 바꾸고 싶은 형식으로 감싸주기

print(str(3)+"4")

print(4 + float(3)) # 소수점 붙이고 싶을 때 값 : 7.0

print(4+3.7)
#--------------slicing 슬라이싱
#[시작 이상: 끝 미만** : 1 정방, -1 거꾸로, -2 = 2개씩 건너뛰면서 거꾸로(증감+방향성)]

msg = "ABCDE"
print (msg[0:2]) # 0이상 2 미만 값 가져와 A,B
print (msg[3:5]) # 3이상 5 미만 값 가져와 , [3:2] 아님. [3번부터 5번 사이 값 가져와], [3:]만 적어도 된다. 다 가져와
print (msg[-2:])

emps = [7733, 7822, 7922, 8000]
print (emps[1:3])

license_plate = "24가 2210" #뒤에 4자리 출력해와라

print(license_plate[-4:]) #앞에서부터는 0부터 뒤는 그냥 -4

string = "홀짝홀짝홀짝" #홀만 출력
print (string[::2])

string = "PYTHON" #뒤집어 출력
print(string[-1::-1])

phone_number="010-1111-2222"

print(phone_number[:3])
print(phone_number[4:8])
print(phone_number[-4:]) #-4부터 끝까지

#strip 좌우공백제거 = trim (가운데는 제거 X)

data ="   삼성전자   "
data1 = data.strip() #data1은 data값을 좌우 공백제거한 값이다.
print(data1) #data1을 좌우 공백제거한 값을 출력해라

#split 주어진 구분자 단위로 문자열 자르기. 기본 구분자는 공백

a = "hello world"
print(a.split(), type(a.split()))

tel = "010-123-1234"
print(tel.split("-")) # 출력 후 리스트로 바뀜.
print(tel.split("-")[1]) # 리스트로 바뀐 값이기 때문에 [1] 형식으로 출력 가능 , 몇번째 값으로 꺼내 쓸 수 있게 변환


#remove, del
# del a[n] a리스트의 n값을 지워라
# a.remove("값") 값을 직접 지칭해서 지워라

lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
lang3 = lang1+lang2
print(lang3)
print(lang1)
lang1.extend(lang2) #lang1에 lang2 합치고
print(lang1) #lang1 을 출력해야 값이 나온다

#len : 리스트의 길이재는 것
print(len(lang1))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

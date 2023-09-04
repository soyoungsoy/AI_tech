#---------복습 완


#--------------------------------
#패키지    모듈     클래스   함수
# 폴더   .py파일   class   def
#-------------------------------

#이 파일 모듈 뭔가요? - lec04 파일입출력함수.py입니다.

class TestClass :
    def add(n1, n2): #함수 정의 해줘 함수이름(값,값)
        res = n1 + n2
        return res
a = TestClass.add(1,5) #add함수는 a이다
print(a)

#이렇게 만들어서 쓰는 이유? : 공통의 기능을 함수화시켜놓고 효율적으로 쓰기 위함이 목적.
# class 함수관리 위한 큰 틀 > 함수의 범위를 지정(회원관리의 add와 계산기의 add는 다르다)



def myprint(n):
    print(n,"입력했습니다.")

myprint(5)


def uprint(n):
    print(n,"입력~~~~~")
uprint(6)



class CalcClass :
    def add(n1, n2):
        res = n1 + n2
        return res

class MemberClass:
    def add(name, age):
        print(name,"저장")

def myprint(n):
    print(n,"입력되었습니다")

def uprint(n):
    print(n,"입력되었습니다2222")

    # #------------------------------------
    # # 함수를 불러서 사용한다 --> 함수 호출
    # # 함수에 return이 있는 경우 변수에 바인딩해 사용할 수 있다.
    # #------------------------------------
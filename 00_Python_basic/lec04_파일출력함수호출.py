# 함수 호출

#  결과를 준다 안준다의 구분 기준 : return
#  (함수로 새로운 값을 돌려주는 것 : 연산 등 / 내가 입력한 값을 받는 것 : return x)
# return 이 없으면 a= ... 이런거 받는거 아니다. 호출만 하고 끝남.



def myprint(n):
    print(n,"입력했습니다.")

myprint(5) #리턴 없음

# 함수에 return 있으면 바인딩해서 사용할 수 있다. a=calcul.add(1,5)
#---------------------------------------------------------
# from : 패키지명.모듈명
# import : 클래스명, 함수명, 모듈명
# 모듈명은 일반적으로 별칭(alias)를 사용한다
# import 함수명1, 함수명2이 길어지면 import 모듈명으로 한다
#   ex) from 패키지명.모듈명 import 클래스명
  # ex) from 패키지명.모듈명 import 함수명1, 함수명2 ...
  # ex) from 패키지명     import 모듈명 as 별명
#---------------------------------------------------------
#

#-------------------------------------------------
#import에 쓸 수 있는 것 : 클래스명, 함수명, 모듈명(.py)이 올 수 있다.
#--------------------------------------------------
from python_basic import lec04_파일입출력함수_lkh#클래스는 별명 안만든다, 문법상은 되는데.. 안됨!
from python_basic.lec04_파일입출력함수_lkh import CalcClass #함수 만든 경로 설정해주기
from python_basic.lec04_파일입출력함수_lkh import myprint
from python_basic import lec04_파일입출력함수_lkh as lec04 #전체 함수 불러와

from python_basic.lec04_파일입출력함수_lkh import CalcClass
from python_basic.lec04_파일입출력함수_lkh import myprint
from python_basic.lec04_파일입출력함수_lkh import MemberClass
from python_basic.lec04_파일입출력함수_lkh import uprint, myprint

lec04.uprint(55) #별명에서 유프린트 뽑아와
lec04.uprint


MemberClass.add("kim",30)
myprint(5)


a = CalcClass.add(1,5)
print(a)
print(CalcClass.add(1,5))


from python_basic.lec04_파일입출력함수_lkh import myprint,uprint
MemberClass.add("kim",30)
myprint(5)

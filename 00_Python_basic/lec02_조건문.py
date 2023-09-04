# if 조건식 : 조건1
#      실행1
# -------------------------- #if단독 가능(if는 무조건 써야된다)
# if 조건식 : 조건1
#      실행1
# else : 그 외 조건
#      실행2
# -------------------------- # if, else 가능

# if 조건식 : 조건1
#     실행1
# elif 조건식 : 조건2
#     실행2
# elif 조건식 : 조건3
#     실행3
#     (,,,elif 계속 가능)
# -------------------------- #if , elif .... 가능
# -------------------------- #if, elif ... else 가능

score = 80

#90이상이면 a 80이상이면 b 아니면c

if score >=90:
    print("a") #파이썬은 들여쓰기 잘 지켜야한다. 들여쓰기에 따라 범위 설정됨. : 하고 반드시 한 탭 들여써서 범위설정해줘야.
elif score>=80:
    print("b")
else:
    print("c")


# 90이상일 때, 성별이 남성1 여성이2
# 80이상일 때, 성별이 남성 11 여성 22
# 아니면 0

score = 80
gen ="남"


# 같다면 == , 같지않다면 !=
if score >=90:
    if gen=="남":
     print("1")
    else :
     print("2")
elif score >=80:
    if gen =="남":
     print("11")
    else:
     print("22")
else :
     print("0")



#이렇게 복합적으로도 쓸 수 있다.
if score>=90 and gen =="남":
    print("1")
elif score>=90 and gen =="여":
    print("2")
elif score>=80 and gen =="남":
    print("11")
elif score>=80 and gen =="여":
    print("22")
else:
    print("0")


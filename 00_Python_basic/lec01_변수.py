a=10
b=20
print(a+b)

# 파이썬은 값에 대한 타입을 외관적으로는 따지지 않는다.
# ex. abc, 023 -> 외관적인 타입은 크게 신경쓰지 않는다. 그러나 abc + 023 더하면 에러 -> 연산은 안돼 / abc+xyz = abcxyz 가능
# * 숫자의 연산은 계산, 글자의 연산은 합치는 기능
# * abc*3 = abcabcabc 반복의 의미의 곱하기


a= "abc"
b=3
print(a*b)


# 리스트 [] :다양한 타입을 한꺼번에 넣고 싶을 때 쓴다. 값의 접근 인덱스(index) 0번째
a=[1,2,3,4,5,"A"] #여러개를 모아놨다 : 컬렉션 [a,b,c,...]
print(a)
a.append(6) #추가해라
print(a)
print(a[4]) #a의 0번째부터 4번째 값 출력해라 : 5


#튜플 () : 리스트의 사촌. 리스트의 상수형(항상 변하지 않는 수) ex. 파이값, 중력 가속도값
# 한번 세팅하면 끝인 값이다. 값을 수정하지 못하게 하는, 오직 조회용으로만 보는(회원정보 등)

b =(1,2,3,4,5)
#b.append는 없다, 값을 수정하지 못하기 때문에
print(b)
print(b[2])

#딕셔너리 {키:값, 키:값, 키:값 ,...}
d = {"empno":7733,"ename":"SMITH"} #글자,숫자 상관없다.
print(d)
print(d["ename"]) #키를 넣으면 해당 값을 꺼낼 수 있다. ---select
d["job"]="SALES" #기존에 없던 값이라 추가된다. ---insert
d["ename"]="SSMITH" #기존에 있는 키를 입력하면 기존 값을 변경한다. ---update
print(d)



# 리스트 [] :다양한 타입을 한꺼번에 넣고 싶을 때 쓴다. 값의 접근 인덱스(index) 0번째부터 시작한다.
a=[1,2,3,4,"A"] #여러개를 모아놨다 : 컬렉션 [a,b,c,...]
a[4] = "Z" #인덱스로 접근해라. a의 4번째를 Z로 수정해라.
a.append(6) #추가해라 ---insert
a.insert(1,"BBB") #n번째에 무슨 값을 넣어주세요.
a.pop(0) #뒤의 0번째 지워주세요. delete
a.remove("Z") #"Z"를 지우세요.
print(a) #BBB,2,3,4,6

print(a[3]) #a의 0번째부터 3번째 값 출력해라 : 3 / [bbb]추가된 상태. select


mem = [1,2,3,["A","B"]] # 리스트 안에 리스트 넣기 가능
print(mem[3][1]) #3번째 중에서도 1번째 리스트 안의 리스트 전체가 n번째 인덱스 [n][n]
print(mem)

mem = [1,2,3,("A","B")] #리스트에 튜플 넣기 가능
print(mem[3][1])

mem = [1,2,3,{"empno":7733,"ename":"SMITH"}] #리스트에 딕셔너리 넣기 가능
print(mem[3]["empno"]) #키값을 꺼내고 싶으면 키를 입력한다. print(a[인덱스n]["키"])
print(mem[3])


ytb = {
 "kind": "youtube#videoListResponse",
 "etag": "\"UCBpFjp2h75_b92t44sqraUcyu0/sDAlsG9NGKfr6v5AlPZKSEZdtqA\"",
 "videos": [
  {
   "id": "7lCDEYXw3mM",
   "kind": "youtube#video",
   "etag": "\"UCBpFjp2h75_b92t44sqraUcyu0/iYynQR8AtacsFUwWmrVaw4Smb_Q\"",
   "snippet": {
    "publishedAt": "2012-06-20T22:45:24.000Z",
    "channelId": "UC_x5XG1OV2P6uZZ5FSM9Ttw",
    "title": "Google I/O 101: Q&A On Using Google APIs",
    "description": "Antonio Fuentes speaks to us and takes questions on working with Google APIs and OAuth 2.0.",
    "thumbnails": {
     "default": {
      "url": "https://i.ytimg.com/vi/7lCDEYXw3mM/default.jpg"
     },
     "medium": {
      "url": "https://i.ytimg.com/vi/7lCDEYXw3mM/mqdefault.jpg"
     },
     "high": {
      "url": "https://i.ytimg.com/vi/7lCDEYXw3mM/hqdefault.jpg"
     }
    },
    "categoryId": "28"
   },
   "contentDetails": {
    "duration": "PT15M51S",
    "aspectRatio": "RATIO_16_9"
   },
   "statistics": {
    "viewCount": "3057",
    "likeCount": "25",
    "dislikeCount": "0",
    "favoriteCount": "17",
    "commentCount": "12"
   },
   "status": {
    "uploadStatus": "STATUS_PROCESSED",
    "privacyStatus": "PRIVACY_PUBLIC"
   }
  }
 ]
}

print(ytb["videos"][0]["snippet"]["title"]) #딕셔너리{} -> 리스트[]이기 때문에 print(ytb["키"][리스트인덱스n]["키"])를 입력
print(ytb["videos"][0]["snippet"]["thumbnails"]["default"]["url"])
print(ytb["videos"][0]["statistics"]["viewCount"]) #대소문자 구분해서 입력해야한다.


naver = {
  "urls": [
    {
      "url": "http://www.your-site.com/article-1",
      "type": "update"
    },
    {
      "url": "http://www.your-site.com/article-2",
      "type": "update"
    },
    {
      "url": "http://www.your-site.com/article-3",
      "type": "delete"
    },
    {
      "url": "http://www.your-site.com/article-4",
      "type": "delete"
    }
  ]
}
print(naver["urls"][2]["url"])#주소를 뽑아야함으로 delete 의 url을 키로 쓴다.[{},{},{}]

print(ytb["videos"])
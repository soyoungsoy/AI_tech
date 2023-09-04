
#-------------------
# pip install Flask, requests(외부 통신을 위한  API)
#-------------------
import cx_Oracle
from flask import Flask, make_response, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')

def index():
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = "select * from kio_goods"
    cur = conn.cursor()
    cur.execute(sql)
    for good_list in cur:
        print(list(good_list))
    cur.close()
    conn.close()

    return render_template('index.html',GOODS_LIST = good_list)

@app.route('/list')
def test_list():
    test_list = [1,2,3]
    test_dict = {"uid":"kim","upw":"111"}
    test_list_dict = [ {"uid":"kim1","upw":"555"},
                       {"uid": "kim2", "upw": "666"}]

    return render_template('test.html',KEY_TEST_LIST = test_list,
                                       aaa = test_dict,
                                       bbb = test_list_dict )


if __name__ == '__main__':#내가 돌리는 메인 모듈이라면
    app.debug = True #개발자 모드, 개발 끝나면 꺼야 한다.
    app.run(host='localhost', port=80)#내 웹에 보여줘,  웹서비스 기본 포트 :80
    #app = flask : 원래는 파이썬에서 실행되지만 이제 앱인 플라스크에서 구동된다.



    #그럼 이제 내 lacalhost(웹)에서 hello world!가 출력된다

    #플라스크에서 디자인은 templates에 스크립트는 static에 지정(약속된 틀)
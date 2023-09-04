#------------------------------------------------
# pip install Flask,  requests
#------------------------------------------------

from flask import Flask, render_template, make_response, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    cur.execur3e("select * from kio_goods")
    goods_list_dict = [{"GOOD_NAME": "스파이시11", "GOOD_IMG":"static/images/menu/burger-11.jpg","GOOD_PRICE":5, "GOOD_DESC":"이건설명1"},
                      {"GOOD_NAME": "스파이시22", "GOOD_IMG": "static/images/menu/burger-11.jpg", "GOOD_PRICE": 25, "GOOD_DESC": "이건설명2"},
                      {"GOOD_NAME": "스파이시33", "GOOD_IMG": "static/images/menu/burger-11.jpg", "GOOD_PRICE": 15, "GOOD_DESC": "이건설명3"},
                      {"GOOD_NAME": "스파이시44", "GOOD_IMG": "static/images/menu/burger-11.jpg", "GOOD_PRICE": 4345, "GOOD_DESC": "이건설명4"},
                      ]

    return render_template('index.html', KEY_GOODS_LIST_DICT = goods_list_dict)



@app.route('/list')
def test_list():
    test_list = [good_]
    test_dict = {"uid":"kim", "upw":"111"}
    test_list_dict= [ {"uid": "kim1", "upw": "555"},
                      {"uid": "kim2", "upw": "666"} ]

    return render_template('test_LHK.html'
        , KEY_TEST_LIST = test_list
        , aaa = test_dict
        , KEY_TEST_LIST_DICT = test_list_dict
                           )



if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=80)
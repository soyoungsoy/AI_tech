from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from keras.preprocessing.text import Tokenizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Markup

total_seoul=pd.read_csv('./total_seoul.csv')

app = Flask(__name__)

@app.route("/")
def home() :
  return render_template('index.html')


from sqlalchemy import create_engine, text
import cx_Oracle


def 질문지출력(check, 성별, 나이):
    col_list = [ '앉아윗몸앞으로굽히기(cm)','10M_4회_왕복달리기(초)', '제자리멀리뛰기(cm)', '교차윗몸일으키기(회)']
    입력값_list = []
    for col in col_list:

        q30 = check['q30'][check['구분'] == col].values[0]
        q50 = check['q50'][check['구분'] == col].values[0]
        q70 = check['q70'][check['구분'] == col].values[0]
        a = f'{q30} 미만'
        b = f'{q30} 이상 {q50} 미만'
        c = f'{q50} 이상 {q70} 미만'
        d = f'{q70} 이상'

        입력값_list.append([a, b, c, d])

    col_list2 = ['상대악력(%)', '스텝검사출력(VO₂max)', '전신반응(초)','왕복오래달리기(회)']
    for col2 in col_list2:
        aa = '매우 그렇지 않다'
        bb = '그렇지 않다'
        cc = '그렇다'
        dd = '매우 그렇다'
        입력값_list.append([aa, bb, cc, dd])

    return 입력값_list


def sql_호출(성별, 나이):
    from sqlalchemy import create_engine, text
    import cx_Oracle
    engine = create_engine("oracle+cx_oracle://AI:0000@localhost:1521/XE")
    table_name = str(성별) + str(나이)
    check = pd.read_sql_query(text(f"select * from {table_name}"), con=engine.connect())
    engine.dispose()

    사용자입력값_list = 질문지출력(check, 성별, 나이)

    return 사용자입력값_list

# ------------------------------------------------------------------
# 워드 클라우드 관련 함수
# ------------------------------------------------------------------
from keras.preprocessing.text import Tokenizer
from wordcloud import WordCloud
def word_cloud_def(성별,나이,grade,col_gubun):
    temp=total_seoul[(total_seoul['성별구분코드']==성별)&(total_seoul['측정연령수']==나이)&(total_seoul['인증구분명']==grade)]
    gen_list=[]
    token = Tokenizer()
    token.fit_on_texts(temp[col_gubun])
    wc = WordCloud(font_path='malgun', background_color="white", max_font_size=60,colormap = 'Set3')
    gen = wc.generate_from_frequencies(token.word_docs)
    # plt.figure(figsize=(8, 6))
    plt.axis('off')
    plt.imshow(gen)
    plt.savefig(f'./static/Plotly-World_Cloud{col_gubun}.png')
    return ""


#------------------------------------------------------------
# rader chart
#------------------------------------------------------------
def rader_chart(성별, 나이):
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    import plotly.offline as pyo
    import pandas as pd

    col_list = ['신장(cm)', '체중(kg)', '체지방율(%)', '허리둘레(cm)',
                'BMI(kg/㎡)', '상대악력(%)', '교차윗몸일으키기(회)',
                '왕복오래달리기(회)', '스텝검사출력(VO₂max)', '앉아윗몸앞으로굽히기(cm)',
                '10M_4회_왕복달리기(초)', '제자리멀리뛰기(cm)']

    categories = ['신장', '체중', '체지방율', 'BMI']
    categories = [*categories, categories[0]]

    categories2 = ['상대악력', '교차윗몸일으키기',
                   '왕복오래달리기', '스텝검사출력', '앉아윗몸앞으로굽히기',
                   '10M_4회_왕복달리기', '제자리멀리뛰기']
    categories2 = [*categories2, categories2[0]]

    나이별_mu = total_seoul[col_list][(total_seoul['성별구분코드'] == 성별) & (total_seoul['측정연령수'] == 나이)].describe().iloc[
        1].values
    일등급_mu = total_seoul[col_list][(total_seoul['측정연령수'] == 나이) & (total_seoul['인증구분명'] == 1)].describe().iloc[
        1].values
    이등급_mu = total_seoul[col_list][(total_seoul['측정연령수'] == 나이) & (total_seoul['인증구분명'] == 2)].describe().iloc[
        1].values
    삼등급_mu = total_seoul[col_list][(total_seoul['측정연령수'] == 나이) & (total_seoul['인증구분명'] == 3)].describe().iloc[
        1].values
    # 나의_mu=total_seoul[col_list][total_seoul['성별구분코드']==sex].describe().iloc[1].values

    grade1 = [나이별_mu[0], 나이별_mu[1], 나이별_mu[2], 나이별_mu[4]]
    # grade2 = [heigt,weight,bmi,체지방률]
    grade3 = [일등급_mu[5], 일등급_mu[6], 일등급_mu[7], 일등급_mu[8], 일등급_mu[9], 일등급_mu[10], 일등급_mu[11]]
    grade4 = [이등급_mu[5], 이등급_mu[6], 이등급_mu[7], 이등급_mu[8], 이등급_mu[9], 이등급_mu[10], 이등급_mu[11]]
    grade5 = [삼등급_mu[5], 삼등급_mu[6], 삼등급_mu[7], 삼등급_mu[8], 삼등급_mu[9], 삼등급_mu[10], 삼등급_mu[11]]

    grade1 = [*grade1, grade1[0]]
    # grade2 = [*grade2, grade2[0]]
    grade3 = [*grade3, grade3[0]]
    grade4 = [*grade4, grade4[0]]
    grade5 = [*grade5, grade5[0]]

    fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'polar'}] * 2] * 1,
                        horizontal_spacing=0.3,
                        # vertical_spacing=0.1,
                        subplot_titles=("나와 같은 연령대의 사람들은?", "등급별 운동종목 평균은?"))

    fig.add_trace(
        go.Scatterpolar(r=grade1, theta=categories, fill='toself', name=f'{성별}세 {나이}성의 평균'),

        row=1,
        col=1,
    )
    fig.add_trace(
        go.Scatterpolar(r=grade3, theta=categories2, fill='toself', name='1등급평균'),
        row=1,
        col=2,
    )
    fig.add_trace(
        go.Scatterpolar(r=grade4, theta=categories2, fill='toself', name='2등급평균'),
        row=1,
        col=2,
    )
    fig.add_trace(
        go.Scatterpolar(r=grade5, theta=categories2, fill='toself', name='3등급평균'),
        row=1,
        col=2,
    )

    fig.update_layout(
        autosize=False,
        width=1000,
        height=700
    )
    fig.show()
    return fig


#--------------------------------------------------------------------
# flask
#--------------------------------------------------------------------

성별 = '남'
나이 = 20


@app.route("/questions", methods=['POST'])
def questions() :
  global 성별, 나이
  성별 = request.form['gen']
  나이 = request.form['age']
  print(성별,나이)
  answer_list = sql_호출(성별, 나이)
  print(answer_list)
  engine = create_engine("oracle+cx_oracle://AI:0000@localhost:1521/XE")
  check = pd.read_sql_query(text(f"select * from my_questions_table"), con=engine.connect())
  engine.dispose()

  print(check)

  my_question_list = [ ]
  for i, ques in enumerate(check['질문']):

      # print(성별,나이)

      my_question_dict = {}
      my_question_dict['number'] =  '0'+str(i+1)
      my_question_dict['question'] =  ques

      if i <5:
          my_question_dict['choices'] = [{'text': answer_list[i][0], 'value': '1'},
                                         {'text': answer_list[i][1], 'value': '2'},
                                         {'text': answer_list[i][2], 'value': '3'},
                                         {'text': answer_list[i][3], 'value': '4'}
                                         ]
      else:
          my_question_dict['choices'] = [{'text': answer_list[i][0], 'value': '1'},
                                         {'text': answer_list[i][1], 'value': '2'},
                                         {'text': answer_list[i][2], 'value': '3'},
                                         {'text': answer_list[i][3], 'value': '4'}
                                         ]
      my_question_list.append(my_question_dict)

  return render_template('questions.html', MY_QUESTION_LIST=my_question_list)


@app.route("/result", methods=['POST'])
def result():
    # print("-----", 성별, 나이)



    my_answer = request.form['my_answer']
    ans = my_answer[:-1].split(",")  #1,1,1,1,1,1,1,4,  끝에 ,버리기 [:-1]
    grade = 4
    if ((ans[0] == 4) & (ans[3] == 4) & (ans[4] == 4) & (ans[5] == 4) & (ans[6] == 4)) & (
          (ans[1] == 4) | (ans[2] == 4) | (ans[7] == 4)):
      grade = 1
    elif ((ans[0] == 3) & (ans[3] == 3) & (ans[4] == 3) & (ans[5] == 3) & (ans[6] == 3)) & (
          (ans[1] == 3) | (ans[2] == 3) | (ans[7] == 3)):
      grade = 2
    elif (ans[0] == 2) & (ans[3] == 2) & (ans[4] == 2) & (ans[5] == 2) & (ans[6] == 2):
      grade = 3

    # -------------------------------------------
    # 워드클라우드 생성 ---------------------- 불안정
    # ------------------------------------------
    # col_list = ['준비운동', '본운동', '마무리운동']
    # for col_gubun in col_list:
    #     word_cl = word_cloud_def(성별, 나이, grade, col_gubun)
    # ------------------------------------------
    # res_fig = rader_chart(성별, 나이)




    #-------------------------------------------
    # 차트 가져오기
    # ------------------------------------------
    my_exec_result = [
        f"체력심사 {grade}등급",
        "/static/my_rader_chart1.png",
        "/static/my_rader_chart2.png",
        "./static/Plotly-World_Cloud준비운동.png",
        "./static/Plotly-World_Cloud본운동.png",
        "./static/Plotly-World_Cloud마무리운동.png"
    # "/static/images/my_recomm_result1.png",
    # "/static/images/my_recomm_result1.png",
    # "/static/images/my_recomm_result1.png"
    ]
    return render_template('results.html', MY_EXEC_RESULT=my_exec_result)






if __name__=='__main__':
  app.run('0.0.0.0',port=5000,debug=True)
  

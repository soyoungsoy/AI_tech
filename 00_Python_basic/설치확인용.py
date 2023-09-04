# # from konlpy.tag import Komoran
# # komoran = Komoran()
# # print(komoran.nouns("게시글이 apple 좋았다면 Dr Hong 쿄쿄쿄 공감을 눌러주세요!!"))
#
# from konlpy.tag import Okt
# okt = Okt()
# print(okt.pos('아버지가 방에 들어가신다'))
# print(okt.pos('아버지가방에들어가신다'))


from konlpy.tag import Mecab
mecab = Mecab(dicpath=r"C:\mecab\mecab-ko-dic")
print(mecab.pos('아버지가방에들어가신다'))
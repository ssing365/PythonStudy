# -*- coding: utf-8 -*-
from konlpy.tag import Okt

test = ("동해물과 백두산이 마르고 닳도록 "
        "하느님이 보우하사 우리나라 만세 Korea :)")

#Okt객체 선언
okt = Okt()

#morphs : 형태소 단위로 구문 분석을 수행
print(okt.morphs(test))
print()

#nouns : 명사만 추출
print(okt.nouns(test))
print()

#phrases : 어절만 추출
result1 = okt.phrases(test)
print(result1)
print()

'''
pos : 형태소 단위로 쪼갠 후 각 품사들을 태깅해서 리스트 형태로 반환
영어단어는 Alpha 특수기호는 Puntuation 한글은 KoreanParticle등
'''
result2 = okt.pos(test)
print(result2)
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

'''
박스플롯
 : 범주형 데이터의 분포를 파악할 때 적합한 그래프
 최소, 최대, 1분위값, 중간값, 2분위값 등의 정보를 제공한다.
'''
font_path = '../resData/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

#스타일로 사용할 수 있는 항목 확인
print(plt.style.available)
plt.style.use('seaborn-v0_8-poster')
plt.rcParams['axes.unicode_minus']=False

df=pd.read_csv('../resData/auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

#그림 크기 설정
fig = plt.figure(figsize=(15,5))
#2개의 Axe 객체 생성(1행 2열)
ax1 = fig.add_subplot(1,2,1)
ax2= fig.add_subplot(122)   

ax1.boxplot(x=[df[df['origin']==1]['mpg'],
               df[df['origin']==2]['mpg'],
               df[df['origin']==3]['mpg']],
            labels=['USA','EU','JAPAN'])

ax2.boxplot(x=[df[df['origin']==1]['mpg'],
               df[df['origin']==2]['mpg'],
               df[df['origin']==3]['mpg']],
            labels=['USA','EU','JAPAN'],
            vert=False)

ax1.set_title('제조국가별 연비 분포(수직 박스 플롯)')
ax2.set_title('제조국가별 연비 분포(수평 박스 플롯)')

'''
그래프 상단 혹은 우측에 o로 표시되는 값이 있는데,
보통 관측되는 데이터의 범위에서 많이 벗어난 값으로 '이상치'라고 표현한다.
'''
plt.show()
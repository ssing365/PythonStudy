# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

#한글깨짐처리 start
from matplotlib import font_manager, rc
font_path = "../resData/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
#한글깨짐처리 end

df = pd.read_excel('../resData/시도별_전출입_인구수.xlsx', engine = 'openpyxl', header=0)
df = df.fillna(method = 'ffill')
print(df.head())

#서울에서 경기로 전출할 데이터만 추출
mask = (df['전출지별']=='서울특별시') & (df['전입지별']!= '서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'],axis=1)   
df_seoul.rename({'전입지별': '전입지'},axis=1, inplace=True)   
df_seoul.set_index('전입지', inplace=True)
print(df_seoul)
sr_one = df_seoul.loc['경기도']
print(sr_one)

plt.style.use('ggplot')
plt.figure(figsize=(14,5))
plt.xticks(rotation = 'vertical')
##마커와 마크사이즈 지정
plt.plot(sr_one.index, sr_one.values, marker='o', markersize=10)

plt.title('서울 -> 경기 인구 이동')
plt.xlabel('기간')
plt.ylabel('이동 인구수')
plt.legend(labels=['서울 -> 경기'], loc='best')

plt.ylim(50000, 800000)

'''
위치를 나타내는 x,y좌표에서 x는 인덱스 번호를 사용한다.
y는 인구수를 나타내는 숫자이므로 그대로 사용할 수 있다.
즉 (2, 290000) 이라면 1972년의 29만의 좌표가 된다.
'''
#첫 번째 화살표
plt.annotate('',#텍스트표시(화살표라 생략)
             xytext=(2, 290000), #화살표의 꼬리부분(시작점)
             xy=(20, 620000), #화살표의 머리부분(끝점)
             xycoords='data', #좌표체계(데이터를 사용함)
             arrowprops=dict(arrowstyle='-|>', color='skyblue', lw=2),
             #화살표의 스타일 지정. 모양, 컬러, 두께를 딕셔너리로 지정
             )
#두 번째 화살표
plt.annotate('',
             xytext=(30, 580000),
             xy=(47, 450000),
             xycoords='data',
             arrowprops=dict(arrowstyle='-|>', color='olive', lw=5),)
#텍스트 주석
plt.annotate('인구 이동 증가(1970-1995)', #출력할 텍스트
             xy=(10, 450000), #텍스트 위치
             rotation=25, #회전각도
             va='baseline', #글자 세로(수직) 방향 정렬. 속성값은 center, top, bottom, baseline등
             ha='center', #글자 좌우(수평)방향 정렬. 속성값은 center, left, right등
             fontsize=15
             )
plt.annotate('인구 이동 감소(1995-2017)',
             xy=(40, 560000),
             rotation=-10,
             va='baseline',
             ha='center',
             fontsize=15
             )
plt.show()

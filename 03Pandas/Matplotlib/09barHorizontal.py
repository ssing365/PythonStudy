# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

#폰트 설정
font_path = "../resData/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

#서울 -> 경기 데이터를 Excel로부터 추출
df = pd.read_excel('../resData/시도별_전출입_인구수.xlsx', engine = 'openpyxl', header=0)
df = df.fillna(method = 'ffill')
mask = (df['전출지별']=='서울특별시') & (df['전입지별']!= '서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'],axis=1)   
df_seoul.rename({'전입지별': '전입지'},axis=1, inplace=True)   
df_seoul.set_index('전입지', inplace=True)

col_years = list(map(str, range(2010, 2018)))
df4 = df_seoul.loc[['충청남도', '경상북도', '강원도', '전라남도'], col_years]

df4['합계']=df4.sum(axis=1)
df_total = df4[['합계']].sort_values(by='합계', ascending=True)
plt.style.use('ggplot')
df4.plot(kind='barh', figsize=(10,5), width=0.5, color='cornflowerblue')

plt.title("서울 -> 다른지역 인구 이동", size=30)
plt.ylabel('전입지', size=20)
plt.xlabel('이동 인구 수',size=20)

plt.show()
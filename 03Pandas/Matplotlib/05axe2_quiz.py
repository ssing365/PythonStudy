# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

#폰트 설정
font_path = "../resData/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

#강원 -> 서울 데이터를 Excel로부터 추출
df = pd.read_excel('../resData/시도별_전출입_인구수.xlsx', engine = 'openpyxl', header=0)
df = df.fillna(method = 'ffill')
mask = (df['전출지별']=='강원도') & (df['전입지별']!= '강원도')
df_gangwon = df[mask]
df_gangwon = df_gangwon.drop(['전출지별'],axis=1)   
df_gangwon.rename({'전입지별': '전입지'},axis=1, inplace=True)   
df_gangwon.set_index('전입지', inplace=True)

sr_one = df_gangwon.loc['서울특별시']

plt.style.use('ggplot')

fig = plt.figure(figsize=(20,5)) 
ax1 = fig.add_subplot(2,1,1) 

ax1.plot(sr_one, marker='o', markerfacecolor='green', color = 'olive', linewidth=2, label='강원->서울')
ax1.legend(loc='best')
ax1.set_ylim(0, 100000)
ax1.set_title("강원 -> 서울 인구 이동", size=20)    
ax1.set_xlabel('기간', size=12)
ax1.set_ylabel('이동 인구수', size=12)
ax1.set_xticklabels(sr_one.index, rotation=75)  

ax1.tick_params(axis='x', labelsize=10)
ax1.tick_params(axis='y', labelsize=10)

plt.show()
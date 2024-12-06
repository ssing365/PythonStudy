# -*- coding: utf-8 -*-
import pandas as pd
import folium
import json

'''
Choropleth Map(코로프레스 맵)
 : 행정구역과 같이 지도상에 경계를 표시해준다.
'''

file_path = '../resData/경기도_인구_데이터.xlsx'    
df = pd.read_excel(file_path, index_col = '구분', engine='openpyxl')    
# 컬럼을 문자형으로 변환
df.columns = df.columns.map(str)

geo_path = '../resData/경기도_행정구역_경계.json'   
try:
    geo_data = json.load(open(geo_path, encoding='utf-8'))
except:
    geo_data = json.load(open(geo_path, encoding='utf-8-sig'))

# 폴리엄을 통해 지도 생성
g_map = folium.Map(location=[37.5502, 126.982],
                   tiles='OpenToPoMap', zoom_start=9)   

'''
geo_data : 지도 데이터 혹은 파일 경로
data ; 시각화하기위한 데이터파일 (여기서는 데이터프레임)
columns : 지도 데이터와 매핑할 값. 시각화할 변수를 지정
key_on :데이터파일과 매핑할 값
'''
year='2017'

folium.Choropleth(geo_data=geo_data,
                  data=df[year],
                  columns=[df.index, df[year]],
                  fill_color='PuBuGn', fill_opacity=0.7, line_opacity=1,
                  key_on='feature.properties.name',
                  legend_name='경기도인구데이터',
                  ).add_to(g_map)

g_map.save('../saveFiles/gyonggi_population_' + year + '.html')

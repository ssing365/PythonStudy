# -*- coding: utf-8 -*-
import folium

seoul_map1 = folium.Map(location=[37.55, 126.98], zoom_start=12)
seoul_map1.save('../saveFiles/seoul1.html')

seoul_map2 = folium.Map(location=[37.55, 126.98], zoom_start=12, tiles='OpenTopoMap')
seoul_map2.save('../saveFiles/seoul2.html')

seoul_map3 = folium.Map(location=[37.55, 126.98], zoom_start=15, tiles='Cartodb dark_matter')
seoul_map3.save('../saveFiles/seoul3.html')

import pandas as pd
df = pd.read_excel('../resData/서울지역_대학교_위치.xlsx', engine='openpyxl')
df.columns = ['학교명', '위도', '경도']
for name, lat, lng in zip(df.학교명, df.위도, df.경도):
    folium.Marker([lat,lng], popup=name).add_to(seoul_map2)
seoul_map2.save('../saveFiles/seoul_colleges1.html')

for name, lat, lng in zip(df.학교명, df.위도, df.경도):
    folium.CircleMarker([lat, lng], radius=10, color='brown', fill=True,
                        fill_color='coral', fill_opacity=0.7, popup=name).add_to(seoul_map3)
seoul_map3.save('../saveFiles/seoul_colleges2.html')
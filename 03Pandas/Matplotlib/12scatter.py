# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')

df = pd.read_csv('../resData/auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

# 히스토그램 생성. bins 옵션으로 10개의 구간으로 나눈다.
# bins가 커지면 세분화된다(그래프의 폭이 좁아진다).
df.plot(kind='scatter', x='weight', y='mpg', c='blue', s=10, figsize=(10,5))

plt.title('Scatter Plot - mpg vs weight')
plt.show()
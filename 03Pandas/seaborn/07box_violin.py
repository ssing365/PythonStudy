# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')
sns.set_style('whitegrid')

fig = plt.figure(figsize=(15, 10))
axe1 = fig.add_subplot(221)
axe2 = fig.add_subplot(222)
axe3 = fig.add_subplot(223)
axe4 = fig.add_subplot(224)

'''
boxplot()
 : 범주형 데이터 분포와 주요 통계 지표를 함께 제공하는 그래프
 단, 데이터가 퍼져있는 분산의 정도를 정확히 알기 어려운 단점이 있다.

violinplot()
 : 데이터가 퍼져있는 분산의 정도를 알기 위해 사용하는 그래프
'''
#박스플롯(기본값)
sns.boxplot(x='alive', y='age', data=titanic, ax=axe1)
sns.boxplot(x='alive', y='age', hue='sex', data=titanic, ax=axe2) #hue 옵션으로 남녀 구분
#바이올린플롯(기본값)
sns.violinplot(x='alive', y='age', data=titanic, ax=axe3)
sns.violinplot(x='alive', y='age', hue='sex', data=titanic, ax=axe4) #hue 옵션으로 남녀 구분

plt.show()

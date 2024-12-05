import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')
sns.set_style('darkgrid')

fig = plt.figure(figsize=(15,5))
axe1 = fig.add_subplot(121)
axe2 = fig.add_subplot(122)

'''
regplot() : 회귀선이 있는 산점도를 표현
    서로 다른 2개의 연속 변수 사이의 산점도를 그리고
    선형 회귀 분석을 위한 회귀선을 출력한다.
    회귀의 목적은 데이터에서 패턴을 학습해 새로운 데이터에 대한 예측을 수행하는 것이다.
'''

'''
x축은 나이, y축은 운임요금에 대한 관계를 그래프로 표현한다.
fit_reg 옵션은 회귀선을 표시하기 위한 것으로 True가 디폴트값이다.
'''
sns.regplot(x='age', y='fare', data=titanic, ax=axe1)
sns.regplot(x='age', y='fare', data=titanic, ax=axe2, fit_reg=False)

plt.show()
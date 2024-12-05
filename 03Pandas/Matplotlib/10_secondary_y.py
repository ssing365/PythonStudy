import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

#폰트 설정
font_path = "../resData/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

plt.style.use('ggplot')
'''
그래프에 음수기호를 유니코드가 아닌 ASCII로 출력되도록 설정.
이 설정이 없으면 0를 제대로 인식하지못해 깨짐
'''
plt.rcParams['axes.unicode_minu']=False

'''
엑셀파일을 데이터프레임으로 변환. 
header옵션이 없으므로 첫 행은타이틀로 지정된다.
'''
df = pd.read_excel('../resData/남북한_발전_전력량.xlsx', engine='openpyxl')
#5~8행까지 북한의 합계~원자력 행을 선택하여 변수에 저장
df = df.loc[5:9]
#'전력량' 컬럼을 삭제한 후 원본 데이터프레임에 적용한다.
df.drop("전력량 (억㎾h)", axis='columns', inplace=True)
df.set_index('발전 전력별', inplace=True)
df = df.T

df = df.rename(columns={'합계' : '총발전량'})
df['총발전량 - 1년'] = df['총발전량'].shift(1)
df['증감률'] = ((df['총발전량']/df['총발전량 - 1년']) -1) * 100 

axe1 = df[['수력', '화력']].plot(kind='bar', figsize=(20,10), width=0.7, stacked=True)
axe2 = axe1.twinx()
axe2.plot(df.index, df.증감률, ls='--', marker='o', markersize=20,
          color='red', label='전년대비 증감률(%)')
axe1.set_ylim(0,500)
axe2.set_ylim(-50,50)   

axe1.set_xlabel('연도', size=20)
axe1.set_ylabel('발전량(억 ㎾h)')
axe2.set_ylabel('전년 대비 증감률(%)')

plt.title('북한 전력 발전량 (1990~2016)', size=30)
axe1.legend(loc='upper left')

plt.show()

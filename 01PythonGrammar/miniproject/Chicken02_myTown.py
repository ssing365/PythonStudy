import squarify
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from sympy.abc import alpha
from collections import Counter

#데이터 확인
df = pd.read_csv('../resData/치킨집가공.csv')
df.info()
print(df.head())

dong_list=[]
for addr in df['소재지전체주소']:

    dong_list.append(addr.split(' ')[2])

    # 등장 횟수 계산
    dong_counts = Counter(dong_list)

    # 중복되지 않는 동 이름 리스트
    unique_dongs = list(dong_counts.keys())

    # 등장 횟수 리스트
    counts = list(dong_counts.values())

#트리맵 생성
data = {'customers' : counts,
        'cluster' : unique_dongs}
df2 = pd.DataFrame(data)

plt.style.use('ggplot')
font_name = (font_manager.FontProperties(fname="../resData/malgun.ttf")
             .get_name())
rc('font', family=font_name)

df2['label'] = df2['cluster'] + "\n(" +df2['customers'].astype(str) + ")"
plt.figure(figsize=(30, 16))
squarify.plot(sizes=df2['customers'],label=df2['label'],alpha=.8 )
plt.axis('off')
plt.show()
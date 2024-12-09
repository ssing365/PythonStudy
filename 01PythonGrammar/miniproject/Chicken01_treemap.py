import squarify
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from sympy.abc import alpha

data = {'customers' : [8,3,4,2],
        'cluster' : ['영역A', '영역B', '영역C', '영역D']}
df = pd.DataFrame(data)

plt.style.use('ggplot')
font_name = (font_manager.FontProperties(fname="../resData/malgun.ttf")
             .get_name())
rc('font', family=font_name)

df['label'] = df['cluster'] + "\n(" +df['customers'].astype(str) + ")"
squarify.plot(sizes=df['customers'],label=df['label'],alpha=.8 )
plt.axis('off')
plt.show()
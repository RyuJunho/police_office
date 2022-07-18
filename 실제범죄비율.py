import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


# 한글깨짐 방지
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

df = pd.read_csv('./부산시2.csv', encoding = 'CP949')

행정구역 = df['행정구역'].values.tolist()
신고수 = df['신고수'].values.tolist()
폭력 = df['폭력'].values.tolist()
절도 = df['절도'].values.tolist()
성범죄 = df['성범죄'].values.tolist()
강도 = df['강도'].values.tolist()
살인 = df['살인'].values.tolist()
합계 = np.array(폭력) + np.array(절도) + np.array(성범죄) + np.array(강도) + np.array(살인)

fig = plt.figure(figsize = (15,15))     # size
xtick_label_position = list(range(len(행정구역)))

# first chart1 : ax1
ax1 = fig.add_subplot()
ax1.set_xticks(xtick_label_position)
ax1.set_xticklabels(행정구역)
ax1.set_xlabel('행정구역', fontsize = 20)

# stack bar
ax1.bar(xtick_label_position,폭력,color = 'lightcoral',label = '폭력')
ax1.bar(xtick_label_position,절도,bottom = np.array(폭력),color = 'moccasin',label = '절도')
ax1.bar(xtick_label_position,성범죄,bottom = np.array(폭력) + np.array(절도),color = 'greenyellow',label = '성범죄')
ax1.bar(xtick_label_position,강도,bottom = np.array(폭력) + np.array(절도) + np.array(성범죄),color = 'cornflowerblue',label = '강도')
ax1.bar(xtick_label_position,살인,bottom = np.array(폭력) + np.array(절도) + np.array(성범죄) + np.array(강도),color = 'mediumorchid',label = '살인')

# second chart : ax2
ax2 = ax1.twinx()
ax2.plot(xtick_label_position,신고수,linestyle='--',marker='o',label = '신고수',color = 'black')  # plot

plt.title('지역별 신고 건수와 실제 발생한 범죄', fontsize = 20)    # title
# legend
ax1.legend(loc = 'upper left')
ax2.legend(loc = 'upper right')
plt.ylim(0,120000)
plt.show()
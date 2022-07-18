import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# 한글깨짐 방지
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)


df = pd.read_csv('./부산시2.csv', encoding = 'CP949')

행정구역 = df['행정구역'].values.tolist()

신고수 = df['신고수'].values.tolist()

경찰서수 = df['지역경찰서'].values.tolist()

fig = plt.figure(figsize = (15,15))
ax1 = fig.add_subplot()

xtick_label_position = list(range(len(행정구역)))
ax1.set_xticks(xtick_label_position)
ax1.set_xticklabels(행정구역)
ax1.set_xlabel('행정구역', fontsize = 20)
ax1.bar(xtick_label_position,신고수,color = 'yellow',label = '신고수')

ax2 = ax1.twinx()
ax2.plot(xtick_label_position,경찰서수,linestyle='--',marker='o',label = '경찰서수')

plt.title('지역별 신고 건수와 경찰서 수', fontsize = 20)
ax1.legend(loc = 'upper left')
ax2.legend(loc = 'upper right')
plt.ylim(0,12)
plt.show()
from matplotlib import pyplot as plt
import pandas as pd
import os
import datetime
import pytz

# グラフ生成プログラム
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter 


from matplotlib.font_manager import FontProperties
font_path = "/usr/share/fonts/truetype/migmix/migmix-1p-regular.ttf"
font_prop = FontProperties(fname=font_path)
plt.rcParams["font.family"] = font_prop.get_name()

class FixedOrderFormatter(ScalarFormatter):
    def __init__(self, order_of_mag=0, useOffset=True, useMathText=True):
        self._order_of_mag = order_of_mag
        ScalarFormatter.__init__(self, useOffset=useOffset, 
                                 useMathText=useMathText)
    def _set_orderOfMagnitude(self, range):
        self.orderOfMagnitude = self._order_of_mag

today = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
tstr = today.strftime('%Y年%m月%d日 %H時%M分')
file = today.strftime('%Y-%m-%d-%H-%M-%S')
title = ('NiziU-Chopstick 再生回数')


# 再生履歴のcsvを読み込む
input_csv = pd.read_csv('./Data/chopstick-view-v2.csv')
first_column_data = input_csv[input_csv.keys()[1]]
second_column_data = input_csv[input_csv.keys()[0]]

plt.xlabel(input_csv.keys()[1])
plt.ylabel(input_csv.keys()[0])


ax = plt.plot(first_column_data, second_column_data, linestyle='solid', marker='o')
plt.title(title + tstr + '時点')

ax.yaxis.set_major_formatter(FixedOrderFormatter(4 ,useMathText=True))
#ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.ticklabel_format(style="sci",  axis="y",scilimits=(0,0))

plt.savefig('./Data/' + file + ".png")
plt.close()

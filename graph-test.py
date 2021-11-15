from matplotlib import pyplot as plt
import pandas as pd
import os
import datetime
import pytz

# グラフ生成プログラム
import pandas as pd
import matplotlib.pyplot as plt

today = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
tstr = today.strftime('%Y年%m月%d日 %H時%M分')
file = today.strftime('%Y-%m-%d-%H-%M-%S')
title = ('NiziU-Chopstick 再生回数')


# 再生履歴のcsvを読み込む
input_csv = pd.read_csv('./Data/chopstick-view-v2.csv')
first_column_data = input_csv[input_csv.keys()[2]]
second_column_data = input_csv[input_csv.keys()[1]]

plt.xlabel(input_csv.keys()[2])
plt.ylabel(input_csv.keys()[1])

plt.plot(first_column_data, second_column_data, linestyle='solid', marker='o')
plt.title(title + tstr + '時点')

plt.savefig(./Data/file+".png")
plt.close()

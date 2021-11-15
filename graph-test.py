import os
import settings
from twitter import Twitter, OAuth
import pathlib
import pytz
# import pandas as pd

# df = pd.read_csv('chopstick-view.csv')
# df.tail(1)
# グラフ生成プログラム
import pandas as pd
import matplotlib.pyplot as plt

# 再生履歴のcsvを読み込む
input_csv = pd.read_csv('./Data/chopstick-view-v2.csv')
first_column_data = input_csv[input_csv.keys()[2]]
second_column_data = input_csv[input_csv.keys()[1]]

plt.xlabel(input_csv.keys()[2])
plt.ylabel(input_csv.keys()[1])

plt.plot(first_column_data, second_column_data, linestyle='solid', marker='o')
plt.show()

import json
from requests_oauthlib import OAuth1Session
import settings

from matplotlib import pyplot as plt
import pandas as pd
import os
import datetime
import pytz

# グラフ生成プログラム
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates


# 日本語設定
from matplotlib.font_manager import FontProperties
font_path = "/usr/share/fonts/truetype/migmix/migmix-1p-regular.ttf"
font_prop = FontProperties(fname=font_path)
plt.rcParams["font.family"] = font_prop.get_name()

# タイトル設定
today = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
tstr = today.strftime('%Y年%m月%d日 %H時%M分')
file = today.strftime('%Y-%m-%d-%H-%M-%S')
title = ('NiziU-Chopstick 再生回数')

# 再生履歴のcsvを読み込む
input_csv = pd.read_csv('./Data/chopstick-view-v2.csv')
first_column_data = input_csv[input_csv.keys()[1]]
second_column_data = input_csv[input_csv.keys()[0]]

# 軸指定
plt.xlabel(input_csv.keys()[1])
plt.ylabel(input_csv.keys()[0])

plt.ticklabel_format(style = 'plain')


# plt.gcf().autofmt_xdate() 

# plt.gca().xaxis.set_major_formatter(mdates.DayLocator(bymonthday=None, interval=2, tz=None))

# グラフ出力時にx軸が重なるのを防止する
plt.gca().xaxis.set_major_formatter(mdates.DayLocator)

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%m/%d")) 

plt.xticks(rotation=40)

# プロット
ax = plt.plot(first_column_data, second_column_data, linestyle='solid', antialiased='True')
# タイトル書き込み
plt.title(title + tstr + '時点')

plt.savefig('./Data/' + file + ".png")
plt.close()

CK = settings.TW_CONSUMER_KEY
CS = settings.TW_CONSUMER_SECRET
AT = settings.TW_TOKEN
AS = settings.TW_TOKEN_SECRET

url_media = "https://upload.twitter.com/1.1/media/upload.json"
url_text = "https://api.twitter.com/1.1/statuses/update.json"

# OAuth認証 セッションを開始
twitter = OAuth1Session(CK, CS, AT, AS)

# 画像投稿
files = {"media" : open('./Data/' + file + '.png', 'rb')}
req_media = twitter.post(url_media, files = files)

# レスポンスを確認
if req_media.status_code != 200:
    print ("画像アップデート失敗: %s", req_media.text)
    exit()

# Media ID を取得
media_id = json.loads(req_media.text)['media_id']
print ("Media ID: %d" % media_id)

# Media ID を付加してテキストを投稿
params = {'status': 'tweet with image.\n\nTesting now.', "media_ids": [media_id]}
req_media = twitter.post(url_text, params = params)

# 再びレスポンスを確認
if req_media.status_code != 200:
    print ("テキストアップデート失敗: %s", req_text.text)
    exit()

print ("OK")

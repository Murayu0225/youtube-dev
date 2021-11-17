import os
import json
from requests_oauthlib import OAuth1Session
import pandas as pd
import settings
 
CONSUMER_KEY = settings.TW_CONSUMER_KEY
CONSUMER_SECRET = settings.TW_CONSUMER_SECRET
ACCESS_KEY = settings.TW_TOKEN
ACCESS_KEY_SECRET = settings.TW_TOKEN_SECRET

twitter = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_KEY_SECRET)
 
list_text = []
list_favorite_count = []
list_retweet_count = []

url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
 
# APIアクセスチェック
if url.status_code == 200:
  print('APIステータスチェックに成功しました。')
else:
  print('[ERR01]APIステータスチェックにて問題が発生しました。')
  print('プログラムを終了します。')
  sys.exit(1)

params = {
    'count':1,
    'screen_name':'NiziU__official'
}
 
res = twitter.get(url, params=params)
 
timelines = json.loads(res.text)
 
for data in timelines:
    list_text.append(data['text'])
    list_favorite_count.append(data['favorite_count'])
    list_retweet_count.append(data['retweet_count'])
df = pd.DataFrame({'text': list_text,
                   'fav_count': list_favorite_count,
                   'RT_count': list_retweet_count
                  })
videos_report.to_csv("./Data/niziu-tweet.csv", index=None, mode='a', header=False)

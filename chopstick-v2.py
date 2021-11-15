import pandas as pd
from apiclient.discovery import build
from apiclient.errors import HttpError
import settings
import datetime
import pytz

today = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
tstr = today.strftime('%Y/%m/%d %H:%M:%S')

# settings.pyからAPIキーを受け取る
API_KEY = settings.YT_API
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
# リスト形式でChopstickのvideo idを追加
searches = ['nCjmXHsRJNY']
# 情報を下記リストに挿入
videos = []

youtube = build(
    YOUTUBE_API_SERVICE_NAME, 
    YOUTUBE_API_VERSION,
    developerKey=API_KEY
    )

# リストに複数あった場合、ループ処理するようになっている。
for result in searches:
    video_response = youtube.videos().list(
      part = 'snippet,statistics',
      id = result
      ).execute()
    # YouTube APIリクエスト
    for video_result in video_response.get("items", []):
        if video_result["kind"] == "youtube#video":
            videos.append([video_result["snippet"]["title"],video_result["statistics"]["viewCount"],video_result["statistics"]["likeCount"],video_result["statistics"]["dislikeCount"],video_result["statistics"]["commentCount"],video_result["snippet"]["publishedAt"]])

videos_report = pd.DataFrame(videos, columns=['title', 'viewCount', 'likeCount', 'dislikeCount', 'commentCount', 'publishedAt'], index=[tstr])
videos_report['Date'] = tstr
videos_report.set_index('Date')
videos_report.to_csv("./Data/chopstick-v2.csv", mode='a', header=False)

import pandas as pd
from apiclient.discovery import build
from apiclient.errors import HttpError
import settings
import datetime
import pytz

today = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
tstr = today.strftime('%Y/%m/%d %H:%M:%S')

API_KEY = settings.YT_API
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
searches = ['v9H-bT_76x0']
videos = []

youtube = build(
    YOUTUBE_API_SERVICE_NAME, 
    YOUTUBE_API_VERSION,
    developerKey=API_KEY
    )

for result in searches:
    video_response = youtube.videos().list(
      part = 'snippet,statistics',
      id = result
      ).execute()

    for video_result in video_response.get("items", []):
        if video_result["kind"] == "youtube#video":
            videos.append([video_result["statistics"]["viewCount"]])

videos_report = pd.DataFrame(videos, columns=['viewCount'])
videos_report['Date'] = tstr
videos_report.to_csv("./Data/need-u-view-data.csv", index=None, mode='a', header=False)

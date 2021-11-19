import pandas as pd
from apiclient.discovery import build
from apiclient.errors import HttpError
import settings

API_KEY = settings.YT_API
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
# CHANNEL_ID = 'UCHp2q2i85qt_9nn2H7AvGOw'
# channels = [] #チャンネル情報を格納する配列
searches = ['nCjmXHsRJNY'] #videoidを格納する配列
videos = [] #各動画情報を格納する配列
# nextPagetoken = None
# nextpagetoken = None

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
videos_report.to_csv("./Data/need-view.csv", index=None, mode='a', header=False)

# channel_report = pd.DataFrame(channels, columns=['title', 'subscriberCount', 'videoCount', 'publishedAt'])
# channel_report.to_csv("channels_report.csv", index=None, mode='a', header=False)

import pandas as pd
from apiclient.discovery import build
from apiclient.errors import HttpError
import settings
from twitter import Twitter, OAuth

userdicdf = pd.read_csv('./Data/id.csv', sep=',', encoding='utf-8', index_col=False, header=None)
id_list = list(userdicdf[0])

API_KEY = settings.YT_API
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
CHANNEL_ID = 'UCHp2q2i85qt_9nn2H7AvGOw'
channels = []
searches = []
videos = []
nextPagetoken = None
nextpagetoken = None

youtube = build(
    YOUTUBE_API_SERVICE_NAME, 
    YOUTUBE_API_VERSION,
    developerKey=API_KEY
    )

channel_response = youtube.channels().list(
    part = 'snippet,statistics',
    id = CHANNEL_ID
    ).execute()
  
for channel_result in channel_response.get("items", []):
    if channel_result["kind"] == "youtube#channel":
        channels.append([channel_result["snippet"]["title"],channel_result["statistics"]["subscriberCount"],channel_result["statistics"]["videoCount"],channel_result["snippet"]["publishedAt"]])

while True:
    if nextPagetoken != None:
        nextpagetoken = nextPagetoken

    search_response = youtube.search().list(
      part = "snippet",
      channelId = CHANNEL_ID,
      maxResults = 50,
      order = "date",
      pageToken = nextpagetoken
      ).execute()  

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            searches.append(search_result["id"]["videoId"])
    try:
        nextPagetoken =  search_response["nextPageToken"]
    except:
        break

print(searches)

for result in searches:
    video_response = youtube.videos().list(
      part = 'snippet,statistics',
      id = result
      ).execute()

    for video_result in video_response.get("items", []):
        if video_result["kind"] == "youtube#video":
            videos.append([video_result["snippet"]["title"],video_result["statistics"]["viewCount"],video_result["statistics"]["likeCount"],video_result["statistics"]["commentCount"],video_result["snippet"]["publishedAt"]])  

searches_report = pd.DataFrame(searches)
searches_report.to_csv("./Data/id.csv", index=None)

check = set(id_list) ^ set(searches)
check = list(check)
print(check)

if not check:
  print('Not found.')
else:
  print('Start Tweet.')
  for id in check:
    t = Twitter(
      auth=OAuth(
          settings.TW_TOKEN,
          settings.TW_TOKEN_SECRET,
          settings.TW_CONSUMER_KEY,
          settings.TW_CONSUMER_SECRET,
      )
    )
    msg = "[TEST MODE] NiziU OfficialさんがYouTubeに新規投稿をしました！\n#NiziU\n\nhttps://www.youtube.com/watch?v=" + id
    t.statuses.update(status=msg)

videos_report = pd.DataFrame(videos, columns=['title', 'viewCount', 'likeCount', 'commentCount', 'publishedAt'])
videos_report.to_csv("./Data/videos_report.csv", index=None)

channel_report = pd.DataFrame(channels, columns=['title', 'subscriberCount', 'videoCount', 'publishedAt'])
channel_report.to_csv("./Data/channels_report.csv", index=None)

import pandas as pd
from apiclient.discovery import build
from apiclient.errors import HttpError
import settings
from requests_oauthlib import OAuth1Session

userdicdf = pd.read_csv('./Data/id.csv', sep=',', encoding='utf-8', index_col=False, header=None)
list(userdicdf[0])
print(userdicdf)

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

check = set(userdicdf) ^ set(searches.T)
check = list(check)
print(check)

CK = settings.TW_CONSUMER_KEY
CS = settings.TW_CONSUMER_SECRET
AT = settings.TW_TOKEN
AS = settings.TW_TOKEN_SECRET

url_text = "https://api.twitter.com/1.1/statuses/update.json"

twitter = OAuth1Session(CK, CS, AT, AS)

if not check:
  print('Not found.')
else:
  print('新規投稿あり')
  for id in check:
    print(check[id])
    params = {'status': "[TEST MODE] NiziU OfficialさんがYouTubeに新規投稿をしました！\n#NiziU\n\nhttps://www.youtube.com/watch?v="}
    req_media = twitter.post(url_text, params = params)

videos_report = pd.DataFrame(videos, columns=['title', 'viewCount', 'likeCount', 'commentCount', 'publishedAt'])
videos_report.to_csv("./Data/videos_report.csv", index=None)

channel_report = pd.DataFrame(channels, columns=['title', 'subscriberCount', 'videoCount', 'publishedAt'])
channel_report.to_csv("./Data/channels_report.csv", index=None)

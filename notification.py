import pandas as pd
from apiclient.discovery import build
from apiclient.errors import HttpError
from twitter import Twitter, OAuth
import settings
import sys

try:
  print('NiziU YouTube Notification System. Created by Murayu0225.')
except Exception as e:
  print("Can't start program.")
  print(e)
  sys.exit(1)

try:
  userdicdf = pd.read_csv('./Data/id.csv', sep=',', encoding='utf-8', index_col=False, header=None)
  id_list = list(userdicdf[0])
except Exception as e:
  print('\033[31m' + "Error occurred! Can't read csv file." +'\033[0m')
  print(e)
  sys.exit(1)

API_KEY = settings.YT_API
YOUTUBE_API_SERVICE_NAME = settings.YT_NAME
YOUTUBE_API_VERSION = settings.YT_VERSION
CHANNEL_ID = settings.YT_ID
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
  
print('Start request data.')
try:
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
  print('All data download successfully')
except Exception as e:
  print('\033[31m' + "Error occurred! Can't request data." +'\033[0m')
  print(e)
  sys.exit(1)

print('Checking new post.')
check = set(id_list) ^ set(searches)
check = list(check)
i = 0
if not check:
  print('Not found.')
else:
  print('Found!')
  print('Start Tweet...')
  i += 1
  for id in check:   
    t = Twitter(auth = OAuth(settings.TW_TOKEN, settings.TW_TOKEN_SECRET, settings.TW_CONSUMER_KEY, settings.TW_CONSUMER_SECRET))
    msg = settings.TW_MESSAGE + id
    try:
      statusUpdate = t.statuses.update(status=msg)
      print('\033[32m' + 'Tweeted!' + '\033[0m')
      print(statusUpdate)
    except Exception as e:
      print('\033[31m' + 'Error occurred! The tweet was not successful.' +'\033[0m')
      print(e)

print('Start saving data.')
try:
  if i == 1:
    for id in check:
      searches_report = pd.DataFrame(id)
      searches_report.to_csv("./Data/id.csv", mode='a', index=None, header=None)
  
  videos_report = pd.DataFrame(videos, columns=['title', 'viewCount', 'likeCount', 'commentCount', 'publishedAt'])
  videos_report.to_csv("./Data/videos_report.csv", index=None)

  channel_report = pd.DataFrame(channels, columns=['title', 'subscriberCount', 'videoCount', 'publishedAt'])
  channel_report.to_csv("./Data/channels_report.csv", index=None)
  print('The data was successfully saved.')
  print('Bye!')
  sys.exit(0)
except Exception as e:
  print('The data was not successfully saved.')
  print(e)
  print('Please fix error.')
  print('Bye.')
  sys.exit(1)

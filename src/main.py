import time
import json
import requests
import settings
import csv
import schedule

YT_API_KEY = settings.YT_API
FILE = '6.txt'
# どうしてもActionの動作を見たいので機密事項ですがprintします。すぐにAPIを破棄します。
# print(YT_API_KEY)

# 出典元：https://qiita.com/harukikaneko/items/b004048f8d1eca44cba9 (ありがとうございます。)
def get_chat_id(yt_url):
    '''
    https://developers.google.com/youtube/v3/docs/videos/list?hl=ja
    '''
    video_id = yt_url.replace('https://www.youtube.com/watch?v=', '')
    print('video_id : ', video_id)

    url    = 'https://www.googleapis.com/youtube/v3/videos'
    params = {'key': YT_API_KEY, 'id': video_id, 'part': 'liveStreamingDetails'}
    data   = requests.get(url, params=params).json()

    liveStreamingDetails = data['items'][0]['liveStreamingDetails']
    if 'activeLiveChatId' in liveStreamingDetails.keys():
        chat_id = liveStreamingDetails['activeLiveChatId']
        print('get_chat_id done!')
        print(chat_id)
    else:
        chat_id = None
        print('NOT live')

    return chat_id

def get_chat(chat_id, pageToken, log_file):
    '''
    https://developers.google.com/youtube/v3/live/docs/liveChatMessages/list
    '''
    url    = 'https://www.googleapis.com/youtube/v3/liveChat/messages'
    params = {'key': YT_API_KEY, 'liveChatId': chat_id, 'part': 'id,snippet,authorDetails'}
    if type(pageToken) == str:
        params['pageToken'] = pageToken

    data   = requests.get(url, params=params).json()
    print(data)

    try:
        for item in data['items']:
            channelId = item['snippet']['authorChannelId']
            msg       = item['snippet']['displayMessage']
            usr       = item['authorDetails']['displayName']
            #supChat   = item['snippet']['superChatDetails']
            #supStic   = item['snippet']['superStickerDetails']
            log_text  = '[by {}  https://www.youtube.com/channel/{}]\n  {}'.format(usr, channelId, msg)
            with open(FILE, 'a') as f:
                print(log_text, file=f)
                print(log_text)
        print('start : ', data['items'][0]['snippet']['publishedAt'])
        print('end   : ', data['items'][-1]['snippet']['publishedAt'])

    except:
        pass

    return data['nextPageToken']

def main(yt_url):
    slp_time        = 10 #sec
    iter_times      = 90 #回
    take_time       = slp_time / 60 * iter_times
    print('{}分後　終了予定'.format(take_time))
    print('work on {}'.format(yt_url))

    log_file = yt_url.replace('https://www.youtube.com/watch?v=', '') + '.txt'
    with open(log_file, 'a') as f:
        print('{} のチャット欄を記録します。'.format(yt_url), file=f)
    chat_id  = get_chat_id(yt_url)

    nextPageToken = None
    for ii in range(iter_times):
        #for jj in [0]:
        try:
            print('\n')
            nextPageToken = get_chat(chat_id, nextPageToken, log_file)
            time.sleep(slp_time)
        except:
            break

# if __name__ == '__main__':
    # 人気な方のライブ配信URLを勝手に貼らさせてもらいました。
    # yt_url = https://www.youtube.com/watch?v=Jr5uuXWB96U
    # main(yt_url)

if __name__ == '__main__':
  yt_url = 'https://www.youtube.com/watch?v=BRXHVEWb4Rk'
  main(yt_url)

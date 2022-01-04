## YouTube Dev

src以下にソースコードは入ってませんが、下記を参照してください。

```
.
├── CODE_OF_CONDUCT.md
├── Data
│   ├── channels_report.csv
│   ├── chopstick-v2.csv
│   ├── chopstick-view-v2.csv
│   ├── chopstick-view.csv
│   ├── chopstick.csv
│   ├── id.csv
│   ├── need-u-view-data.csv
│   ├── need-view.csv
│   ├── need.csv
│   ├── niziu-tweet.csv
│   └── videos_report.csv
├── LICENSE
├── README.md
├── requirements.txt
└── src
    ├── chopstick-v2.py (Chopstick の全データと日付を記録)
    ├── chopstick-view-v2.py (Chopstick の再生回数と日付を記録(ツイートグラフ生成用))
    ├── chopstick-view.py (Chopstick の再生回数を記録(ツイート数値取得用))
    ├── chopstick.py (Chopstick の全データを記録)
    ├── data.py (NiziU の全投稿の全データを取得。チャンネル登録者等も含む)
    ├── delete.py (使ってないです。)
    ├── graph-test.py (グラフ生成のプログラムテスト)
    ├── main.py (YouTube Liveのチャットを取得)
    ├── need-data.py (Need U の再生回数と日付を記録(ツイートグラフ生成用))
    ├── need-tweet.py (Need U のツイート生成(グラフ生成含む))
    ├── need-view.py (Need U の再生回数を記録(ツイート数値取得用))
    ├── need.py (Need U の全データを記録)
    ├── notification.py (NiziU のYouTube投稿を通知)
    ├── retweet.py (NiziU のツイートを自動リツイート(作成中))
    ├── settings.py (.env の読み込み(全ファイルにおいて基本的に必要))
    ├── status.py (NiziU のツイートを取得(作成中))
    ├── tweet-v2.py (Chopstick のツイート生成(グラフ生成含む)
    └── tweet.py (Chopstick ツイート生成(グラフ含まない))
```

![Alt](https://repobeats.axiom.co/api/embed/e6566cf7565af1ce363bad3afb53140b17e369e1.svg "Repobeats analytics image")


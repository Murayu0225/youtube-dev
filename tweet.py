import os
import settings
from twitter import Twitter, OAuth
import pathlib
import pytz
# import pandas as pd

# df = pd.read_csv('chopstick-view.csv')
# df.tail(1)

f = open('./Data/chopstick-view.csv', 'r')
alltxt = f.readlines()
f.close()

endgyou = len(alltxt)
enddata = alltxt[endgyou-1].strip()
print(enddata)
intenddata = int(enddata)
formatenddata = "{:,}".format(intenddata)

def main():
    t = Twitter(
        auth=OAuth(
            settings.TW_TOKEN,
            settings.TW_TOKEN_SECRET,
            settings.TW_CONSUMER_KEY,
            settings.TW_CONSUMER_SECRET,
        )
    )

    msg = "現在、「NiziU(니쥬) 1st Album 「Chopstick」 MV」の再生回数は、" +  formatenddata + "回です。#NiziU\n\nhttps://www.youtube.com/watch?v=nCjmXHsRJNY"
    t.statuses.update(status=msg)

if __name__ == "__main__":
    main()

import os
import settings
from twitter import Twitter, OAuth
import pathlib
import pytz
# import pandas as pd

# df = pd.read_csv('chopstick-view.csv')
# df.tail(1)

f = open('./chopstick-view.csv', 'r')
alltxt = f.readlines()
f.close()

endgyou = len(alltxt)
enddata = alltxt[endgyou-1].strip()
print(enddata)

def main():
    t = Twitter(
        auth=OAuth(
            config.TW_TOKEN,
            config.TW_TOKEN_SECRET,
            config.TW_CONSUMER_KEY,
            config.TW_CONSUMER_SECRET,
        )
    )

    msg = "現在の、「NiziU(니쥬) 1st Album 「Chopstick」 MV」の再生数は、" +  enddata + "回です。#NiziU"
    t.statuses.update(status=msg)

if __name__ == "__main__":
    main()

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
formatenddata = "{:,}".format(enddata)

def main():
    t = Twitter(
        auth=OAuth(
            settings.TW_TOKEN,
            settings.TW_TOKEN_SECRET,
            settings.TW_CONSUMER_KEY,
            settings.TW_CONSUMER_SECRET,
        )
    )

    msg = "現在の、「NiziU(니쥬) 1st Album 「Chopstick」 MV」の再生数は、" +  formatenddata + "回です。#NiziU"
    t.statuses.update(status=msg)

if __name__ == "__main__":
    main()

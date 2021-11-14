import os
# import pandas as pd

# df = pd.read_csv('chopstick-view.csv')
# df.tail(1)

f = open('./chopstick-view.csv', 'r')
alltxt = f.readlines()
f.close()

endgyou = len(alltxt)
endtxt = alltxt[endgyou-1].strip()
print(enddata)

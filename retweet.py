import sys
import json
import oauth2 as oauth
from define_client import define_client_proc

def get_tweets_proc(client,user_name):
    nnx = 10
    url_base = "https://api.twitter.com/1.1/statuses/user_timeline.json?user_name="
    url = url_base + user_name + "&count=" + str(nnx)
    array_aa = []
    response, data = client.request(url)
    if response.status == 200:
        json_str = data.decode('utf-8')
        array_aa = json.loads(json_str)
        sys.stderr.write("len(array_aa) = %d\n" % len(array_aa))

    else:
        sys.stderr.write("*** error *** get_ids_proc ***\n")
        sys.stderr.write("Error: %d\n" % response.status)

    return  array_aa
sys.stderr.write("*** 開始 ***\n")

user_name = "NiziU__official"

client = define_client_proc()

array_aa = get_tweets_proc(client,user_name)

sys.stderr.write("len(array_aa) = %d\n" % len(array_aa))

for unit_aa in array_aa:
    print (unit_aa['created_at'])
    print (unit_aa['id'])
    print (unit_aa['text'])

sys.stderr.write("*** 終了 ***\n")

import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

YT_API = os.environ.get("YT_API")
YT_URL = os.environ.get("YT_URL")
TW_CONSUMER_KEY = os.environ.get('TW_CONSUMER_KEY')
TW_CONSUMER_SECRET = os.environ.get('TW_CONSUMER_SECRET')
TW_TOKEN = os.environ.get('TW_TOKEN')
TW_TOKEN_SECRET = os.environ.get('TW_TOKEN_SECRET')
YT_NAME = os.environ.get('YT_NAME')
YT_ID = os.environ.get('YT_ID')
YT_VERSION = os.environ.get('YT_VERSION')
TW_MESSAGE = os.environ.get('TW_MESSAGE')

# どうしてもActionの動作を見たいので機密事項ですがprintします。すぐにAPIを破棄します。
# print(YT_API)

import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

YT_API = os.environ.get("YT_API_ENV")
YT_URL = os.environ.get("YT_URL_ENV")

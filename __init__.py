import os
import requests
from time_before_ny import time_before_ny

# environment variable is as unique as possible
TELEGRAM_BOT_API_KEY = os.getenv("GET_DAYS_BEFORE_NEW_YEAR_TG_BOT_API_KEY", "WRONG KEY")



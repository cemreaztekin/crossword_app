import os

APP_NAME = "bot_theMiniCrossword"
BASE_URL = "https://www.nytimes.com/crosswords/game/mini"
URL_JSON = "https://www.nytimes.com/svc/crosswords/v6/puzzle/mini.json"
SLEEP = float(os.environ.get("SLEEP", 86400))

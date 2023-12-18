# (c) @AmznUsers | Jordan Gill

import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1166670205").split())
DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "Amazon-Bot")
AMAZON_TLD = os.environ.get("AMAZON_TLD", "in")
AMAZON_TAG = os.getenv("AMAZON_TAG", "JaiShreeRam")
FORWARD_CHANNEL_NUMBER = os.getenv("FORWARD_CHANNEL_NUMBER", 5)
BOT_TYPE_PUBLIC = os.getenv("BOT_TYPE_PUBLIC", "True").lower() == "true"
COOKIES = os.environ.get("COOKIES", '')
BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "True").lower() == "true"

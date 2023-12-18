# (c) @AmznUsers | Jordan Gill

import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6789726483:AAH9zTpUqv6GJxz5Zu-o8ftWdq-z_msRSW8")
API_ID = int(os.environ.get("API_ID", "12936189"))
API_HASH = os.environ.get("API_HASH", "7e24008e8ec33a397155b6a9d618497b")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001994128629"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1166670205").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://Gill:Gill@cluster0.gfqiphu.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "Amazon_Working")
AMAZON_TLD = os.environ.get("AMAZON_TLD", "in")
AMAZON_TAG = os.getenv("AMAZON_TAG", "gillharyana0e-21")
FORWARD_CHANNEL_NUMBER = os.getenv("FORWARD_CHANNEL_NUMBER", -1001292328024)
BOT_TYPE_PUBLIC = os.getenv("BOT_TYPE_PUBLIC", "True").lower() == "true"
COOKIES = os.environ.get("COOKIES", 's_fid=40A6029881A3C199-3B635DBDEED0AE6A; ubid-acbin=262-9487551-3295620; lc-acbin=en_IN; session-id-time=2082787201l; csm-sid=226-0318853-8569382; x-acbin="ss2ghQdCTuGvdaMJ4YoJ?cs2TS9IoGDum?fhK?P@haNxmJCP4Yp5KjwuszRH5pw?"; i18n-prefs=INR; session-id=262-4094851-8630311; csm-hit=tb:s-96Z9QMJ7RQTTRRVSBRCA|1695628644972&t:1695628648212&adb:adblk_no')
BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "True").lower() == "true"

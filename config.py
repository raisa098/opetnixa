import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQC0TJjR50U4in4eQmSHk2a7D5YDeYEdzuOZ5P4ae0DLzCOlNI7lWa6QMAIcTSxVlESJrKiT_fU7r5L1t5YeEmsvCM7XklQzdgNE_9hI1pNWm1te9OIXtpIgP9T-n7Fq71hU8y3IJORaB9DmZ-AmGlWS4gDY3BC4mGZZHq3lxXlEmvS1W2FB2vNob4nwj9ESqCgFE-oSYpoeA96X8VZ_bQHWrhUQkhsZDu_x2_jOrY1xmtDDNj5xAIPjiCEwysYpeYG9oZuZXGIbUJ8r3LCHa1RIb6lKINYGlWa_KRSvOObacu_vT7eG6FusjAQyWbvwvVQvJ2ajwZWFl2P7_b6l4LSxAAAAAUKVUL0A")
BOT_TOKEN = getenv("BOT_TOKEN", "5430611324:AAGRuWb8BxK9Q_fWh5gQAwY0ZUsmhDc8AIY")
BOT_NAME = getenv("BOT_NAME", "˹ᴄᴀᴛ ✘ ᴍᴜsɪᴄ˼")
API_ID = int(getenv("API_ID", "26505340"))
API_HASH = getenv("API_HASH", "2c687333637c38602329de84aeb64baf")
OWNER_NAME = getenv("OWNER_NAME", "˹ꝛλᴠᴇɴ˼")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Juliiannnnn")
ALIVE_NAME = getenv("ALIVE_NAME", "kintil")
BOT_USERNAME = getenv("BOT_USERNAME", "kucinggtapibot")
OWNER_ID = getenv("OWNER_ID", "2061280554")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ᴄᴀᴛ ✘ ᴀssɪsᴛᴀɴᴛ")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "pbm212")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "windtalkerr")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2061280554").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/084c206996897e2d42443.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/084c206996897e2d42443.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Sumit9969/NIXA-MUSIC-BOT")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/cb0315c63c5fce38ae3eb.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/880f7e9706591af8d0bfa.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/324399325cf48ff25a494.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/a79d792baacc982ff57bd.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cb0315c63c5fce38ae3eb.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/a79d792baacc982ff57bd.jpg")

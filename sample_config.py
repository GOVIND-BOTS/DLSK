from os import getenv

from decouple import config

APP_ID = getenv("APP_ID", "25357017")

API_HASH = getenv("API_HASH", "df7ba78cede9124c83aeda70288f51ca")

HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", "242d94ff-d398-46d6-b050-a47b9f170182")

BOT_TOKEN = config("BOT_TOKEN", "5959897792:AAEVaEAHUHj-7aXnf9xM2WDEXq22ciQgX2Y")
BOT_TOKEN2 = config("BOT_TOKEN2", "6292359535:AAEDI7EtNfVbG4VQv0cM3GTX-9WwydeuzsM")
BOT_TOKEN3 = config("BOT_TOKEN3", "6268640520:AAF8YfhXa1hMgQbe9FvwtBoxmyCrrfj1S90")
BOT_TOKEN4 = config("BOT_TOKEN4", default=None)
BOT_TOKEN5 = config("BOT_TOKEN5", default=None)
BOT_TOKEN6 = config("BOT_TOKEN6", default=None)
BOT_TOKEN7 = config("BOT_TOKEN7", default=None)
BOT_TOKEN8 = config("BOT_TOKEN8", default=None)
BOT_TOKEN9 = config("BOT_TOKEN9", default=None)
BOT_TOKEN10 = config("BOT_TOKEN10", default=None)
BOT_TOKEN11 = config("BOT_TOKEN11", default=None)
BOT_TOKEN12 = config("BOT_TOKEN12", default=None)
BOT_TOKEN13 = config("BOT_TOKEN13", default=None)
BOT_TOKEN14 = config("BOT_TOKEN14", default=None)
BOT_TOKEN15 = config("BOT_TOKEN15", default=None)
BOT_TOKEN16 = config("BOT_TOKEN16", default=None)
BOT_TOKEN17 = config("BOT_TOKEN17", default=None)
BOT_TOKEN18 = config("BOT_TOKEN18", default=None)
BOT_TOKEN19 = config("BOT_TOKEN19", default=None)
BOT_TOKEN20 = config("BOT_TOKEN20", default=None)
BOT_TOKEN21 = config("BOT_TOKEN21", default=None)
BOT_TOKEN22 = config("BOT_TOKEN22", default=None)
BOT_TOKEN23 = config("BOT_TOKEN23", default=None)
BOT_TOKEN24 = config("BOT_TOKEN24", default=None)
BOT_TOKEN25 = config("BOT_TOKEN25", default=None)
try:
    SUDO_USERS = str(getenv("SUDO_USERS", "6020570673")).split(" ")
except Exception:
    SUDO_USERS = str(getenv("SUDO_USERS", "123 456"))

START_MESSAGE = getenv("START_MESSAGE", None)

PING_PIC = getenv("PING_PIC", None)

START_PIC = getenv("START_PIC", "https://te.legra.ph/file/6aad866982e67533b7111.jpg")


HELP_MSG = getenv("HELP_MSG", None)
HELP_PIC = getenv("HELP_PIC", "https://graph.org/file/89ed7d3a2bd8aa2c61385.jpg")
LOG_CHANNEL = getenv("LOG_CHANNEL", None)

HANDLER = getenv("HANDLER", "/")

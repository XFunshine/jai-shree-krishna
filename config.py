import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "27947566"))
API_HASH = environ.get("API_HASH", "9f9f5e44b10b65b576395c0a8d2682a0")
BOT_TOKEN = environ.get("BOT_TOKEN", "7179645509:AAFGl1ordN-TycGvx3FHwzYx0wvuXD3vols")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002016103125"))
ADMINS = int(environ.get("ADMINS", "1715422029"))
DB_URI = environ.get("DB_URI", "mongodb+srv://nova:novabro99@cluster0.wkhngfn.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "chatgptvjbot")
OPENAI_API = environ.get("OPENAI_API", "")
AI = is_enabled((environ.get("AI","True")), False)

import os
from dotenv import load_dotenv

load_dotenv()

# Telegram API
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION_STRING = os.getenv("SESSION_STRING")

# Bot Owner
OWNER_ID = int(os.getenv("OWNER_ID"))

# Settings
SILENT_MODE = True
TIMEZONE = "Asia/Kolkata"

# Files
CHANNELS_FILE = "channels.json"
LOG_FILE = "logs/bot.log"

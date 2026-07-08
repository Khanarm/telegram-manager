from telethon import TelegramClient, events
from telethon.sessions import StringSession

from config import (
    API_ID,
    API_HASH,
    BOT_TOKEN,
    USERBOT1_SESSION,
    USERBOT2_SESSION,
    USERBOT3_SESSION,
    USERBOT4_SESSION
)
import commands as cmd

# ==========================
# FLASK SERVER (Render fix)
# ==========================
from flask import Flask
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

def run_web():
    app.run(host="0.0.0.0", port=10000)

threading.Thread(target=run_web).start()

# ==========================
# TELEGRAM CLIENT
# ==========================
master = TelegramClient(
    "master_bot",
    API_ID,
    API_HASH
)

ub1 = TelegramClient(
    StringSession(USERBOT1_SESSION),
    API_ID,
    API_HASH
)

ub2 = TelegramClient(
    StringSession(USERBOT2_SESSION),
    API_ID,
    API_HASH
)

ub3 = TelegramClient(
    StringSession(USERBOT3_SESSION),
    API_ID,
    API_HASH
)

ub4 = TelegramClient(
    StringSession(USERBOT4_SESSION),
    API_ID,
    API_HASH
)

userbots = [ub1, ub2, ub3, ub4]

# ==========================
# START MESSAGE
# ==========================
@master.on(events.NewMessage(pattern=r"^/start$"))
async def start(event):
    if event.sender_id != cmd.OWNER_ID:
        return
    await event.reply("✅ Userbot is running successfully!")

# ==========================
# CHANNEL COMMANDS
# ==========================
@master.on(events.NewMessage(pattern=r"^/addchannel"))
async def addchannel(event):
    await cmd.cmd_add(event)

@master.on(events.NewMessage(pattern=r"^/removechannel"))
async def removechannel(event):
    await cmd.cmd_remove(event)

@master.on(events.NewMessage(pattern=r"^/listchannels"))
async def listchannels(event):
    await cmd.cmd_list(event)

@master.on(events.NewMessage(pattern=r"^/clearchannels"))
async def clearchannels(event):
    await cmd.cmd_clear(event)

# ==========================
# NAME COMMANDS
# ==========================
@master.on(events.NewMessage(pattern=r"^/setname"))
async def setname(event):
    await cmd.set_name_all(client, event)

@master.on(events.NewMessage(pattern=r"^/rename"))
async def rename(event):
    await cmd.rename_one(client, event)

# ==========================
# USERNAME COMMANDS
# ==========================
@master.on(events.NewMessage(pattern=r"^/setusername"))
async def setusername(event):
    await cmd.set_username_all(client, event)

@master.on(events.NewMessage(pattern=r"^/username"))
async def username(event):
    await cmd.username_one(client, event)

# ==========================
# ABOUT COMMANDS
# ==========================
@master.on(events.NewMessage(pattern=r"^/setabout"))
async def setabout(event):
    await cmd.set_about_all(client, event)

@master.on(events.NewMessage(pattern=r"^/about"))
async def about(event):
    await cmd.about_one(client, event)

# ==========================
# PHOTO COMMANDS
# ==========================
@master.on(events.NewMessage(pattern=r"^/setphoto"))
async def setphoto(event):
    await cmd.set_photo_all(client, event)

@master.on(events.NewMessage(pattern=r"^/photo"))
async def photo(event):
    await cmd.photo_one(client, event)

# ==========================
# BROADCAST COMMANDS
# ==========================
@master.on(events.NewMessage(pattern=r"^/broadcastall"))
async def broadcastall(event):
    await cmd.broadcast_all(client, event)

@master.on(events.NewMessage(pattern=r"^/broadcast"))
async def broadcast(event):
    await cmd.broadcast_one(client, event)

# ==========================
# MAIN START
# ==========================
print("🚀 Bot is starting...")

client.start()
print("✅ Bot is running!")

client.run_until_disconnected()

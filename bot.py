import os
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

from config import API_ID, API_HASH, STRING_SESSION
import commands as cmd


# ==========================
# CLIENT (MUST BE FIRST)
# ==========================
client = TelegramClient(
    StringSession(STRING_SESSION),
    API_ID,
    API_HASH
)


# ==========================
# HANDLERS
# ==========================

@client.on(events.NewMessage(pattern=r"^/start$"))
async def start(event):
    if event.sender_id != cmd.OWNER_ID:
        return
    await event.reply("✅ Userbot is running successfully!")


@client.on(events.NewMessage(pattern=r"^/addchannel"))
async def addchannel(event):
    await cmd.cmd_add(event)


@client.on(events.NewMessage(pattern=r"^/removechannel"))
async def removechannel(event):
    await cmd.cmd_remove(event)


@client.on(events.NewMessage(pattern=r"^/listchannels"))
async def listchannels(event):
    await cmd.cmd_list(event)


@client.on(events.NewMessage(pattern=r"^/clearchannels"))
async def clearchannels(event):
    await cmd.cmd_clear(event)


@client.on(events.NewMessage(pattern=r"^/setname"))
async def setname(event):
    await cmd.set_name_all(client, event)


@client.on(events.NewMessage(pattern=r"^/rename"))
async def rename(event):
    await cmd.rename_one(client, event)


@client.on(events.NewMessage(pattern=r"^/setusername"))
async def setusername(event):
    await cmd.set_username_all(client, event)


@client.on(events.NewMessage(pattern=r"^/username"))
async def username(event):
    await cmd.username_one(client, event)


@client.on(events.NewMessage(pattern=r"^/setabout"))
async def setabout(event):
    await cmd.set_about_all(client, event)


@client.on(events.NewMessage(pattern=r"^/about"))
async def about(event):
    await cmd.about_one(client, event)


@client.on(events.NewMessage(pattern=r"^/setphoto"))
async def setphoto(event):
    await cmd.set_photo_all(client, event)


@client.on(events.NewMessage(pattern=r"^/photo"))
async def photo(event):
    await cmd.photo_one(client, event)


@client.on(events.NewMessage(pattern=r"^/broadcastall"))
async def broadcastall(event):
    await cmd.broadcast_all(client, event)


@client.on(events.NewMessage(pattern=r"^/broadcast"))
async def broadcast(event):
    await cmd.broadcast_one(client, event)


# ==========================
# MAIN LOOP
# ==========================
async def main():
    print("🚀 Starting bot...")

    await client.start()
    print("✅ Bot started")

    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())

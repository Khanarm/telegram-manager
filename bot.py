import os
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

from config import API_ID, API_HASH, STRING_SESSION
import commands as cmd

client = None


@client.on(events.NewMessage(pattern=r"^/start$"))
async def start(event):
    if event.sender_id != cmd.OWNER_ID:
        return
    await event.reply("✅ Userbot is running successfully!")


async def main():
    global client

    print("🚀 Starting bot...")

    client = TelegramClient(
        StringSession(STRING_SESSION),
        API_ID,
        API_HASH
    )

    await client.start()
    print("✅ Bot started")

    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())

from telethon import TelegramClient, events
from telethon.sessions import StringSession

from config import (
    API_ID,
    API_HASH,
    SESSION_STRING,
    OWNER_ID
)

from database import create_tables

client = TelegramClient(
    StringSession(SESSION_STRING),
    API_ID,
    API_HASH
)

print("===================================")
print(" Telegram Channel Manager Started ")
print("===================================")


@client.on(events.NewMessage(outgoing=True))
async def owner_commands(event):

    # Sirf owner ke commands
    if event.sender_id != OWNER_ID:
        return

    text = event.raw_text

    if text == "/ping":
        await event.reply("✅ Bot Online")


async def main():

    create_tables()

    await client.start()

    me = await client.get_me()

    print(f"Logged in as: {me.first_name}")
    print(f"User ID: {me.id}")

    await client.run_until_disconnected()


if __name__ == "__main__":
    client.loop.run_until_complete(main())

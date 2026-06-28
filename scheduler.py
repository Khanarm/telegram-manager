import asyncio
from datetime import datetime, timedelta
from telethon import TelegramClient

from config import API_ID, API_HASH, SESSION_NAME
from database import get_channels

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

# 🔥 Example posts (tum isko DB ya file se bhi connect kar sakte ho)
POSTS = [
    "🔥 Daily Update: New offer live!",
    "🎮 Check out latest game deals!",
    "🚀 Join now and earn rewards!",
]

INTERVAL_MINUTES = 60  # हर 60 min me post

async def send_post():
    channels = get_channels()

    if not channels:
        print("No channels found!")
        return

    for channel in channels:
        for post in POSTS:
            try:
                await client.send_message(channel, post)
                print(f"Sent to {channel}: {post}")
                await asyncio.sleep(5)  # spam protection
            except Exception as e:
                print(f"Error sending to {channel}: {e}")

async def scheduler_loop():
    while True:
        print(f"[{datetime.now()}] Running scheduled posts...")
        await send_post()

        await asyncio.sleep(INTERVAL_MINUTES * 60)

async def start_scheduler():
    await client.start()
    print("Scheduler started...")
    await scheduler_loop()

if __name__ == "__main__":
    asyncio.run(start_scheduler())

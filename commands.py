from telethon import functions
from database import (
    add_channel,
    remove_channel,
    get_channels,
    channel_exists,
)

# ==========================
# Add Channel
# ==========================

async def cmd_add(event):
    try:
        channel = event.raw_text.split(maxsplit=1)[1].strip()

        if channel_exists(channel):
            await event.reply("⚠️ Channel already added.")
            return

        add_channel(channel)

        await event.reply(f"✅ Added: {channel}")

    except:
        await event.reply("Usage:\n/addchannel @channel")


# ==========================
# Remove Channel
# ==========================

async def cmd_remove(event):
    try:
        channel = event.raw_text.split(maxsplit=1)[1].strip()

        remove_channel(channel)

        await event.reply(f"🗑 Removed: {channel}")

    except:
        await event.reply("Usage:\n/removechannel @channel")


# ==========================
# List Channels
# ==========================

async def cmd_list(event):

    channels = get_channels()

    if not channels:
        await event.reply("No channels added.")
        return

    msg = "📋 Channel List\n\n"

    for ch in channels:
        msg += f"• {ch}\n"

    await event.reply(msg)

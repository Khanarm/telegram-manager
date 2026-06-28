from telethon import functions
from database import (
    add_channel,
    remove_channel,
    get_channels,
    channel_exists,
)

# ==========================
# ADD CHANNEL
# ==========================

async def cmd_add(event):
    try:
        channel = event.raw_text.split(maxsplit=1)[1].strip()

        if channel_exists(channel):
            await event.reply("⚠️ Channel already exists.")
            return

        add_channel(channel)
        await event.reply(f"✅ Added: {channel}")

    except Exception:
        await event.reply("Usage:\n/addchannel @channel")


# ==========================
# REMOVE CHANNEL
# ==========================

async def cmd_remove(event):
    try:
        channel = event.raw_text.split(maxsplit=1)[1].strip()

        remove_channel(channel)

        await event.reply(f"🗑 Removed: {channel}")

    except Exception:
        await event.reply("Usage:\n/removechannel @channel")


# ==========================
# LIST CHANNELS
# ==========================

async def cmd_list(event):

    channels = get_channels()

    if not channels:
        await event.reply("📭 No channels added.")
        return

    text = "📋 Saved Channels\n\n"

    for i, ch in enumerate(channels, start=1):
        text += f"{i}. {ch}\n"

    await event.reply(text)

# ==========================
# CHANGE NAME OF ALL CHANNELS
# /setname New Name
# ==========================

async def set_name_all(client, event):

    try:
        new_name = event.raw_text.split(maxsplit=1)[1].strip()
    except IndexError:
        await event.reply("Usage:\n/setname New Channel Name")
        return

    channels = get_channels()

    if not channels:
        await event.reply("❌ No channels added.")
        return

    success = 0
    failed = 0

    for channel in channels:
        try:
            await client(
                functions.channels.EditTitleRequest(
                    channel=channel,
                    title=new_name
                )
            )
            success += 1
        except Exception as e:
            print(f"{channel}: {e}")
            failed += 1

    await event.reply(
        f"✅ Updated: {success}\n❌ Failed: {failed}"
    )


# ==========================
# CHANGE NAME OF ONE CHANNEL
# /rename @channel New Name
# ==========================

async def rename_one(client, event):

    parts = event.raw_text.split(maxsplit=2)

    if len(parts) < 3:
        await event.reply(
            "Usage:\n/rename @channel New Name"
        )
        return

    channel = parts[1]
    new_name = parts[2]

    try:
        await client(
            functions.channels.EditTitleRequest(
                channel=channel,
                title=new_name
            )
        )

        await event.reply("✅ Channel renamed successfully.")

    except Exception as e:
        await event.reply(f"❌ {e}")


# ==========================
# CHANGE ABOUT OF ALL CHANNELS
# /setabout Description
# ==========================

async def set_about_all(client, event):

    try:
        about = event.raw_text.split(maxsplit=1)[1].strip()
    except IndexError:
        await event.reply("Usage:\n/setabout Description")
        return

    channels = get_channels()

    success = 0

    for channel in channels:
        try:
            await client(
                functions.channels.EditAboutRequest(
                    channel=channel,
                    about=about
                )
            )
            success += 1
        except Exception as e:
            print(e)

    await event.reply(
        f"✅ About updated in {success} channels."
                 )


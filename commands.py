from telethon import functions
from database import (
    add_channel,
    remove_channel,
    get_channels,
    clear_channels,
    channel_exists,
)
from config import OWNER_ID


# ==========================
# OWNER CHECK
# ==========================

async def is_owner(event):
    if event.sender_id != OWNER_ID:
        await event.reply("❌ You are not authorized.")
        return False
    return True


# ==========================
# ADD CHANNEL
# /addchannel @channel
# ==========================

async def cmd_add(event):
    if not await is_owner(event):
        return

    try:
        channel = event.raw_text.split(maxsplit=1)[1].strip()

        if channel_exists(channel):
            await event.reply("⚠️ Channel already added.")
            return

        add_channel(channel)

        await event.reply(
            f"✅ Channel added:\n{channel}"
        )

    except Exception:
        await event.reply(
            "Usage:\n/addchannel @channel"
        )


# ==========================
# REMOVE CHANNEL
# /removechannel @channel
# ==========================

async def cmd_remove(event):
    if not await is_owner(event):
        return

    try:
        channel = event.raw_text.split(maxsplit=1)[1].strip()

        remove_channel(channel)

        await event.reply(
            f"🗑 Removed:\n{channel}"
        )

    except Exception:
        await event.reply(
            "Usage:\n/removechannel @channel"
        )


# ==========================
# LIST CHANNELS
# /listchannels
# ==========================

async def cmd_list(event):
    if not await is_owner(event):
        return

    channels = get_channels()

    if not channels:
        await event.reply("📭 No channels saved.")
        return

    text = "📋 Saved Channels\n\n"

    for i, channel in enumerate(channels, start=1):
        text += f"{i}. {channel}\n"

    text += f"\nTotal: {len(channels)}"

    await event.reply(text)


# ==========================
# CLEAR ALL CHANNELS
# /clearchannels
# ==========================

async def cmd_clear(event):
    if not await is_owner(event):
        return

    clear_channels()

    await event.reply(
        "🗑 All channels removed successfully."
    )

# ==========================
# CHANGE NAME OF ALL CHANNELS
# /setname New Channel Name
# ==========================

async def set_name_all(client, event):
    if not await is_owner(event):
        return

    try:
        new_name = event.raw_text.split(maxsplit=1)[1].strip()
    except IndexError:
        await event.reply(
            "Usage:\n/setname New Channel Name"
        )
        return

    channels = get_channels()

    if not channels:
        await event.reply("❌ No channels saved.")
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
        f"✅ Name updated.\n\n"
        f"Success: {success}\n"
        f"Failed: {failed}"
    )


# ==========================
# CHANGE NAME OF ONE CHANNEL
# /rename @channel New Name
# ==========================

async def rename_one(client, event):
    if not await is_owner(event):
        return

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

        await event.reply(
            f"✅ Channel renamed successfully.\n\n"
            f"Channel: {channel}\n"
            f"New Name: {new_name}"
        )

    except Exception as e:
        await event.reply(f"❌ {e}")

# ==========================
# CHANGE USERNAME OF ALL CHANNELS
# /setusername newusername
# ==========================

async def set_username_all(client, event):
    if not await is_owner(event):
        return

    try:
        new_username = event.raw_text.split(maxsplit=1)[1].strip().replace("@", "")
    except IndexError:
        await event.reply(
            "Usage:\n/setusername newusername"
        )
        return

    channels = get_channels()

    if not channels:
        await event.reply("❌ No channels saved.")
        return

    success = 0
    failed = 0

    for i, channel in enumerate(channels, start=1):
        try:
            username = f"{new_username}{i}"

            await client(
                functions.channels.UpdateUsernameRequest(
                    channel=channel,
                    username=username
                )
            )

            success += 1

        except Exception as e:
            print(f"{channel}: {e}")
            failed += 1

    await event.reply(
        f"✅ Username updated.\n\n"
        f"Success: {success}\n"
        f"Failed: {failed}"
    )


# ==========================
# CHANGE USERNAME OF ONE CHANNEL
# /username @channel newusername
# ==========================

async def username_one(client, event):
    if not await is_owner(event):
        return

    parts = event.raw_text.split(maxsplit=2)

    if len(parts) < 3:
        await event.reply(
            "Usage:\n/username @channel newusername"
        )
        return

    channel = parts[1]
    username = parts[2].replace("@", "")

    try:
        await client(
            functions.channels.UpdateUsernameRequest(
                channel=channel,
                username=username
            )
        )

        await event.reply(
            f"✅ Username updated.\n\n"
            f"Channel: {channel}\n"
            f"Username: @{username}"
        )

    except Exception as e:
        await event.reply(f"❌ {e}")

# ==========================
# CHANGE DESCRIPTION OF ALL CHANNELS
# /setabout New Description
# ==========================

async def set_about_all(client, event):
    if not await is_owner(event):
        return

    try:
        about = event.raw_text.split(maxsplit=1)[1].strip()
    except IndexError:
        await event.reply(
            "Usage:\n/setabout New Description"
        )
        return

    channels = get_channels()

    if not channels:
        await event.reply("❌ No channels saved.")
        return

    success = 0
    failed = 0

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
            print(f"{channel}: {e}")
            failed += 1

    await event.reply(
        f"✅ Description updated.\n\n"
        f"Success: {success}\n"
        f"Failed: {failed}"
    )


# ==========================
# CHANGE DESCRIPTION OF ONE CHANNEL
# /about @channel New Description
# ==========================

async def about_one(client, event):
    if not await is_owner(event):
        return

    parts = event.raw_text.split(maxsplit=2)

    if len(parts) < 3:
        await event.reply(
            "Usage:\n/about @channel New Description"
        )
        return

    channel = parts[1]
    about = parts[2]

    try:
        await client(
            functions.channels.EditAboutRequest(
                channel=channel,
                about=about
            )
        )

        await event.reply(
            f"✅ Description updated.\n\n"
            f"Channel: {channel}"
        )

    except Exception as e:
        await event.reply(f"❌ {e}")

from telethon.tl.functions.channels import EditPhotoRequest
from telethon.tl.types import InputChatUploadedPhoto

# ==========================
# CHANGE PHOTO OF ALL CHANNELS
# Reply to image:
# /setphoto
# ==========================

async def set_photo_all(client, event):
    if not await is_owner(event):
        return

    if not event.is_reply:
        await event.reply(
            "Reply to a photo with:\n/setphoto"
        )
        return

    reply = await event.get_reply_message()

    if not reply.photo:
        await event.reply("❌ Reply must contain a photo.")
        return

    file = await client.download_media(reply, file=bytes)
    channels = get_channels()

    if not channels:
        await event.reply("❌ No channels saved.")
        return

    success = 0
    failed = 0

    for channel in channels:
        try:
            uploaded = await client.upload_file(file)

            await client(
                EditPhotoRequest(
                    channel=channel,
                    photo=InputChatUploadedPhoto(uploaded)
                )
            )

            success += 1

        except Exception as e:
            print(f"{channel}: {e}")
            failed += 1

    await event.reply(
        f"✅ Profile photos updated.\n\n"
        f"Success: {success}\n"
        f"Failed: {failed}"
    )


# ==========================
# CHANGE PHOTO OF ONE CHANNEL
# Reply to image:
# /photo @channel
# ==========================

async def photo_one(client, event):
    if not await is_owner(event):
        return

    if not event.is_reply:
        await event.reply(
            "Reply to a photo with:\n/photo @channel"
        )
        return

    parts = event.raw_text.split(maxsplit=1)

    if len(parts) < 2:
        await event.reply(
            "Usage:\n/photo @channel"
        )
        return

    channel = parts[1]

    reply = await event.get_reply_message()

    if not reply.photo:
        await event.reply("❌ Reply must contain a photo.")
        return

    try:
        file = await client.download_media(reply, file=bytes)
        uploaded = await client.upload_file(file)

        await client(
            EditPhotoRequest(
                channel=channel,
                photo=InputChatUploadedPhoto(uploaded)
            )
        )

        await event.reply(
            f"✅ Profile photo updated.\n\n"
            f"Channel: {channel}"
        )

    except Exception as e:
        await event.reply(f"❌ {e}")

# ==========================
# SILENT BROADCAST TO ALL CHANNELS
# Reply to any message:
# /broadcastall
# ==========================

async def broadcast_all(client, event):
    if not await is_owner(event):
        return

    if not event.is_reply:
        await event.reply(
            "Reply to any message with:\n/broadcastall"
        )
        return

    reply = await event.get_reply_message()

    channels = get_channels()

    if not channels:
        await event.reply("❌ No channels saved.")
        return

    success = 0
    failed = 0

    for channel in channels:
        try:
            await client.forward_messages(
                entity=channel,
                messages=reply,
                from_peer=reply.chat_id,
                silent=True
            )

            success += 1

        except Exception as e:
            print(f"{channel}: {e}")
            failed += 1

    await event.reply(
        f"✅ Broadcast completed.\n\n"
        f"Success: {success}\n"
        f"Failed: {failed}"
    )


# ==========================
# SILENT BROADCAST TO ONE CHANNEL
# Reply to any message:
# /broadcast @channel
# ==========================

async def broadcast_one(client, event):
    if not await is_owner(event):
        return

    if not event.is_reply:
        await event.reply(
            "Reply to any message with:\n/broadcast @channel"
        )
        return

    parts = event.raw_text.split(maxsplit=1)

    if len(parts) < 2:
        await event.reply(
            "Usage:\n/broadcast @channel"
        )
        return

    channel = parts[1]

    reply = await event.get_reply_message()

    try:
        await client.forward_messages(
            entity=channel,
            messages=reply,
            from_peer=reply.chat_id,
            silent=True
        )

        await event.reply(
            f"✅ Broadcast sent successfully.\n\n"
            f"Channel: {channel}"
        )

    except Exception as e:
        await event.reply(f"❌ {e}")

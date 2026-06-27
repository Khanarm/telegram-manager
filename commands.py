from telethon import functions

from database import (
    add_channel,
    remove_channel,
    get_channels,
    channel_exists,
    get_channel_count,
    clear_channels
)

from telethon import functions
from database import get_channels


async def set_name_all(client, new_name):

    channels = get_channels()

    success = 0

    for username, title in channels:

        try:
            await client(
                functions.channels.EditTitleRequest(
                    channel=username,
                    title=new_name
                )
            )

            success += 1

        except Exception as e:
            print(e)

    return success

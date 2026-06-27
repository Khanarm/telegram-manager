import json

CHANNELS_FILE = "channels.json"


def load_channels():
    try:
        with open(CHANNELS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data["channels"]
    except:
        return []


def save_channels(channels):
    with open(CHANNELS_FILE, "w", encoding="utf-8") as f:
        json.dump(
            {
                "channels": channels
            },
            f,
            indent=4
        )


def add_channel(username):

    channels = load_channels()

    if username not in channels:
        channels.append(username)
        save_channels(channels)
        return True

    return False


def remove_channel(username):

    channels = load_channels()

    if username in channels:
        channels.remove(username)
        save_channels(channels)
        return True

    return False


def get_all_channels():
    return load_channels()

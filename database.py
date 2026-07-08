from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)

db = client["telegram_manager"]

channels = db["channels"]
userbots = db["userbots"]


# ==========================
# CHANNELS
# ==========================

def add_channel(username, owner_bot="default"):
    if channels.find_one({"username": username}):
        return False

    channels.insert_one({
        "username": username,
        "owner_bot": owner_bot
    })
    return True


def remove_channel(username):
    channels.delete_one({"username": username})


def get_channels():
    return list(channels.find({}, {"_id": 0}))


def get_channel(username):
    return channels.find_one(
        {"username": username},
        {"_id": 0}
    )


def channel_exists(username):
    return channels.find_one({"username": username}) is not None


def update_channel_owner(username, owner_bot):
    channels.update_one(
        {"username": username},
        {
            "$set": {
                "owner_bot": owner_bot
            }
        }
    )


def clear_channels():
    channels.delete_many({})


def get_channel_count():
    return channels.count_documents({})


# ==========================
# USERBOTS
# ==========================

def add_userbot(bot_id, string_session):
    if userbots.find_one({"bot_id": bot_id}):
        return False

    userbots.insert_one({
        "bot_id": bot_id,
        "string_session": string_session
    })
    return True


def remove_userbot(bot_id):
    userbots.delete_one({"bot_id": bot_id})


def get_userbots():
    return list(userbots.find({}, {"_id": 0}))


def get_userbot(bot_id):
    return userbots.find_one(
        {"bot_id": bot_id},
        {"_id": 0}
    )


def update_userbot(bot_id, string_session):
    userbots.update_one(
        {"bot_id": bot_id},
        {
            "$set": {
                "string_session": string_session
            }
        }
    )


def close_database():
    client.close()

from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["telegram_manager"]
channels = db["channels"]


def add_channel(username):
    if channels.find_one({"username": username}):
        return False
    channels.insert_one({"username": username})
    return True


def remove_channel(username):
    channels.delete_one({"username": username})


def get_channels():
    return [doc["username"] for doc in channels.find({}, {"_id": 0, "username": 1})]


def channel_exists(username):
    return channels.find_one({"username": username}) is not None


def clear_channels():
    channels.delete_many({})


def get_channel_count():
    return channels.count_documents({})


def close_database():
    client.close()

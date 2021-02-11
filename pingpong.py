import discord
from datetime import datetime

def ping(message):
    return datetime.timestamp(datetime.now()) - datetime.timestamp(message.created_at)
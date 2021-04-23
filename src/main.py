import asyncio
import json
from datetime import datetime

import discord

from commands import *

client = discord.Client()
CONFIGS = json.load(open("settings.json"))

cooldown = 3
lastUse = {"": 0}

def is_me(m):
    return m.author == client.user

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    lastUse["^sys"] = datetime.timestamp(datetime.now())

@client.event
async def on_message(message):

    print(str(message.created_at) +
          "=> Message from {0.author} at channel  #{0.channel} : {0.content}".format(message))

    if message.author is client.user.bot or message.author == message.guild.me:
        return

# Main body of bot
    if message.content.startswith("{}help".format(CONFIGS["prefix"])):
        
        await help.help(message=message, config = CONFIGS, c_args=[])

client.run(CONFIGS["token"])
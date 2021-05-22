import asyncio
import json
from datetime import datetime
from unittest.main import main

import os, sys
import discord
from utils.configmanager import cfg

if __name__ != "__main__": 
    sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    from .commands import *
else:
    import commands

client = discord.Client()

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'settings.json')

main_cfg = json.load(open(filename))

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
    config = cfg(message=message, dbConfig=main_cfg["Database"])

    print(str(message.created_at) +
          "=> Message from {0.author} at channel  #{0.channel} : {0.content}".format(message))

    if message.author is client.user.bot or message.author == message.guild.me:
        return
    prefix = await config.get_prefix()

# Main body of bot
    if message.content.startswith("{}help".format(prefix)):
        await commands.help.help(message=message, config = cfg, c_args=[])

client.run(main_cfg["Token"])
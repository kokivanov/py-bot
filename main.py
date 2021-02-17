import asyncio
import json
from datetime import datetime

import discord

from utils import argsUtils
from utils import handler
from utils import nsfw

client = discord.Client()
CONFIGS = json.load(open("settings.json"))
settings = json.load(open("usersettings.json"))

cooldown = 3
lastUse = {"": 0}

cl_nsfw = cl_nsfw = nsfw.nsfw(
            duname=settings["Danbooru"]["username"],
            dapi=settings["Danbooru"]["api_key"],
            rid=settings["Reddit"]["id"],
            rsec=settings["Reddit"]["secret"],
            rname=settings["Reddit"]["scriptname"],
            runame=settings["Reddit"]["username"],
            rpass=settings["Reddit"]["password"]
        )

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

    if message.author == client.user.bot or message.author == message.guild.me:
        return

# Main body of bot
    if message.content.startswith(CONFIGS["PREFIX"]):
        # Sets timestamps to usage list
        currentUse = datetime.timestamp(datetime.now())
        if currentUse - lastUse["^sys"] > cooldown:
            lastUse.clear()
        lastUse["^sys"] = currentUse

        # Checking if user has cooldown
        if message.author.mention in lastUse.keys() and currentUse - lastUse.get(message.author.mention) < cooldown:
            print(
                str(cooldown - (currentUse - lastUse.get(message.author.mention))) + "left")
            return
        # Sets last usage timestamp
        if message.author.mention in lastUse.keys():
            lastUse.pop(message.author.mention)
            lastUse.update({message.author.mention: currentUse})
        else:
            lastUse.update({message.author.mention: currentUse})

        tmpcmd = message.content.split(" ")[0].lower()
        command = str(tmpcmd[len(CONFIGS["PREFIX"]):len(tmpcmd) + 1])
        del tmpcmd
        args = argsUtils.parseArguments(message, CONFIGS["PREFIX"])

        print("Command \"" + command + "\" has args: " + str(args))

        # Calling commands
        if message.author != client.user.bot:
            await handler.handler(command=command, args=args, message=message, CONFIGS=CONFIGS, cl_nsfw=cl_nsfw)

client.run(CONFIGS["TOKEN"])

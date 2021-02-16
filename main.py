import asyncio
import json
from datetime import datetime

import discord

from utils import argsUtils

client = discord.Client()
CONFIGS = json.load(open("settings.json"))

if CONFIGS["ENABLED_MODULES"]["PING"]:
    from utils.pingpong import ping
if CONFIGS["ENABLED_MODULES"]["GAME_R"]:
    from utils import game_r
if CONFIGS["ENABLED_MODULES"]["ADMUTILS"]:
    from utils import admin

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

    if message.author == client.user.bot:
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
        if CONFIGS["ENABLED_MODULES"]["GAME_R"]:
            if command == "dice":
                await message.channel.send("Rolling... Rolling... And... " + message.author.mention + " rolls **" + str(game_r.roll_dice(args))+"**")
            if command == "random":
                await message.channel.send(message.author.mention + ", stars say that your number is **" + str(game_r.random_rn(args)) + "**")

        if CONFIGS["ENABLED_MODULES"]["HI_MESSAGE"] and (command == "hi" or command == "hello"):
            await message.channel.send('Hello, ' + message.author.mention + '!')
            await message.add_reaction(CONFIGS["HI_MESSAGE"]["REACTION"])

        if CONFIGS["ENABLED_MODULES"]["PING"] and command == "ping":
            await message.channel.send('Pong! Ping is **' + str(round(ping(message) * 1000)) + 'ms.** 🏓')

        if CONFIGS["ENABLED_MODULES"]["ADMUTILS"] and command == "clear":            
            mes = await message.channel.send("Bot deleted **" + str(await admin.clear(message, args)) + "** message(s).")
            await asyncio.sleep(5)
            await mes.delete()

        if CONFIGS["ENABLED_MODULES"]["SUDO"] and command == "sudo" or command == "say":
            await admin.say(message, args)

client.run(CONFIGS["TOKEN"])

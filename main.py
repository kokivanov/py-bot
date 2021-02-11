import json
import discord
from discord.utils import get
from datetime import datetime
from pingpong import ping

client = discord.Client()

CONFIGS = json.load(open("settings.json"))


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    print(str(message.created_at) + "=> Message from {0.author} at channel {0.channel} : {0.content}".format(message))

    if message.author == client.user:
        return

    if message.content.startswith(CONFIGS["PREFIX"]):

        tmpcmd = message.content.split(" ")[0].lower()
        command = str(tmpcmd[len(CONFIGS["PREFIX"]):len(tmpcmd) + 1])
        del tmpcmd
        args = message.content.split(" ")[1:]

        print("Command \"" + command + "\" has args: " + str(args))

        if CONFIGS["ENABLED_MODULES"]["HI_MESSAGE"] and (command == "hi" or command == "hello"):
            await message.channel.send('Hello, ' + message.author.mention + '!')
            await message.add_reaction(CONFIGS["HI_MESSAGE"]["REACTION"])

        if CONFIGS["ENABLED_MODULES"]["PING"] and command == "ping":
            await message.channel.send('Pong! Ping is **' + str(round(ping(message) * 1000)) + 'ms.** 🏓')
            #print(round(ping(message) * 1000))

client.run(CONFIGS["TOKEN"])

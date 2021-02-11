import json
import discord
from discord.utils import get
from datetime import datetime

client = discord.Client()

CONFIGS = json.load(open("settings.json"))

if CONFIGS["ENABLED_MODULES"]["PING"] == True:
    from pingpong import ping

if CONFIGS["ENABLED_MODULES"]["GAME_R"] == True:
    from utils import game_r

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

        if CONFIGS["ENABLED_MODULES"]["GAME_R"] and command == "dice":
            a = 2
            b = 6
            if len(args) < 1:
                args.append(a)
                args.append(b)
            elif len(args) < 2:
                if not args[0].isdigit():
                    args[0] = a
                args.append(b)
            elif len(args) < 3:
                if not args[0].isdigit():
                    args[0] = a
                if not args[1].isdigit():
                    args[1] = b

            try:
                await message.channel.send("Rolling... Rolling... And... " + message.author.mention + " rolls **" + str(game_r.roll_dice(int(args[0]), int(args[1])))+"**")
            except:
                print("Arguments error")

        if CONFIGS["ENABLED_MODULES"]["GAME_R"] and command == "random":
            a = 0
            b = 10
            if len(args) < 1:
                args.append(a)
                args.append(b)
            elif len(args) < 2:
                if not args[0].isdigit():
                    args[0] = a
                args.append(b)
            elif len(args) < 3:
                if not args[0].isdigit():
                    args[0] = a
                if not args[1].isdigit():
                    args[1] = b

            try:
                await message.channel.send(message.author.mention + ", stars say that your number is **" + str(game_r.random_rn(int(args[0]), int(args[1]))) + "**")
            except:
                print("Arguments error")

        if CONFIGS["ENABLED_MODULES"]["HI_MESSAGE"] and (command == "hi" or command == "hello"):
            await message.channel.send('Hello, ' + message.author.mention + '!')
            await message.add_reaction(CONFIGS["HI_MESSAGE"]["REACTION"])

        if CONFIGS["ENABLED_MODULES"]["PING"] and command == "ping":
            await message.channel.send('Pong! Ping is **' + str(round(ping(message) * 1000)) + 'ms.** 🏓')

client.run(CONFIGS["TOKEN"])
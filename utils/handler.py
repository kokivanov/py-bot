import discord
from utils import cadmin, argsUtils, game_r, pingpong
import asyncio

async def handler(command : str, args : [], message : discord.Message, CONFIGS : dict) -> int:
    if CONFIGS["ENABLED_MODULES"]["GAME_R"]:
        if command == "dice":
            await message.channel.send("Rolling... Rolling... And... " + message.author.mention + " rolls **" + str(game_r.roll_dice(args))+"**")
        if command == "random":
            await message.channel.send(message.author.mention + ", stars say that your number is **" + str(game_r.random_rn(args)) + "**")

    if CONFIGS["ENABLED_MODULES"]["HI_MESSAGE"] and (command == "hi" or command == "hello"):
        await message.channel.send('Hello, ' + message.author.mention + '!')
        await message.add_reaction(CONFIGS["HI_MESSAGE"]["REACTION"])

    if CONFIGS["ENABLED_MODULES"]["PING"] and command == "ping":
        await message.channel.send('Pong! Ping is **' + str(round(pingpong.ping(message) * 1000)) + 'ms.** 🏓')

    #Admin

    if CONFIGS["ENABLED_MODULES"]["ADMUTILS"] and message.author.guild_permissions.administrator:
        if (command == "clear" or command == "purge"):            
            mes = await message.channel.send("Bot deleted **" + str(await cadmin.clear(message, args)) + "** message(s).")
            await asyncio.sleep(5)
            await mes.delete()

        if (command == "sudo" or command == "say"):
            await cadmin.say(message, args)

    elif not message.author.guild_permissions.administrator:
        await message.channel.send("Sorry " + message.author.mention + ", you don't have permission to do that")

if __name__ == "__main__":
    handler("say", )
import discord
from utils import cadmin, argsUtils, game_r, pingpong, medias
import asyncio
import json
import requests

fl = open("usersettings.json")
settings = json.loads(fl.read())


async def handler(command: str, args: [], message: discord.Message, CONFIGS: dict, cl_medias: medias.medias) -> int:
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

    # NSFW

    if CONFIGS["ENABLED_MODULES"]["NSFW"]:
        if command == "sendnudes" or command == "r34" or command == "porn" or command == "hentai" or command == "jerk":
            request = cl_medias.handler(args=args)
            if request.endswith(".jpg") or request.endswith(".png") or request.endswith(".gif"):
                embed = discord.Embed().set_image(url=str(request))
                embed.add_field(name="**Link**", value=str(request))
                embed.title = "Some pervy stuff for " + message.author.display_name + "さん"
                await message.channel.send(content=(message.author.mention + " Here is your pervy stuff:\n"), embed=embed)
            else:
                embed = discord.Embed().add_field(name="**Link**", value=str(request))
                embed.title = "Some pervy stuff for " + message.author.display_name + "さん"
                await message.channel.send(content=(message.author.mention + " Here is your pervy stuff:\n"), embed=embed)

    # Admin

    if CONFIGS["ENABLED_MODULES"]["ADMUTILS"]:
        if (command == "clear" or command == "purge"):
            if not message.author.guild_permissions.administrator:
                await message.channel.send("Sorry " + message.author.mention + ", you don't have permission to do that")
            else:
                mes = await message.channel.send("Bot deleted **" + str(await cadmin.clear(message, args)) + "** message(s).")
                await asyncio.sleep(5)
                await mes.delete()

        if (command == "sudo" or command == "say"):
            if not message.author.guild_permissions.administrator:
                await message.channel.send("Sorry " + message.author.mention + ", you don't have permission to do that")
            else:
                await cadmin.say(message, args)

    try:
        await message.delete()
    except:
        print("Can't delete message => " + str(Exception.args))

# if __name__ == "__main__":
#    handler("say", )

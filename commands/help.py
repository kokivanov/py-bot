import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils import commandtemplate
import discord
import asyncio

import commands
import modules

def ltos(lst):
    format_list = ['{:>3}' for item in lst] 
    s = ', '.join(format_list)
    return s.format(*lst)

async def fn_help(message, config, c_args, *args, **kwargs):
    availableCommands = [getattr(getattr(commands, i), i) for i in dir(commands) if not i.startswith("__")]

    availableModules = {}
    for i in dir(modules):
        if not i.startswith("__"):
            availableModules[i] = [getattr(getattr(getattr(modules, i), j), j) for j in dir(getattr(modules, i)) if not j.startswith("__")]
    
    print("{}".format([i.name for i in availableCommands]))

    for k in availableModules.keys():
        print("{}:".format(k))
        print("{}".format([i.name for i in availableModules[k]]))

    if len(c_args) < 1:
        embed = discord.Embed(title="Did someone asked for help? ( ͡° ͜ʖ ͡°)", description="Ok, here we go, here it is!", color=0x2cd147)
        embed.set_author(name=message.guild.name, icon_url = message.guild.icon_url if message.guild.icon_url != None else "https://cdn.discordapp.com/embed/avatars/1.png")
        embed.set_footer(text="Hope it was useful!", icon_url=message.author.avatar_url)
        for i in availableCommands:
            embed.add_field(name=i.name, value="Command **{}**\n{}\nUsage: {}".format(i.name, i.description, i.usage.replace("*prf*", config['prefix'])), inline=False)
        
        for i in availableModules:
            embed.add_field(name="Module {}".format(i), value="Available commands from there: {}.\nSee help for each using **{}help <command_you_need>**".format(ltos([j.name for j in availableModules[i]]), config['prefix']), inline=False)
        
        print("{}".format(embed.to_dict()))

    await message.channel.send(embed=embed)

    pass

help = commandtemplate.commandtemplate(
    name= 'help',
    description= 'desc',
    usage='*prf*help',
    parameters=None,
    aliases=None,
    is_callable=True,
    required_permissions=None,
    channels_blacklist=None,
    roles_blacklist=None,
    command=fn_help
)
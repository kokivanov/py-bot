import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils.commandtemplate import commandtemplate
import discord
import asyncio

async def fn_say(message, config, c_args, *args, **kwargs):
    pass

say = commandtemplate(name = "say", command=fn_say, aliases = ["say"])
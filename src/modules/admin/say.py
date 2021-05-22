import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils.commandtemplate import commandtemplate
from utils.abc import userRequestHandler as URH 
import discord
import asyncio

async def fn_say(message, params : URH, *args, **kwargs):
    pass

say = commandtemplate(name = "say", command=fn_say, aliases = ["say"], parameters={"Message" : True, "Repetition count" : False})
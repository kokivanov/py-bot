import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils.commandtemplate import commandtemplate
from utils.abc import userRequestHandler as URH 
import discord
import asyncio

async def fn_clear(message, params : URH, *args, **kwargs):
    pass

clear = commandtemplate(
    name= 'clear',
    description= 'desc',
    parameters=None,
    aliases=["clear"],
    is_callable=True,
    required_permissions=None,
    channels_blacklist=None,
    roles_blacklist=None,
    command=fn_clear
)
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils.commandtemplate import commandtemplate
import discord
import asyncio

async def fn_clear(message, config, c_args, *args, **kwargs):
    pass

clear = commandtemplate(
    name= 'clear',
    description= 'desc',
    usage='*prf*clear',
    parameters=None,
    aliases=None,
    is_callable=True,
    required_permissions=None,
    channels_blacklist=None,
    roles_blacklist=None,
    command=fn_clear
)
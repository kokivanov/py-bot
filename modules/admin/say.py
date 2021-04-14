import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils.commandtemplate import commandtemplate
import discord
import asyncio

async def fn_say(message, config, c_args, *args, **kwargs):
    pass

say = commandtemplate(
    name= 'say',
    description= 'desc',
    usage='*prf*say',
    parameters=None,
    aliases=None,
    is_callable=True,
    required_permissions=None,
    channels_blacklist=None,
    roles_blacklist=None,
    command=fn_say
)
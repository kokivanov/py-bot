import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils.commandtemplate import commandtemplate
import discord
import asyncio

async def fn_reddit(message, config, c_args, *args, **kwargs):
    pass

reddit = commandtemplate(
    name= 'reddit',
    description= 'desc',
    usage='*prf*reddit',
    parameters=None,
    aliases=["reddit"],
    is_callable=True,
    required_permissions=None,
    channels_blacklist=None,
    roles_blacklist=None,
    command=fn_reddit
)
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils.commandtemplate import commandtemplate
from utils.abc import userRequestHandler as URH 
import discord
import asyncio

async def fn_reddit(message, params : URH, *args, **kwargs):
    pass

reddit = commandtemplate(
    name= 'reddit',
    description= 'desc',
    parameters=None,
    aliases=["reddit"],
    is_callable=True,
    required_permissions=None,
    channels_blacklist=None,
    roles_blacklist=None,
    command=fn_reddit,
    custom_parameters={"nsfw_allowed" : False}
)
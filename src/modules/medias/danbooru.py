import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils.commandtemplate import commandtemplate
from utils.abc import userRequestHandler as URH 
import discord
import asyncio

async def fn_danbooru(message, params : URH, *args, **kwargs):
    pass

danbooru = commandtemplate(
    name= 'danbooru',
    description= 'desc',
    parameters=None,
    aliases=["danbooru", "dnbru"],
    is_callable=True,
    required_permissions=None,
    channels_blacklist=None,
    roles_blacklist=None,
    command=fn_danbooru,
    custom_parameters={"nsfw_allowed" : False}
)
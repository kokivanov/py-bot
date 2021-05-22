import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils.commandtemplate import commandtemplate
from utils.abc import userRequestHandler as URH 
import discord
import asyncio

async def fn_rule34(message, params : URH, *args, **kwargs):
    pass

rule34 = commandtemplate(
    name= 'rule34',
    description= 'desc',
    parameters=None,
    aliases=["rule34", "r34"],
    is_callable=True,
    required_permissions=None,
    channels_blacklist=None,
    roles_blacklist=None,
    command=fn_rule34,
    custom_parameters={"nsfw_allowed" : False}
)
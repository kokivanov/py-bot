import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils.commandtemplate import commandtemplate
import discord
import asyncio

async def fn_rule34(message, config, c_args, *args, **kwargs):
    pass

rule34 = commandtemplate(
    name= 'rule34',
    description= 'desc',
    usage='*prf*rule34',
    parameters=None,
    aliases=None,
    is_callable=True,
    required_permissions=None,
    channels_blacklist=None,
    roles_blacklist=None,
    command=fn_rule34
)
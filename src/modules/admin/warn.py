import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils.commandtemplate import commandtemplate
from utils.abc import userRequestHandler as URH 
import discord
import asyncio

async def fn_warn(message, params : URH, *args, **kwargs):
    pass

warn = commandtemplate(
    name= 'warn',
    description= 'Warns user, counts amount of warns and does defined action depending on amount of warns',
    parameters={"User ID or mention" : True, "Reason" : False},
    aliases=["warn"],
    is_callable=True,
    required_permissions=None,
    channels_blacklist=None,
    roles_blacklist=None,
    command=fn_warn
)
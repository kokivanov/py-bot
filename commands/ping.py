import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils.command import command
import discord


from datetime import datetime

def ping_fn(message):
    return datetime.timestamp(datetime.now()) - datetime.timestamp(message.created_at)

ping = command(
    description= "Returns bot's ping", 
    usage="*prf*ping", 
    parameters=None, 
    aliases=None, 
    is_callable=True, 
    required_permissions=None, 
    channels_blacklist=None,
    roles_blacklist=None,
    command=ping_fn
)
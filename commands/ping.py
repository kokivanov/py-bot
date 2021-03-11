import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils.command import command
import discord
from datetime import datetime

def ping_fn(message):
    return datetime.timestamp(datetime.now()) - datetime.timestamp(message.created_at)

ping = command(
    "Returns bot's ping", 
    "a-ping", 
    None, 
    None, 
    True, 
    None, 
    None, 
    None, 
    ping_fn
)

if __name__ == "__main__":

    print(ping.description)
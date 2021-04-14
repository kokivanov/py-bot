import discord
import asyncio
import commands
import modules


def handle(message, config):

    command = message.content.split(' ')[0][0 : len(config.prefix)]

    pass
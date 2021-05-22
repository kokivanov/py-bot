from io import TextIOWrapper
import asyncio
import re
from discord.message import Message
from discord.utils import sleep_until
from . import abc
from . import databasemanager
import discord

class cfg:

    db_manager : databasemanager.dbmanager

    async def get_prefix(self):
        self.prefix = (await self.db_manager.get_prefix(self.server_ID))["prefix"]
        if self.prefix == None: self.prefix = "a-"

        return self.prefix

    def __init__(self, message : discord.Message, dbConfig : TextIOWrapper or dict):
        self.db_manager = databasemanager.dbmanager(dbConfig)

        self.server_ID = message.guild.id
        self.owner_ID = message.guild.owner_id
        
    def getFullInfo(self, message : discord.Message) -> dict:
        pass


    # Will try to get parameters using __getCmdParams and __getModParams
    def getParameter(self, *args, **kwargs): ...

    # Will try to get parameters from database
    def __getCmdParams(self, *args, **kwargs): ...
    def __getModParams(self, *args, **kwargs): ...

    def update_parameter(self, *args, **kwargs): ...

    def __updateCmdParameter(self, *args, **kwargs): ...
    def __updateModParameter(self, *args, **kwargs): ...
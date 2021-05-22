import asyncio
from asyncio.base_events import Server
from utils import argumentparser
from utils.moduletemplate import moduletemplate

import modules
import json

from utils import commandmanager
from utils.databasemanager import dbmanager as db

cfg = json.load(open("/mnt/e/python/py-bot/src/settings.json"))

database = db(cfg["Database"])
print(asyncio.get_event_loop().run_until_complete(database.get_prefix("0")))

# print(database.get_Server_Config(server_ID="1", owner_ID=0))
# database.delete_row("feature_config", "1")
# database.delete_row("global_config", "1")

# print(commandmanager.COMMAND_LIST_FULL)

# print(json.loads(str({"a" : "b"}).replace("'", "\"")))
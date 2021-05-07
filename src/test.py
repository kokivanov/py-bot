from utils import argumentparser
from utils.moduletemplate import moduletemplate

import modules

from utils import commandmanager
from utils.databasemanager import dbmanager as db

databse = db(open("d:/python/py-bot/src/dbconfig.json"))

print(databse.get_Server_Config(0))

print(list(i for i in commandmanager.getList().keys()))

# print(commandmanager.getList())
# print(commandmanager.getListUnique())
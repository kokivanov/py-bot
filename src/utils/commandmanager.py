import discord
import asyncio
import commands
import modules
from utils.commandtemplate import commandtemplate
from utils.moduletemplate import moduletemplate

def handle(message, config): ...

def getList() -> dict:
    module_list = []
    command_list = []

    result = {}

    for mod in dir(modules):
        if not mod.startswith("__"):
            for ff in dir(getattr(modules, mod)):
                if not str(ff).startswith("__"):
                    tmp = getattr(getattr(modules, mod), ff)
                    if isinstance(tmp, moduletemplate): module_list.append(tmp)

    for cmd in dir(commands):
        if not cmd.startswith("__"):
            for ff in dir(getattr(commands, cmd)):
                if not str(ff).startswith("__"):
                    tmp = getattr(getattr(commands, cmd), ff)
                    if isinstance(tmp, commandtemplate): command_list.append(tmp)

    for i in module_list:
        for k, v in i.command_list.items():
            result["{}.{}".format(i.name, k)] = v

    for i in module_list:
        for k, v in i.command_list.items():
            try:
                for a in v.aliases:
                    result[a] = v
            except TypeError:
                continue
    
    for i in command_list:
        result[i.name] = i

    for i in command_list:
        try:
            for a in i.aliases:
                result[a] = v
        except TypeError:
            continue
    
    return result

def __generete_aliases__map(config): ...

def __unname(name : str) -> commandtemplate: ...
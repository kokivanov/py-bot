import discord
import asyncio
import commands
import modules
from utils.commandtemplate import commandtemplate
from utils.moduletemplate import moduletemplate

def handle(message, config): ...

def getList() -> dict:
    """
        Returns dictionary with:
            (cammand_name/alias, command_object)
    """

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
        for k in i.commands:
            result["{}.{}".format(i.name, k.name)] = k

    for i in module_list:
        for k in i.commands:
            try:
                for j in k.aliases:
                    result[j] = k
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

def getListUnique() -> list:
    """
        Returns list of all available commands
    """

    result = list()

    for mod in dir(modules):
        if not mod.startswith("__"):
            for ff in dir(getattr(modules, mod)):
                if not str(ff).startswith("__"):
                    tmp = getattr(getattr(modules, mod), ff)
                    if isinstance(tmp, moduletemplate):
                        for v in tmp.commands:
                            result.append(v)

    for cmd in dir(commands):
        if not cmd.startswith("__"):
            for ff in dir(getattr(commands, cmd)):
                if not str(ff).startswith("__"):
                    tmp = getattr(getattr(commands, cmd), ff)
                    if isinstance(tmp, commandtemplate): result.append(tmp)

    return result

def __generete_aliases__map(config, cmd): ...
"""
    Utilite: abc

    Description: 
        Provides basic types for working with data

"""

from typing import NewType

class commandConfig(object): ...

class userRequestHandler(object):
    """
        Class: UserRequestHandler

        Description:
            Returntype of parser that allows transfering data to command or work with it
    """
    
    def __init__(self, *args, **kwargs):
        i : int = 0

        try:
            self.command = kwargs['command']
        except KeyError:
            try:
                self.command = args[i]
                i+=1
            except IndexError:
                self.command = None
                self.args = None
                self.flags = None
                return

        try:
            self.args = kwargs['args']
        except KeyError:
            try:
                self.args = args[i]
                i+=1
            except IndexError:
                self.args = None

        try:
            self.flags = kwargs['flags']
        except KeyError:
            try:
                self.flags = args[i]
                i+=1
            except IndexError:
                self.flags = None

    def __eq__(self, item):
        if self.args == item.args and self.flags == item.flags and self.command == item.command:
            return True
        else:
            return False

    def __ne__(self, item):
        if self.args == item.args and self.flags == item.flags and self.command == item.command:
            return False
        else:
            return True

    def __str__(self):
        return "Command: {}\n Arguments: {}\n Flags: {}".format(self.command, self.args, self.flags)

class commandParameters(object):
    """
        Class: commandParameters
        
        Description:
            Holds all changable fields of class commandtemplate.commandtemplate for comfortable work with them
    """

    def __init__(self, aliases : list = [], is_callable : bool = True, required_permissions : list = [], channels_blacklist : list = [], roles_blacklist : list = [], custom_parameters : list = [],):
        self.aliases = aliases
        self.is_callable = is_callable
        self.required_permissions = required_permissions
        self.channels_blacklist = channels_blacklist
        self.roles_blacklist = roles_blacklist
        self.custom_parameters = custom_parameters

    def __eq__(self, item):
        if self.aliases == item.aliases and self.is_callable == item.is_callable and self.required_permissions == item.required_permissions and self.channels_blacklist == item.channels_blacklist and self.roles_blacklist == item.roles_blacklist and self.custom_parameters == item.custom_parameters:
            return True
        else:
            return False

    def __ne__(self, item):
        if self.aliases == item.aliases and self.is_callable == item.is_callable and self.required_permissions == item.required_permissions and self.channels_blacklist == item.channels_blacklist and self.roles_blacklist == item.roles_blacklist and self.custom_parameters == item.custom_parameters:
            return False
        else:
            return True

    def __invert__(self):
        self.is_callable = self.is_callable ^ True
        return self
"""
    Utility: abc

    Description: 
        Provides basic types for working with data

"""

from typing import NewType
from typing import List
import json
import dataclasses as ds

server_id = NewType("server_id", str)

@ds.dataclass(frozen=False, eq=True, order=True)
class watchedUser(object):
    ...


@ds.dataclass(frozen=False, eq=True, order=True)
class watchedMesage(object):
    ...


@ds.dataclass(frozen=False, eq=True, order=True)
class userRequestHandler(object):
    """
        Class: UserRequestHandler

        Description:
            Returntype of parser that allows transfering data to command or work with it
    """

    command: str = ds.field(default_factory=str)
    args: list = ds.field(default_factory=list)
    flags: dict = ds.field(default_factory=dict)


@ds.dataclass(frozen=False, eq=True, order=True)
class commandParameters(object):
    """
        Class: commandParameters

        Description:
            Holds all changable fields of class commandtemplate.commandtemplate for comfortable work with them

        Fields:
            aliases : list[str] -- Which words you can use to call this command. Be careful! Aliases must be unique for each command!
            is_callable : bool -- Is this command enabled on server. Can be changed using `admin.edit` command
            is_custom : bool -- Is this command can be affected by parent module, like changing fields to the same as parent's ones
            reqired_permissions : list[str] -- List of roles that user must have in order to use command. `%admin` and `%moderator` are keywords representing server owner (admin) and user with administrator rights.
            channels_blacklist: list[str] -- List of ids or names of channels where bot won't execute command.
            roles_blacklist: list[str] -- List of roles that aren't allowed to use commands. "@everyone" is also an option.
            custom_parameters: dict[str : any] -- Dictionary of custom parameters and default values that will be passed to command, can be edited with `admin.edit`
    """

    aliases: list = ds.field(default_factory=list)
    is_callable: bool = ds.field(default_factory=bool)
    is_custom: bool = ds.field(default=True)
    required_permissions: list = ds.field(default_factory=list)
    channels_blacklist: list = ds.field(default_factory=list)
    roles_blacklist: list = ds.field(default_factory=list)
    custom_parameters: dict = ds.field(default_factory=dict)

    @classmethod
    def copy(cls, initializer):
        try:
            return cls(aliases=initializer.aliases, is_callable=initializer.is_callable, required_permissions=initializer.required_permissions, channels_blacklist=initializer.channels_blacklist, roles_blacklist=initializer.roles_blacklist, custom_parameters=initializer.custom_parameters, is_custom=initializer.is_custom)
        except AttributeError:
            raise ValueError("Can't copy instance")

    def __invert__(self):
        self.is_callable ^= True
        return self.is_callable
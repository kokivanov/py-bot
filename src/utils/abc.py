"""
    Utilite: abc

    Description: 
        Provides basic types for working with data

"""

from typing import NewType
import json
import dataclasses as ds

server_id = NewType("server_id", str)


class watchedUser(object):
    ...


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
    args: list[str] = ds.field(default_factory=list)
    flags: dict[str, str] = ds.field(default_factory=dict)


@ds.dataclass(frozen=False, eq=True, order=True)
class commandParameters(object):
    """
        Class: commandParameters

        Description:
            Holds all changable fields of class commandtemplate.commandtemplate for comfortable work with them
    """

    aliases: list[str] = ds.field(default_factory=list)
    is_callable: bool = ds.field(default_factory=bool)
    is_custom: bool = ds.field(default_factory=bool)
    required_permissions: list[str] = ds.field(default_factory=list)
    channels_blacklist: list[str] = ds.field(default_factory=list)
    roles_blacklist: list[str] = ds.field(default_factory=list)
    custom_parameters: dict[str, bool] = ds.field(default_factory=dict)

    @classmethod
    def copy(cls, initializer):
        try:
            return cls(aliases=initializer.aliases, is_callable=initializer.is_callable, required_permissions=initializer.required_permissions, channels_blacklist=initializer.channels_blacklist, roles_blacklist=initializer.roles_blacklist, custom_parameters=initializer.custom_parameters, is_custom=initializer.is_custom)
        except AttributeError:
            raise ValueError("Can't copy instance")

    def __invert__(self):
        self.is_callable ^= True
        return self.is_callable

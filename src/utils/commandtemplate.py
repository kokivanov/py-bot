import asyncio
import json

from .abc import commandParameters
from .abc import userRequestHandler
import dataclasses as ds
import typing
import discord

@ds.dataclass
class commandtemplate(commandParameters):
    """
        Basic class of command, every instance of it is a command that can be called from discord

        Reqired argumets to initialize:
            name = str() # name of the command, can be called by it
            description = str()

    """

    name : str = ds.field(default_factory=str)
    description : str = ds.field(default_factory=str)
    are_flags_enabled : bool = ds.field(default_factory=bool)
    command : typing.Callable = ds.field(default_factory=typing.Callable[[discord.Message, userRequestHandler, ...], discord.Message])
    parameters : dict = ds.field(default=None)
    custom_parameters : dict = ds.field(default_factory=dict)
    usage : str = ds.field(default="", init=False)
    default_parameters : commandParameters = ds.field(default_factory=commandParameters, init=False)

    def __post_init__(cls):
        cls.usage = "*prf*{}".format(object.__getattribute__(cls, "name"))
        cls.default_parameters = commandParameters.copy(cls)
        
        try:
            for k, v in object.__getattribute__(cls, "parameters").items():
                if bool(v) == True:
                    cls.usage += ' [{}]'.format(str(k))
                elif bool(v) is False:
                    cls.usage += ' <{}>'.format(str(k))
        except AttributeError:
            cls.parameters = None

    async def __call__(self, message, config, *args, **kwargs):
        try:
            await self.command(message, config, parent=self, *args, **kwargs)
        except TypeError as e:
            print(e)

    # Returns command name and descriprion as string
    def __str__(self):
        return "Command {}, {}".format(self.name, self.description)

    # ======================================== Functions to manipulate permissions ============================================================
    def _set_permissions(self, *args, **kwargs):
        if len(args) < 1 or '' in args:
            raise ValueError("Can't append no parameters")
        for i in args:
            if not isinstance(i, str):
                raise InvalidParameter(command='{} : premission add'.format(
                    self.__class__.__name__), has_param=args, required_param=["any amount of str"], msg="Incorrect parameters")

        self.required_permissions = args

    def _add_permissions(self, *args, **kwargs):
        if len(args) < 1 or '' in args:
            raise ValueError("Can't append no parameters")
        for i in args:
            if isinstance(i, str):
                if i in self.required_permissions:
                    pass
                else:
                    self.required_permissions.append(i)
            else:
                raise InvalidParameter(command='{} : premission add'.format(
                    self.__class__.__name__), has_param=args, required_param=["any amount of str"], msg="Incorrect parameters")

    def _remove_permissions(self, *args, **kwargs):
        if len(args) < 1:
            raise ValueError("Can't remove void from list")
        for i in args:
            if isinstance(i, str):
                if i in self.required_permissions:
                    self.required_permissions.remove(i)
                else:
                    pass
            else:
                raise InvalidParameter(command='{} : premission remove'.format(
                    self.__class__.__name__), has_param=args, required_param=["any amount of str"], msg="Incorrect parameters")

    def _prune_permissions(self, *args, **kwargs):
        self.required_permissions.clear()

    # ======================================== Functions to manipulate aliases ============================================================
    def _set_aliases(self, *args, **kwargs):
        if len(args) < 1 or '' in args:
            raise ValueError("Can't append no parameters")
        for i in args:
            if not isinstance(i, str):
                raise InvalidParameter(command='{} : premission add'.format(
                    self.__class__.__name__), has_param=args, required_param=["any amount of str"], msg="Incorrect parameters")

        self.aliases = list(args)

    def _add_aliases(self, *args, **kwargs):
        if len(args) < 1 or '' in args:
            raise ValueError("Can't append no parameters")
        for i in args:
            if isinstance(i, str):
                if i in self.aliases:
                    pass
                else:
                    self.aliases.append(i)
            else:
                raise InvalidParameter(command='{} : aliases add'.format(
                    self.__class__.__name__), has_param=args, required_param=["any amount of str"], msg="Incorrect parameters")

    def _remove_aliases(self, *args, **kwargs):
        if len(args) < 1:
            raise ValueError("Can't remove void from list")
        for i in args:
            if isinstance(i, str):
                if i in self.aliases:
                    self.aliases.remove(i)
                else:
                    pass
            else:
                raise InvalidParameter(command='{} : aliases remove'.format(
                    self.__class__.__name__), has_param=args, required_param=["any amount of str"], msg="Incorrect parameters")

    def _prune_aliases(self, *args, **kwargs):
        self.aliases.clear()

    # ======================================== Functions to manipulate availability ============================================================
    def _set_availability(self, *args, **kwargs):
        if len(args) >= 1 and isinstance(args[0], bool):
            self.is_callable = args[0]

    def _change_availability(self):
        self.is_callable ^= True

    def __invert__(self):
        self.is_callable ^= True

    # ======================================== Functions to manipulate channel blacklist ============================================================
    def _set_channels_blacklist(self, *args, **kwargs):
        if len(args) < 1 or '' in args:
            raise ValueError("Can't append no parameters")
        for i in args:
            if not isinstance(i, str):
                raise InvalidParameter(command='{} : premission add'.format(
                    self.__class__.__name__), has_param=args, required_param=["any amount of str"], msg="Incorrect parameters")

        self.channels_blacklist = list(args)

    def _add_channels_blacklist(self, *args, **kwargs):
        if len(args) < 1 or '' in args:
            raise ValueError("Can't void parameter(s)")
        for i in args:
            if isinstance(i, str):
                if i in self.channels_blacklist:
                    pass
                else:
                    self.channels_blacklist.append(i)
            else:
                raise InvalidParameter(command='{} : channels_blacklist add'.format(
                    self.__class__.__name__), has_param=args, required_param=["any amount of str"], msg="Incorrect parameters")

    def _remove_channels_blacklist(self, *args, **kwargs):
        if len(args) < 1:
            raise ValueError("Can't remove void from list")
        for i in args:
            if isinstance(i, str):
                if i in self.channels_blacklist:
                    self.channels_blacklist.remove(i)
                else:
                    pass
            else:
                raise InvalidParameter(command='{} : channels_blacklist remove'.format(
                    self.__class__.__name__), has_param=args, required_param=["any amount of str"], msg="Incorrect parameters")

    def _prune_channels_blacklist(self, *args, **kwargs):
        self.channels_blacklist.clear()

    # ======================================== Functions to manipulate roles blacklist ============================================================
    def _set_roles_blacklist(self, *args, **kwargs):
        if len(args) < 1 or '' in args:
            raise ValueError("Can't append no parameters")
        for i in args:
            if not isinstance(i, str):
                raise InvalidParameter(command='{} : premission add'.format(
                    self.__class__.__name__), has_param=args, required_param=["any amount of str"], msg="Incorrect parameters")

        self.roles_blacklist = list(args)

    def _add_roles_blacklist(self, *args, **kwargs):
        if len(args) < 1 or '' in args:
            raise ValueError("Can't append no parameters")
        for i in args:
            if isinstance(i, str):
                if i in self.roles_blacklist:
                    pass
                else:
                    self.roles_blacklist.append(i)
            else:
                raise InvalidParameter(command='{} : roles_blacklist add'.format(
                    self.__class__.__name__), has_param=args, required_param=["any amount of str"], msg="Incorrect parameters")

    def _remove_roles_blacklist(self, *args, **kwargs):
        if len(args) < 1:
            raise ValueError("Can't remove void from list")
        for i in args:
            if isinstance(i, str):
                if i in self.roles_blacklist:
                    self.roles_blacklist.remove(i)
                else:
                    pass
            else:
                raise InvalidParameter(command='{} : roles_blacklist remove'.format(
                    self.__class__.__name__), has_param=args, required_param=["any amount of str"], msg="Incorrect parameters")

    def _prune_roles_blacklist(self, *args, **kwargs):
        self.roles_blacklist.clear()


    # =========================================== Import parameters fields class abc.commandParameters =================================

    def __lshift__(self, item: commandParameters):
        """
            Allows to import parameters from a commandParameters class
        """
        try:
            self.aliases = item.aliases
            self.is_callable = item.is_callable
            self.required_permissions = item.required_permissions
            self.channels_blacklist = item.channels_blacklist
            self.roles_blacklist = item.roles_blacklist
            self.custom_parameters = item.custom_parameters
        except AttributeError as e:
            self.aliases = []
            self.is_callable = True
            self.required_permissions = []
            self.channels_blacklist = []
            self.roles_blacklist = []
            self.custom_parameters = {}
            raise ValueError("Asigning incorrect type, misssing {}".format(e))

    # def __eq__(self, item: commandParameters):
    #     try:
    #         self.aliases = item.aliases
    #         self.is_callable = item.is_callable
    #         self.required_permissions = item.required_permissions
    #         self.channels_blacklist = item.channels_blacklist
    #         self.roles_blacklist = item.roles_blacklist
    #         self.custom_parameters = item.custom_parameters
    #     except AttributeError as e:
    #         self.aliases = []
    #         self.is_callable = True
    #         self.required_permissions = []
    #         self.channels_blacklist = []
    #         self.roles_blacklist = []
    #         self.custom_parameters = {}
    #         raise ValueError("Asigning incorrect type, misssing {}".format(e))

    # updates command if it is related to module 
    def update_r(values : commandParameters) -> None:
        """
            Used in moduletemplate to update related commands, works only if command isn't custom 
        """
        if self.is_custom: return

        try:
            if values.aliases != None:
                self.aliases = values.aliases
        except AttributeError as e:
            raise ValueError("Invalid parameter given: {}".format(e))

        try:
            if values.is_callable != None:
                self.is_callable = values.is_callable
        except AttributeError as e:
            raise ValueError("Invalid parameter given: {}".format(e))

        try:
            if values.required_permissions != None:
                self.required_permissions = values.required_permissions
        except AttributeError as e:
            raise ValueError("Invalid parameter given: {}".format(e))

        try:
            if values.channels_blacklist != None:
                self.channels_blacklist = values.channels_blacklist
        except AttributeError as e:
            raise ValueError("Invalid parameter given: {}".format(e))

        try:
            if values.roles_blacklist != None:
                self.roles_blacklist = values.roles_blacklist
        except AttributeError as e:
            raise ValueError("Invalid parameter given: {}".format(e))
        
        try:
            if values.custom_parameters != None:
                self.custom_parameters = values.custom_parameters
        except AttributeError as e:
            raise ValueError("Invalid parameter given: {}".format(e))

    def update(self, values=commandParameters):...
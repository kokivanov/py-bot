import asyncio
import json

from .exceptions import *
from .abc import commandParameters
from .abc import userRequestHandler
import dataclasses as ds
import typing
import discord

@ds.dataclass
class commandtemplate(commandParameters):
    """
        Basic class of command, every instance of it is a command that can be called from discord

        Reqired arguments to initialize:
            name : str -- Name of the command, can be called by it.
            command : Callable -- Function that will be executed on command use

        Additional fields:
            description : str -- Description of your command.
            are_flags_enabled : bool -- Flags for command that will be used to provide some more settings for command.
            flags : dict[str : bool] -- List of available flags for this command with property of necessary (True if necessary).
            custom_parameters: dict[str : any] -- Dictionary of custom parameters and default values that will be passed to command, can be edited with `admin.edit`
            parameters : dict[str : bool] -- List of parameters that can be passed to command (True if necessary).

        Common parameters:
            aliases : list[str] -- Which words you can use to call this command. Be careful! Aliases must be unique for each command!
            is_callable : bool -- Is this command enabled on server. Can be changed using `admin.edit` command
            is_custom : bool -- Is this command can be affected by parent module, like changing fields to the same as parent's ones
            reqired_permissions : list[str] -- List of roles that user must have in order to use command. `%admin` and `%moderator` are keywords representing server owner (admin) and user with administrator rights.
            channels_blacklist: list[str] -- List of ids or names of channels where bot won't execute command.
            roles_blacklist: list[str] -- List of roles that aren't allowed to use commands. "@everyone" is also an option. \n\tcustom_parameters: dict[str : any] -- Dictionary of custom parameters and default values that will be passed to command, can be edited with `admin.edit`

    """

    name : str = ds.field(default_factory=str)
    description : str = ds.field(default_factory=str)
    are_flags_enabled : bool = ds.field(default_factory=bool)
    flags : dict = ds.field(default_factory=dict)
    command : typing.Callable = ds.field(default_factory=typing.Callable[[discord.Message, userRequestHandler, typing.Any], discord.Message])
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

    # Returns command name and description as string
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
        if ("%admin" in args):
            raise DangerError(msg="You are about to delete standart rights for this command. Unfortunately you aren't allowed to do this otherwise you may not be able to modify this commnad anymore.")

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
        for i in self.required_permissions:
            if i != "%admin": self.required_permissions.remove(i)

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
            raise ValueError("Assigning incorrect type, misssing {}".format(e))

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
    #         raise ValueError("Assigning incorrect type, misssing {}".format(e))

    # updates command if it is related to module 
    def update_r(self, values : commandParameters) -> None:
        """
            Used in moduletemplate to update related commands, works only if command isn't custom 
        """
        if self.is_custom: return

        try:
            if values.aliases != None:
                self.aliases += values.aliases
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
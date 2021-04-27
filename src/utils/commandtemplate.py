import asyncio
import json
from .abc import commandParameters

class commandtemplate(commandParameters):
    """
        Basic class of command, every instance of it is a command that can be called from discord

        Reqired argumets to initialize:
            name = str() # name of the command, can be called by it
            description = str()

    """

    def __init__(self, command, name : str, description : str = "Command that can do something, no description provided", are_flags_enabled : bool = False, parameters : dict = {}, aliases : list = [], is_callable : bool = True, required_permissions : list = [], channels_blacklist : list = [], roles_blacklist : list = [], is_custom = True, custom_parameters : dict = {}, *args, **kwargs):
        self.name = name
        self.description = description
        self.are_flags_enabled = are_flags_enabled
        self.command = command
        self.parameters = parameters
        self.aliases = aliases
        self.is_callable = is_callable
        self.required_permissions = required_permissions
        self.channels_blacklist = channels_blacklist
        self.roles_blacklist = roles_blacklist
        self.is_custom = is_custom

        self.custom_parameters = custom_parameters

        self.usage = "*prf*{}".format(self.name)

        try:
            for k, v in self.parameters.items():
                if bool(v) == True:
                    self.usage += ' [{}]'.format(str(k))
                elif bool(v) is False:
                    self.usage += ' <{}>'.format(str(k))
        except AttributeError:
            self.parameters = None

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

    def _change_availability(self, *args, **kwargs):
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
        try:
            self.aliases = item.aliases
            self.is_callable = item.is_callable
            self.required_permissions = item.required_permissions
            self.channels_blacklist = item.channels_blacklist
            self.roles_blacklist = item.roles_blacklist
        except AttributeError as e:
            self.aliases = []
            self.is_callable = True
            self.required_permissions = []
            self.channels_blacklist = []
            self.roles_blacklist = []
            raise ValueError("Asigning incorrect type, misssing {}".format(e))

    def __eq__(self, item: commandParameters):
        try:
            self.aliases = item.aliases
            self.is_callable = item.is_callable
            self.required_permissions = item.required_permissions
            self.channels_blacklist = item.channels_blacklist
            self.roles_blacklist = item.roles_blacklist
        except AttributeError as e:
            self.aliases = []
            self.is_callable = True
            self.required_permissions = []
            self.channels_blacklist = []
            self.roles_blacklist = []
            raise ValueError("Asigning incorrect type, misssing {}".format(e))

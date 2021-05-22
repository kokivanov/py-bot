from .abc import commandParameters
from .exceptions import *
from .abc import userRequestHandler
from .commandtemplate import commandtemplate
from collections.abc import Callable
import typing
import json
import discord
import dataclasses as dc

@dc.dataclass
class moduletemplate(commandParameters):
    """
        Class that is each bot's module inhibited from

        Requires to initialize:
            name : str -- name of the module
            commands : commandtemplate -- list of imported commands that inhibited from commandtemplate

            Isn't necessary but would be good to provide description

            You can also specify what will happen when module is called directly by setting `on_call` parameter with your function

        Other parameters:
            description : str -- Description of your module.
            on_call : Callable -- Function that will be called in case using module name as command.
            are_flags_enabled : bool -- Flags for command that will be used to provide some more settings for command.
            flags : dict[str : bool] -- List of available flags for this command with property of necessary (True if necessary).
            custom_parameters: dict[str : any] -- Dictionary of custom parameters and default values that will be passed to command, can be edited with `admin.edit`
            parameters : dict[str : bool] -- List of parameters that can be passed to command (True if necessary).

        Common fields:
            aliases : list[str] -- Which words you can use to call this command. Be careful! Aliases must be unique for each command!
            is_callable : bool -- Is this command enabled on server. Can be changed using `admin.edit` command
            is_custom : bool -- Is this command can be affected by parent module, like changing fields to the same as parent's ones
            reqired_permissions : list[str] -- List of roles that user must have in order to use command. `%admin` and `%moderator` are keywords representing server owner (admin) and user with administrator rights.
            channels_blacklist: list[str] -- List of ids or names of channels where bot won't execute command.
            roles_blacklist: list[str] -- List of roles that aren't allowed to use commands. "@everyone" is also an option.
        
        Example:
            admin=moduletemplate(
            commands = [clear.clear, say.say],
            name= 'admin',
            description= 'Provides administrative utilities',
            required_permissions=["%admin", "%moderator"],
            channels_blacklist=None,
            roles_blacklist=None,
            command=None)
        
        Where `clear.clear` and `say.say` are functions
    """

    name : str = dc.field(default_factory=str)
    description : str = dc.field(default_factory=str)
    on_call : typing.Callable[[discord.Message, userRequestHandler, typing.Any], discord.Message] = dc.field(default=None)
    commands : list = dc.field(default_factory=list)
    __is_self_noncallable : bool = dc.field(default=False, init=False)
    are_flags_enabled : bool = dc.field(default_factory=bool)
    flags : dict = dc.field(default_factory=dict)

    parameters : dict = dc.field(default=None)
    usage : str = dc.field(default="", init=False)
    default_parameters : commandParameters = dc.field(default_factory=commandParameters, init=False)

    # Changes parameters of all related commands to modules default
    

    # Changes parameters of all related commands
    def changeRelated(self):
        self_params = commandParameters(aliases=None, is_callable=None, required_permissions=self.required_permissions, channels_blacklist=self.channels_blacklist, roles_blacklist=self.roles_blacklist, custom_parameters=None)
        
        for i in self.commands:
            i.update_r(values=self_params)

    def __post_init__(self):
        self.usage = "*prf*{}".format(object.__getattribute__(self, "name"))
        self.default_parameters = commandParameters.copy(self)

        self.__is_self_noncallable = self.on_call == None
        
        for i in self.commands:
            i.name = self.name + '.' + i.name

        self.changeRelated()

    # Updates settings and sends them to databasemanager
    def update(): ...

    # Returns module config as json string
    def __invert__(self):
        params = json.dumps({
            "name": self.name,
            "description": self.description,
            "required_permissions": self.required_permissions,
            "channels_blacklist": self.channels_blacklist,
            "roles_blacklist": self.roles_blacklist
        })

        return params

    # Returns module name and description as string
    def __str__(self):
        return "Module {}, {}".format(self.name, self.description)

    def __call__(self, *args, **kwargs):
        try:
            return self.on_call(self, *args, **kwargs)
        except AttributeError:
            raise ValueError("You can't call this module")

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
            raise DangerError(msg="You are about to delete standart rights for this command. Unfortunately you aren't allowed to do this otherwise you may not be able to modify this module anymore.")

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

    
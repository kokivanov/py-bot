from .abc import commandParameters
from .abc import userRequestHandler
from .commandtemplate import commandtemplate
from collections.abc import Callable
import typing
import discord
import dataclasses as dc

@dc.dataclass
class moduletemplate(commandParameters):
    """
        Class that is each bot's module inhibited from

        Requires to initialize:
            name : str -- name of the module
            commands : commandtemplate -- list of imported cammands that inhibited from commandtemplate

            Isn't necessary but would be good to provite description

            You can also specify what will happen whel module is called directly by setting `on_call` parameter with your function

        Example:
            admin=moduletemplate(
            commands = [clear.clear, say.say],
            name= 'admin',
            description= 'Provides administrative utilites',
            required_permissions=["%admin", "%moderator"],
            channels_blacklist=None,
            roles_blacklist=None,
            command=None)
        
        Where `clear.clear` and `say.say` are functions
    """

    name : str = dc.field(default_factory=str)
    description : str = dc.field(default_factory=str)
    on_call : typing.Callable[[discord.Message, userRequestHandler, ...], discord.Message] = dc.field(default=None)
    commands : list[typing.Callable[[discord.Message, userRequestHandler, ...], discord.Message]] = dc.field(default_factory=list)

    # Changes parameters of all related commands to modules default
    

    # Changes parameters of all related commands
    def changeRelated():
        self_params = commandParameters(aliases=None, is_callable=None, required_permissions=self.required_permissions, channels_blacklist=self.channels_blacklist, roles_blacklist=self.roles_blacklist, custom_parameters=None)
        
        for i in commands:
            i.update_r(values=self_params)

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

    # Returns module name and descriprion as string
    def __str__(self):
        return "Module {}, {}".format(self.name, self.description)

    def __call__(self):
        try:
            return self.on_call()
        except AttributeError:
            raise ValueError("Can't call unexisting function")

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

    
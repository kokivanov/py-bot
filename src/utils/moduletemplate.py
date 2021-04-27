from .commandtemplate import commandtemplate
from .abc import commandParameters

class moduletemplate(object):
    """
        Class that is each bot's module inhibited from

        Reuires to initialize:
            name : str # name of the module
            commands : commandParameters # list of imported cammands that inhibited from commandtemplate
    """

    def __init__(self,name, commands : list[commandtemplate], roles_blacklist : list = [], channels_blacklist : list = [], description="Module tah holds some commands and shares parameters with them", required_permissions : list = [], *args, **kwargs):
        self.name = name
        self.roles_blacklist = roles_blacklist
        self.channels_blacklist = channels_blacklist
        self.description = description
        self.required_permissions = required_permissions

        self.command_list = {}

        try:
            for i in commands:
                if not isinstance(i, commandtemplate): raise TypeError("{} is not a command instance".format(str(i.__class__.__name__)))
                else: 
                    self.command_list[i.name] = i
        except TypeError as e:
            print("Invalid parameters provided: {}".format(e))

        super().__init__()

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
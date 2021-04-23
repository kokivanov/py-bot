from . import commandtemplate
from types import ModuleType

class moduletemplate():
    name = str()
    description = str()
    required_permissions = list()
    channels_blacklist = list()
    roles_blacklist = list()

    commands = dict()

    def __init__(self, *args, **kwargs):
        try:
            
            try:
                self.name = str(kwargs.get('name'))
            except KeyError as e:
                print ("Missing {} key\n".format(e))

            try:
                self.description = str(kwargs.get('description'))
            except KeyError as e:
                print ("Missing {} key\n".format(e))

            try:
                self.required_permissions = (kwargs.get('required_permissions'))
            except KeyError as e:
                print ("Missing {} key\n".format(e))

            try:
                self.channels_blacklist = (kwargs.get('channels_blacklist'))
            except KeyError as e:
                print ("Missing {} key\n".format(e))

            try:
                self.roles_blacklist = (kwargs.get('roles_blacklist'))
            except KeyError as e:
                print ("Missing {} key\n".format(e))

            for i in kwargs.get('commands'):
                if not isinstance(i, ModuleType): raise TypeError("{} is not a module".format(str(i.__name__)))
                else: 
                    name = str(i.__name__).split(".")[-1]
                    self.commands[name] = getattr(i, name)

        except TypeError as e:
            print("Invalid parameters provided: {}".format(e))

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
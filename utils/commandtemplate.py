import asyncio
import json

class commandtemplate(object):
    name = ''
    description = ''
    usage = ''
    parameters = {}
    aliases = []
    is_callable = True
    required_permissions = []
    channels_blacklist = []
    roles_blacklist = []

    command = None

    def __init__(self, *args, **kwargs):
        try:
            if not isinstance(kwargs.get('name'), str):
                raise TypeError('Required type str as a name')
            if not isinstance(kwargs.get('description'), str):
                raise TypeError('Required type str as a description')
            if not isinstance(kwargs.get("usage"), str):
                raise TypeError('Required type str as a usage')
            if not isinstance(kwargs.get("parameters"), dict) and kwargs.get("parameters") != None:
                raise TypeError('Required type dict as a parameters')
            if not isinstance(kwargs.get("aliases"), list) and kwargs.get("aliases") != None:
                raise TypeError('Required type list as a aliases')
            if not isinstance(kwargs.get("is_callable"), bool):
                raise TypeError('Required type bool as a is_callable')
            if not isinstance(kwargs.get("required_permissions"), list) and kwargs.get('required_permissions') != None:
                raise TypeError('Required type list as a required_permissions')
            if not isinstance(kwargs.get("channels_blacklist"), list) and kwargs.get('channels_blacklist') != None:
                raise TypeError('Required type list as a channels_blacklist')
            if not isinstance(kwargs.get("roles_blacklist"), list) and kwargs.get('roles_blacklist') != None:
                raise TypeError('Required type list as a roles_blacklist')

            self.name = kwargs.get('name')
            self.description = kwargs.get('description')
            self.usage = kwargs.get("usage")
            self.parameters = kwargs.get('parameters')
            self.aliases = kwargs.get('aliases')
            self.is_callable = kwargs.get('is_callable')
            self.required_permissions = kwargs.get('required_permissions')
            self.channels_blacklist = kwargs.get('channels_blacklist')
            self.roles_blacklist = kwargs.get('roles_blacklist')
            self.command = kwargs.get('command')

            if self.parameters != None and isinstance(self.parameters, dict):
                for k, v in self.parameters.items():
                    if not isinstance(v, bool):
                        raise TypeError('Required bool as value')
                    if not isinstance(k, str):
                        raise TypeError('Required str as key')

                    if v == True:
                        self.usage += ' [{}]'.format(k)
                    elif v is False:
                        self.usage += ' <{}>'.format(k)

        except KeyError:
            print("Can't recognize some parameters.")
        except TypeError as e:
            print("Invalid parameters provided: {}".format(e))

    async def __call__(self, message, config, c_args, *args, **kwargs):
        await self.command(message, config, c_args, *args, **kwargs)

    # Returns command config as json string
    def __invert__(self):
        params = json.dumps({
            "name": self.name,
            "description": self.description,
            "usage": self.usage,
            "parameters": self.parameters,
            "aliases": self.aliases,
            "is_callable": self.is_callable,
            "required_permissions": self.required_permissions,
            "channels_blacklist": self.channels_blacklist,
            "roles_blacklist": self.roles_blacklist
        })

        return params

    # Gets command parameters as json string
    def __lshift__(self, p):
        par = json.loads(p)
        try:
            self.name = par['name']
            self.description = par['description']
            self.usage = par['usage']
            self.parameters = par['parameters']
            self.aliases = par['aliases']
            self.is_callable = par['is_callable']
            self.required_permissions = par['required_permissions']
            self.channels_blacklist = par['channels_blacklist']
            self.roles_blacklist = par['roles_blacklist']
        except KeyError:
            raise ValueError("Invalid or corrupted config string")

    # Gets command parameters as json string
    def load_parameters(self, p):
        par = json.loads(p)
        try:
            self.name = par['name']
            self.description = par['description']
            self.usage = par['usage']
            self.parameters = par['parameters']
            self.aliases = par['aliases']
            self.is_callable = par['is_callable']
            self.required_permissions = par['required_permissions']
            self.channels_blacklist = par['channels_blacklist']
            self.roles_blacklist = par['roles_blacklist']
        except KeyError:
            raise ValueError("Invalid or corrupted config string")

    # Returns command parameters as json string
    def get_parameters(self):
        params = json.dumps({
            "name": self.name,
            "description": self.description,
            "usage": self.usage,
            "parameters": self.parameters,
            "aliases": self.aliases,
            "is_callable": self.is_callable,
            "required_permissions": self.required_permissions,
            "channels_blacklist": self.channels_blacklist,
            "roles_blacklist": self.roles_blacklist
        })

        return params

    # Returns command name and descriprion as string
    def __str__(self):
        return "Command {}, {}".format(self.name, self.description)

    # ======================================== Functions to manipulate permissions ============================================================
    def set_permissions(self, *args, **kwargs):
        if len(args) < 1 or '' in args:
            raise ValueError("Can't append no parameters")
        for i in args:
            if not isinstance(i, str):
                raise InvalidParameter(command='{} : premission add'.format(
                    self.__class__.__name__), has_param=args, required_param=["any amount of str"], msg="Incorrect parameters")

        self.required_permissions = args


    def add_permissions(self, *args, **kwargs):
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

    def remove_permissions(self, *args, **kwargs):
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

    def prune_permissions(self, *args, **kwargs):
        self.required_permissions.clear()

    # ======================================== Functions to manipulate aliases ============================================================
    def set_aliases(self, *args, **kwargs):
        if len(args) < 1 or '' in args:
            raise ValueError("Can't append no parameters")
        for i in args:
            if not isinstance(i, str):
                raise InvalidParameter(command='{} : premission add'.format(
                    self.__class__.__name__), has_param=args, required_param=["any amount of str"], msg="Incorrect parameters")

        self.aliases = list(args)

    def add_aliases(self, *args, **kwargs):
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

    def remove_aliases(self, *args, **kwargs):
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

    def prune_aliases(self, *args, **kwargs):
        self.aliases.clear()

    # ======================================== Functions to manipulate availability ============================================================
    def set_availability(self, *args, **kwargs):
        if len(args) >= 1 and isinstance(args[0], bool):
            self.is_callable = args[0]

    def change_availability(self, *args, **kwargs):
        self.is_callable ^= True

    # ======================================== Functions to manipulate channel blacklist ============================================================
    def set_channels_blacklist(self, *args, **kwargs):
        if len(args) < 1 or '' in args:
            raise ValueError("Can't append no parameters")
        for i in args:
            if not isinstance(i, str):
                raise InvalidParameter(command='{} : premission add'.format(
                    self.__class__.__name__), has_param=args, required_param=["any amount of str"], msg="Incorrect parameters")

        self.channels_blacklist = list(args)

    def add_channels_blacklist(self, *args, **kwargs):
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

    def remove_channels_blacklist(self, *args, **kwargs):
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

    def prune_channels_blacklist(self, *args, **kwargs):
        self.channels_blacklist.clear()

    # ======================================== Functions to manipulate roles blacklist ============================================================
    def set_roles_blacklist(self, *args, **kwargs):
        if len(args) < 1 or '' in args:
            raise ValueError("Can't append no parameters")
        for i in args:
            if not isinstance(i, str):
                raise InvalidParameter(command='{} : premission add'.format(
                    self.__class__.__name__), has_param=args, required_param=["any amount of str"], msg="Incorrect parameters")

        self.roles_blacklist = list(args)

    def add_roles_blacklist(self, *args, **kwargs):
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

    def remove_roles_blacklist(self, *args, **kwargs):
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

    def prune_roles_blacklist(self, *args, **kwargs):
        self.roles_blacklist.clear()
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
        # set parameters
            try:
                self.name = str(kwargs.get('name'))
            except KeyError as e:
                print ("Missing {} key\n".format(e))
                return

            try:
                self.description = str(kwargs.get('description'))
            except KeyError as e:
                print ("Missing {} key\n".format(e))
                return

            try:
                self.usage = str(kwargs.get("usage"))
            except KeyError as e:
                print ("Missing {} key\n".format(e))
                return

            try:
                self.parameters = (kwargs.get('parameters'))
            except KeyError as e:
                print ("Missing {} key\n".format(e))
                self.parameters = None

            try:
                self.aliases = (kwargs.get('aliases'))
            except KeyError as e:
                print ("Missing {} key\n".format(e))
                self.aliases = None

            try:
                self.is_callable = (kwargs.get('is_callable'))
            except KeyError as e:
                print ("Missing {} key\n".format(e))
                return

            try:
                self.required_permissions = (kwargs.get('required_permissions'))
            except KeyError as e:
                print ("Missing {} key\n".format(e))
                self.required_permissions = None

            try:
                self.channels_blacklist = (kwargs.get('channels_blacklist'))
            except KeyError as e:
                print ("Missing {} key\n".format(e))
                self.channels_blacklist = None

            try:
                self.roles_blacklist = (kwargs.get('roles_blacklist'))
            except KeyError as e:
                print ("Missing {} key\n".format(e))
                self.roles_blacklist = None

            try:
                self.command = kwargs.get('command')
            except KeyError as e:
                print ("Missing {} key\n".format(e))
                return
        
        except TypeError as e:
            print (e)

        try:
            for k, v in self.parameters.items():
                if bool(v) == True:
                    self.usage += ' [{}]'.format(str(k))
                elif bool(v) is False:
                    self.usage += ' <{}>'.format(str(k))
        except TypeError as e:
            print (e)

    async def __call__(self, message, config, c_args, *args, **kwargs):
        try:
            await self.command(message, config, c_args, *args, **kwargs)
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
from utils.parameter import parameter

class command(object):
    name : str

    usage : str

    description : str

    parameters : dict

    aliases : [str]

    is_callable : bool

    required_permissions : [str]

    channels_blacklist : [str]

    roles_blacklist : [str]

    command : None

    def __init__(self,
            description : str,
            usage : str,
            parameters : dict,
            aliases : [str],
            is_callable : bool,
            required_permissions : [str],
            channels_blacklist : [str],
            roles_blacklist : [str],
            command
        ):

        self.usage = usage
        self.description = description
        self.parameters = parameters
        self.aliases = aliases
        self.is_callable = is_callable
        self.required_permissions = required_permissions
        self.channels_blacklist = channels_blacklist
        self.roles_blacklist = roles_blacklist
        self.command = command
    
    def __str__(self):
        return "Command {0.name}:\n {0.description}".format(self)

    def __call__(self, *args, **kwargs):
        return self.command(*args, **kwargs)

    # def set_permission(self, *args, **kwargs)
    # def set_aliases(self, *args, **kwargs)
    # def set_availability(self, *args, **kwargs)
    # def set_channel_blacklist(self, *args, **kwargs)
    # def set_role_blacklist(self, *args, **kwargs)

    # def __invert__(self): # returns all function parameters as dict
    # def __getitem__(self, *args, **kwargs) # sets all function parameters from dict
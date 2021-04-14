from commandtemplate import commandtemplate

class moduletemplate():
    name = ''
    description = ''
    usage = ''
    parameters = {}
    aliases = []
    is_callable = True
    required_permissions = []
    channels_blacklist = []
    roles_blacklist = []

    commands = None
    custom = dict()

    def __init__(self, *args, **kwargs): ...
    def setProperties(self, *args, **kwargs): ...
    
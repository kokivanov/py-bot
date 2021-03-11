from utils.parameter import parameter

class command(object):
    usage : str

    description : str

    parameters : { str : parameter }

    aliases : [str]

    is_callable : bool

    permissions : [str]

    channels_blacklist : [str]

    roles_blacklist : [str]
import datetime

class ErrorTemplate(object):
    errorTime = None
    errorHash = None
    command = None

    def __init__(self, *args, **kwargs):
        self.errorTime = datetime.now()
        self.errorHash = hash(errorTime)
        try:
            self.command = kwargs.get('command')
        except:
            pass
        super().__init__(*args, **kwargs)

    def __str__(self):
        return "{} error, at {}\n Hash : {}\n".format(self.__class__.__name__, self.errorTime, self.errorHash)

class ArgumentErr(object, ErrorTemplate):
    required_args = []
    has_args = []

    def __init__(self, *args, **kwargs):
        self.required_args = kwargs['required_args']
        self.has_args = kwargs['has_args']

    pass

class ConnectionErr(object, ErrorTemplate):
    pass

class PermissionErr(object, ErrorTemplate):
    reqired_permissions = []
    has_permission = []

    def __init__(self, *args, **kwargs):
        self.required_premissions = kwargs['required_premissions']
        self.required_premissions = kwargs['has_premissions']

    def __str__(self):
        return "{}Reqired permissions: {}\nHas permissions: {}\n".format(super().__str__(), self.required_premissions, self.has_permission)

    pass

class InvalidConfig(object, ErrorTemplate):
    pass

class InvalidParameter(object, ErrorTemplate):
    pass
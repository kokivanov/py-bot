import datetime


class ErrorTemplate(object):
    errorTime = None
    errorHash = None
    command = None

    def __init__(self, *args, **kwargs):
        self.errorTime = datetime.now()
        self.errorHash = hash(self)
        self.command = kwargs.get('command')
        super().__init__(*args, **kwargs)

class ArgumentError(object, ErrorTemplate):
    pass

class ConnectionError(object, ErrorTemplate):
    pass

class PermissionError(object, ErrorTemplate):
    reqired_permissions = []

    def __init__(self, *args, **kwargs):
        self.required_premissions = kwargs['premissions']

    pass


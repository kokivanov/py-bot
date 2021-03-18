import datetime

class ErrorTemplate(Exception):
    errorTime = None
    errorHash = None
    command = None

    def __init__(self, *args, **kwargs):
        self.errorTime = datetime.datetime.now()
        self.errorHash = hash(self.errorTime)
        try:
            self.command = kwargs.get('command')
            super().__init__(kwargs.get("msg"))
        except KeyError:
            raise Exception("Must specify a message")
            pass

    def __str__(self):
        return "{} error, at {}\n Hash : {}\n".format(self.__class__.__name__, self.errorTime, self.errorHash)

class ArgumentErr(ErrorTemplate):
    required_args = []
    has_args = []

    def __init__(self, *args, **kwargs):
        self.required_args = kwargs['required_args']
        self.has_args = kwargs['has_args']
        super().__init__(*args, **kwargs)

    pass

class ConnectionErr(ErrorTemplate):
    pass

class PermissionErr(ErrorTemplate):
    reqired_permissions = []
    has_permission = []

    def __init__(self, *args, **kwargs):
        self.required_premissions = kwargs['required_premissions']
        self.required_premissions = kwargs['has_premissions']

        super().__init__(*args, **kwargs)

    def __str__(self):
        return "{}Reqired permissions: {}\nHas permissions: {}\n".format(super().__str__(), self.required_premissions, self.has_permission)

    pass

class InvalidConfig(ErrorTemplate):
    pass

class InvalidParameter(ErrorTemplate):
    required_param = []
    has_param = []

    def __str__(self):
        return "{}\nRequired: {}\n got: {}\n".format(super().__str__(), self.required_param, self.has_param)

    def __init__(self, *args, **kwargs):
        try:
            self.required_param = kwargs.get('required_param')
            self.has_param = kwargs.get('has_param')

        except KeyError as ex:
            print("Invalid parameters: {}\n".format(ex.__cause__)) 

        super().__init__(*args, **kwargs)

    pass
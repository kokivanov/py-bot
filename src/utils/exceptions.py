import datetime


def form(src : str, index : int):
    result = ''
    
    try:
        for i in range(0, len(src)):
            if i == index: result += '^'
            else: result += ' '
    except Exception as e:
        result = ""
    finally:
        return result

print(form(src="abcdef", index=3))

class ErrorTemplate(Exception):
    def __init__(self, *args, **kwargs):
        self.errorTime = datetime.datetime.now()
        self.errorHash = hash(self.errorTime)

        try:
            self.command = kwargs.get('command')
        except KeyError:
            pass
        finally:
            pass

        try:
            super().__init__(kwargs.get("msg"))
        except KeyError:
            raise Exception("Must specify a message")
            pass

    def __str__(self):
        return "{} error: \n\tError_time = {}\n\tHash = {}\n".format(self.__class__.__name__, self.errorTime, self.errorHash)

class DangerError(ErrorTemplate):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ArgumentErr(ErrorTemplate):
    def __init__(self, *args, **kwargs):
        self.required_args = kwargs['required_args']
        self.has_args = kwargs['has_args']
        super().__init__(*args, **kwargs)

    pass


class ConnectionErr(ErrorTemplate):
    pass


class PermissionErr(ErrorTemplate):
    def __init__(self, *args, **kwargs):
        try:
            self.required_premissions = kwargs['required_premissions']
            self.required_premissions = kwargs['has_premissions']
        except KeyError:
            pass

        super().__init__(*args, **kwargs)

    def __str__(self):
        return "{}Reqired permissions: {}\nHas permissions: {}\n".format(super().__str__(), self.required_premissions, self.has_permission)


class InvalidConfig(ErrorTemplate): ...


class InvalidParameter(ErrorTemplate):
    def __str__(self):
        return "{}\nRequired: {}\n got: {}\n".format(super().__str__(), self.required_param, self.has_param)

    def __init__(self, *args, **kwargs):
        try:
            self.required_param = kwargs.get('required_param')
            self.has_param = kwargs.get('has_param')

        except KeyError as ex:
            print("Invalid parameters: {}\n".format(ex.__cause__))

        super().__init__(*args, **kwargs)


class VoidError(ErrorTemplate): ...


class InputError(ErrorTemplate):

    def __init__(self, *args, **kwargs):
        try:
            self.index = kwargs.get('index')
        except KeyError:
            try:
                self.index = args[0] if isinstance(args[0], int) else args[1]
            except:
                self.index = None
        except:
            self.index = None

        try:
            self.src = (kwargs.get('src'))
        except KeyError:
            self.src = None

        try:
            self.message = (kwargs.get('msg'))
        except KeyError:
            try:
                if isinstance(args[0], str):
                    super().__init__(msg=args[0])
                else:
                    super().__init__(msg=args[1])
            except:
                super().__init__()
        except:
            super().__init__()

    def __str__(self):
        formated = form(src=self.src, index=self.index)
        return str(self.message) + ":" + str(("\n\t" + str(self.src)) if self.src != None else "") + ("\n\t {}".format(formated) if formated != "" else "") + '\n' + super().__str__()
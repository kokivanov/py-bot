"""
    Utilite: abc

    Description: 
        Provides basic types for working with data

"""

class userRequestHandler(object):

    """
        Class: UserRequestHandler

        Description:
            Returntype of parser thar allows transfering data to command
    """

    command = str()
    args = list[str]
    flags = dict[str, str]

    def __init__(self, *args, **kwargs):
        i : int = 0

        try:
            self.command = kwargs['command']
        except KeyError:
            try:
                self.command = args[i]
                i+=1
            except IndexError:
                self.command = None
                self.args = None
                self.flags = None
                return

        try:
            self.args = kwargs['args']
        except KeyError:
            try:
                self.args = args[i]
                i+=1
            except IndexError:
                self.args = None

        try:
            self.flags = kwargs['flags']
        except KeyError:
            try:
                self.flags = args[i]
                i+=1
            except IndexError:
                self.flags = None
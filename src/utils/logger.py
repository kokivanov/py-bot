import os
import datetime
from os import path

LOG_ALL = 0x1111
LOG_EVENTS = 0x01111
LOG_WARNS = 0x00111
LOG_SECUTIRY = 0x00011
LOG_ERRORS = 0x00001

LEVEL_MESSAGE = 0x10000
LEVEL_EVENT = 0x01000
LEVEL_WARN = 0x00100
LEVEL_SECURITY = 0x00010
LEVEL_ERRORS = 0x00001

class logger():

    console_output : bool
    file_output : bool
    file_path : str

    logging_level : int
    
    file = None

    def __init__(self, *args, **kwargs):
        console_output = True

        try:
            self.file_output = bool(kwargs.get('file_output'))
            
            if self.file_output:
                if not path.isdir("logs"):
                    os.mkdir("logs")
                self.file_path = "logs/log_{}.log".format(datetime.datetime.now().strftime("%m-%d-%Y_%H-%M"))
                print(self.file_path)
                self.file = open(self.file_path, 'a')

                self.file.write("Successfully logging to {}\n".format(self.file.name))
            
            self.logging_level = kwargs.get('logging_level')

        except KeyError as e:
            print("Error occured:\n{}".format(e))

    def log(self, coroutine): ... # decorator

    async def asyncLog(self, coroutine): ... # decorator

    def event(self, *args, **kwargs): ...
    def exception(self, *args, **kwargs): ...
    def error(self, *args, **kwargs): ...
    def warn(self, *args, **kwargs): ...
    def security(self, *args, **kwargs): ...

    def setLoggerLevel(self, level : int): ...
    def _logMsg(self, *args, **kwargs): ...
    def _logInfo(self, *args, **kwargs): ...
    def _logWarn(self, *args, **kwargs): ...
    def _logError(self, *args, **kwargs): ...
    def _logSecurity(self, *args, **kwargs): ...

    def __log_to_file(self, event): ...
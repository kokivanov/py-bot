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

    def __init__(self, *args, **kwargs): ...
    def log(self, event): ... # decorator
    def setLoggerLevel(self,): ...
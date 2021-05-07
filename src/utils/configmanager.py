from . import abc
from . import databasemanager

class cfg:
    prefix : str
    owner_ID : str

    def __init__(self, server_ID : abc.server_id):
        self.server_ID = server_ID



    # Will try to get parameters using __getCmdParams and __getModParams
    def getParameter(self, *args, **kwargs): ...

    # Will try to get parameters from database
    def __getCmdParams(self, *args, **kwargs): ...
    def __getModParams(self, *args, **kwargs): ...

    def update_parameter(self, *args, **kwargs): ...

    def __updateCmdParameter(self, *args, **kwargs): ...
    def __updateModParameter(self, *args, **kwargs): ...
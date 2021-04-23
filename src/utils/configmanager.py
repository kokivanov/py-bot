class cfg:
    prefix : str
    server_ID : str
    func_setup : dict
    mod_setup : dict

    def __init__(self, *args, **kwargs): ...

    # Will try to get parameters using __getCmdParams and __getModParams
    def getParameter(self, *args, **kwargs): ...

    # Will try to get parameters from database
    def __getCmdParams(self, *args, **kwargs): ...
    def __getModParams(self, *args, **kwargs): ...

    def update_parameter(self, *args, **kwargs): ...

    def __updateCmdParameter(self, *args, **kwargs): ...
    def __updateModParameter(self, *args, **kwargs): ...
class cfg:
    prefix : str
    server_ID : str
    func_setup : dict
    mod_setup : dict

    def __init__(self, *args, **kwargs): ...

    def __getParameter(self, name : str): ...

    def __getParameter(self, m_name : str, cmds : []): ...

    
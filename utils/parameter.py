class parameter(object):
    value : str
    is_necessary : bool

    def __init__(self, name, value, is_necessary):
        self.value = value
        self.is_necessary = is_necessary
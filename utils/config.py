import json

class config:
    
    token : str
    
    prefix : str
    modules : dict
    
    nsfw_allowed : bool
    
    hi_message : str

    def __init__(self, **args):
        if args.get('isFile'):
            fl = open("settings.json")
            jsonc = json.loads(fl.read())

            self.token = jsonc["TOKEN"]
            self.prefix = jsonc["PREFIX"]
            self.modules = jsonc["ENABLED_MODULES"]
            self.hi_message = jsonc["HI_MESSAGE"]["REACTION"]
        print(self)

    def __str__(self):
        return "Class 'Config' with parameters:\nToken:{}\nPrefix: {}\nModules: {}\nMessage reaction: {}\n".format(self.token, self.prefix, self.modules, self.hi_message)

if __name__ == "__main__":  
    conf = config(isFile=True)
    #print(conf)
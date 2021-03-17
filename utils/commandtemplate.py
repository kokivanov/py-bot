import asyncio
import json
from . import exceptions as exc

class Command(object):
    name = ''
    description = ''
    usage = ''
    parameters = []
    aliases = []
    is_callable = True
    required_permissions = {}
    channels_blacklist = []
    roles_blacklist = []

    command = None

    def __init__(self, *args, **kwargs):
        try:
            self.name = kwargs['name']
            self.description = kwargs['description']
            self.parameters = kwargs['parameters']
            self.permissions = kwargs['permissions']
            self.aliases = kwargs['aliases']
            self.is_callable = kwargs['is_callable']
            self.required_permissions = kwargs['required_permissions']
            self.channels_blacklist = kwargs['channels_blacklist']
            self.roles_blacklist = kwargs['roles_blacklist']
            self.command = kwargs['command']
        except (KeyError):
            print("Can't recognize some parameters.")

    async def __call__(self, *args, **kwargs):
        await self.command(*args, **kwargs)

    def __invert__(self):
        other = json.dumps({
            "name" : self.name,
            "description" : self.description,
            "parameters" : self.parameters,
            "permissions" : self.permissions,
            "aliases" : self.aliases,
            "is_callable" : self.is_callable,
            "required_permissions" : self.required_permissions,
            "channels_blacklist" : self.channels_blacklist,
            "roles_blacklist" : self.roles_blacklist
        })

        return other

    def __lshift__(self, p):
        par = json.loads(p)
        self.name = par['name']
        self.description = par['description']
        self.parameters = par['parameters']
        self.permissions = par['permissions']
        self.aliases = par['aliases']
        self.is_callable = par['is_callable']
        self.required_permissions = par['required_permissions']
        self.channels_blacklist = par['channels_blacklist']
        self.roles_blacklist = par['roles_blacklist']
        
        pass

    def __str__(self):
        return "Command {}, {}".format(self.name, self.description)

    def set_permission(self, *args, **kwargs):
        try:
            if not isinstance(args[0], dict):
                err = exc.InvalidParameter(command='{} : premission set'.format(self.__class__.__name__))
                print(err)
                raise err
            self.permissions = args[0]
        except KeyError:
            err = exc.InvalidParameter(command='{} : premission set'.format(self.__class__.__name__))
            print(err)
            raise err

    # def add_permission(self, *args, **kwargs)
    # def remove_permission(self, *args, **kwargs)
    # def prune_permission(self, *args, **kwargs)
    
    # def set_aliases(self, *args, **kwargs)
    # def add_aliases(self, *args, **kwargs)
    # def remove_aliases(self, *args, **kwargs)
    # def prune_aliases(self, *args, **kwargs)

    # def set_availability(self, *args, **kwargs)
    # def change_availability(self, *args, **kwargs)
    
    # def set_channel_blacklist(self, *args, **kwargs)
    # def add_channel_blacklist(self, *args, **kwargs)
    # def remove_channel_blacklist(self, *args, **kwargs)
    # def prune_channel_blacklist(self, *args, **kwargs)

    # def set_role_blacklist(self, *args, **kwargs)
    # def add_role_blacklist(self, *args, **kwargs)
    # def remove_role_blacklist(self, *args, **kwargs)
    # def prune_role_blacklist(self, *args, **kwargs)

def main():
    cmd = Command(
        name='test',
        description='test',
        parameters={'Test':False},
        permissions=[],
        aliases = [],
        is_callable= True,
        required_permissions = [],
        channels_blacklist = [],
        roles_blacklist = [],
        command= None
    )

    print(cmd)

    p = ~cmd
    print(p)

    cmd << '{"name" : "self.name","description" : "self.description","parameters" : {"a" : false},"permissions" : [],"aliases" : [],"is_callable" : true,"required_permissions" : [],"channels_blacklist" : [],"roles_blacklist" : []}'
    print(cmd)

if __name__ == '__main__':
    main()
from . import clear, say

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils.moduletemplate import moduletemplate

admin=moduletemplate(
    commands = [clear, say],
    name= 'admin',
    description= 'Provides help for command or module',
    required_permissions=None,
    channels_blacklist=None,
    roles_blacklist=None,
    command=None
)

print (admin.commands)
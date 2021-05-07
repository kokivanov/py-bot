from . import clear, say

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils.moduletemplate import moduletemplate

admin=moduletemplate(
    commands = [clear.clear, say.say],
    name= 'admin',
    description= 'Provides administrative utilites',
    required_permissions=["%admin", "%moderator"],
    channels_blacklist=None,
    roles_blacklist=None
)
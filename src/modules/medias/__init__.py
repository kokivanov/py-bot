from . import danbooru, reddit, rule34

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils.moduletemplate import moduletemplate

medias= moduletemplate(
    commands = [danbooru.danbooru, reddit.reddit, rule34.rule34],
    name= 'medias',
    description= 'Provides entertaining utilites',
    required_permissions=None,
    channels_blacklist=None,
    roles_blacklist=None,
    command=None
)
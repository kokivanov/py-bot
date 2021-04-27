import unittest

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils import abc
from utils import exceptions

class TestABC(unittest.TestCase):

    def test_commandParametersClass(self):
        res = abc.commandParameters(aliases=["rt", "tts"], is_callable=False, required_permissions=["@admin", "@moderator"], channels_blacklist=["163216456465465"], roles_blacklist=[])
        self.assertIsInstance(res, abc.commandParameters)

    def test_commandParametersSet(self):
        m1 = abc.commandParameters(aliases=["rt", "tts"], is_callable=False, required_permissions=["@admin", "@moderator"], channels_blacklist=["163216456465465"], roles_blacklist=[])
        m2 = abc.commandParameters(aliases=["abc"], is_callable=True, required_permissions=["@admin"], channels_blacklist=[], roles_blacklist=[])

        m1 = m2

        self.assertEqual(m1.aliases, m2.aliases)
        self.assertEqual(m1.is_callable, m2.is_callable)
        self.assertEqual(m1.required_permissions, m2.required_permissions)
        self.assertEqual(m1.channels_blacklist, m2.channels_blacklist)
        self.assertEqual(m1.roles_blacklist, m2.roles_blacklist)

    def test_commandParametersEqual(self):
        m1 = abc.commandParameters(aliases=["rt", "tts"], is_callable=False, required_permissions=["@admin", "@moderator"], channels_blacklist=["163216456465465"], roles_blacklist=[])
        m2 = abc.commandParameters(aliases=["abc"], is_callable=True, required_permissions=["@admin"], channels_blacklist=[], roles_blacklist=[])

        self.assertNotEqual(m1, m2)

        m1 = abc.commandParameters(aliases=["rt", "tts"], is_callable=False, required_permissions=["@admin", "@moderator"], channels_blacklist=["163216456465465"], roles_blacklist=[])
        m2 = abc.commandParameters(aliases=["rt", "tts"], is_callable=False, required_permissions=["@admin", "@moderator"], channels_blacklist=["163216456465465"], roles_blacklist=[])

        self.assertEqual(m1, m2)

    def test_commandParametersInvert(self):
        m1 = abc.commandParameters(aliases=["rt", "tts"], is_callable=False, required_permissions=["@admin", "@moderator"], channels_blacklist=["163216456465465"], roles_blacklist=[])

        self.assertTrue((~m1).is_callable)
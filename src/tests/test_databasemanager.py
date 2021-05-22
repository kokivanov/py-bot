import unittest
import asyncio

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

dirname = os.path.dirname(os.path.dirname(__file__))
filename = os.path.join(dirname, 'dbconfig.json')

from utils.databasemanager import dbmanager as db

class test_databaseManager(unittest.TestCase):

    def test_connectDatabase(self):
        database = db(open(filename))
        self.assertTrue(asyncio.get_event_loop().run_until_complete(database.is_still_connected()))

    def test_getZeroServerConfig(self):
        database = db(open(filename))
        expected = {'prefix': None, 'server_id': '0', 'global_mutes': 0, 'global_bans': 0, 'global_leveling': 0, 'rpg_use_global_mobs': 0, 'rpg_use_global_items': 0, 'fishing_use_global_items': 0}
        got = asyncio.get_event_loop().run_until_complete(database.get_Server_Config(0, 0))

        print(got)

        self.assertEqual(got, expected)

    def test_getNonexistingServerConfig(self):
        database = db(open(filename))
        expected = {'prefix': None, 'server_id': '1', 'global_mutes': 0, 'global_bans': 0, 'global_leveling': 0, 'rpg_use_global_mobs': 0, 'rpg_use_global_items': 0, 'fishing_use_global_items': 0}
        got = asyncio.get_event_loop().run_until_complete(database.get_Server_Config(1, 1))

        self.assertEqual(expected, got)
        asyncio.get_event_loop().run_until_complete(database.delete_row(table="global_config", server_ID="1"))




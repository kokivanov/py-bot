import unittest

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils import abc
from utils import exceptions
from utils import commandmanager

class TestCommandManager(unittest.TestCase):

    def test_getList(self):
        res = commandmanager.getList()
        print(res)
        self.assertIsInstance(res, dict)

    def test_getListUnique(self):
        res = commandmanager.getListUnique()
        print(res)
        self.assertIsInstance(res, list)
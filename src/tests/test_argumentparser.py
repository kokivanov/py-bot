import unittest

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils import argumentparser
from utils import exceptions
from utils.abc import userRequestHandler

from __utils import cfg

class TestArgumentParser(unittest.TestCase):

    def test_ParserSimple(self):
        config = cfg()

        raw = "t-test first secound -f=1 --secound=2 -t --fourth -e=True"
        expecting = userRequestHandler(command='test', args=["first", "secound"], flags={"f" : "1", "secound" : "2", "t" : None, "fourth" : None, "e" : "True"})
        result = argumentparser.parse(raw=raw, config=config)

        self.assertEqual(result, expecting)

        raw = "t-test.test first secound -f=1 --secound=2 -t --fourth -e=True"
        expecting = userRequestHandler(command='test.test', args=["first", "secound"], flags={"f" : "1", "secound" : "2", "t" : None, "fourth" : None, "e" : "True"})
        result = argumentparser.parse(raw=raw, config=config)

        self.assertEqual(result, expecting)

    def test_ParserQuotes(self):
        config = cfg()

        raw = "t-test \"first secound\" third -f=1 --secound=2 -t --fourth -e=True -G=\"Mingw Makefile\" --query=\"Raphtalia shield hero\""
        expecting = userRequestHandler(command='test', args=["first secound", "third"], flags={"f" : "1", "secound" : "2", "t" : None, "fourth" : None, "e" : "True", "G" : "Mingw Makefile", "query" : "Raphtalia shield hero"})
        result = argumentparser.parse(raw=raw, config=config)

        self.assertEqual(result, expecting)
        
        raw = "t-test \'first secound\' third -f=1 --secound=2 -t --fourth -e=True -G=\'Mingw Makefile\' --query=\'Raphtalia shield hero\'"
        expecting = userRequestHandler(command='test', args=["first secound", "third"], flags={"f" : "1", "secound" : "2", "t" : None, "fourth" : None, "e" : "True", "G" : "Mingw Makefile", "query" : "Raphtalia shield hero"})
        result = argumentparser.parse(raw=raw, config=config)

        self.assertEqual(result, expecting)

    def test_ParserOddQuotes(self):
        config = cfg()

        raw = "t-test \"first secound\" third -f=1 --secound=2 -t --fourth -e=True -G=\"Mingw Makefile\" --query='Raphtalia shield hero' \"hello there"
        expecting = userRequestHandler(command='test', args=["first secound", "third", "hello there"], flags={"f" : "1", "secound" : "2", "t" : None, "fourth" : None, "e" : "True", "G" : "Mingw Makefile", "query" : "Raphtalia shield hero"})
        result = argumentparser.parse(raw=raw, config=config)

        self.assertEqual(result, expecting)

        raw = "t-test \'first secound\' third -f=1 --secound=2 -t --fourth -e=True -G=\'Mingw Makefile\' --query='Raphtalia shield hero' \'hello there"
        expecting = userRequestHandler(command='test', args=["first secound", "third", "hello there"], flags={"f" : "1", "secound" : "2", "t" : None, "fourth" : None, "e" : "True", "G" : "Mingw Makefile", "query" : "Raphtalia shield hero"})
        result = argumentparser.parse(raw=raw, config=config)

        self.assertEqual(result, expecting)

        raw = "t-test \"first secound\" third -f=1 --secound=2 -t --fourth -e=True -G=\"Mingw Makefile\" --query=\"Raphtalia shield hero\" \"hello there"
        expecting = userRequestHandler(command='test', args=["first secound", "third", "hello there"], flags={"f" : "1", "secound" : "2", "t" : None, "fourth" : None, "e" : "True", "G" : "Mingw Makefile", "query" : "Raphtalia shield hero"})
        result = argumentparser.parse(raw=raw, config=config)

        self.assertEqual(result, expecting)

    def test_ParserMultipleQuotesSimple(self):
        config = cfg()

        raw = "t-test 'first' \"secound\" third -f=1 --secound=2 -t --fourth -e=True -G=\"Mingw Makefile\" --query='Raphtalia shield hero' \"hello there'"
        expecting = userRequestHandler(command='test', args=["first", "secound", "third", "hello there'"], flags={"f" : "1", "secound" : "2", "t" : None, "fourth" : None, "e" : "True", "G" : "Mingw Makefile", "query" : "Raphtalia shield hero"})
        result = argumentparser.parse(raw=raw, config=config)

        self.assertEqual(result, expecting)

    def test_ParserPunct(self):
        config = cfg()

        raw = "t-test 'fi.rst' \"seco.und\" thi.rd -f=1 --secound=\'2!\' -t --fourth -e=True -G=\"Mingw Makefile\" --query='Raphtalia! shield: hero' \"hello !.there'"
        expecting = userRequestHandler(command='test', args=["fi.rst", "seco.und", "thi.rd", "hello !.there'"], flags={"f" : "1", "secound" : "2!", "t" : None, "fourth" : None, "e" : "True", "G" : "Mingw Makefile", "query" : "Raphtalia! shield: hero"})
        result = argumentparser.parse(raw=raw, config=config)

        self.assertEqual(result, expecting)

    def test_ParserQuotesInQuotes(self):
        config = cfg()

        raw = "t-test '\\\"' '\\'' -q='\"' -t=\"'\""
        expecting = userRequestHandler(command='test', args=["\"", "'"], flags={"q" : "\"", "t" : "\'"})
        result = argumentparser.parse(raw=raw, config=config)

        self.assertEqual(result, expecting)


    def test_ParserMultipleOddQuotes(self):
        config = cfg()

        with self.assertRaises(exceptions.InputError) as exception:
            raw = "t-test 'fi.rst' \"seco.und\"\' thi.rd -f=1 --secound=\'2!\' -t --fourth -e=True -G=\"Mingw Makefile\" --query='Raphtalia! shield: hero' \"hello !.there'"
            result = argumentparser.parse(raw=raw, config=config)

    def test_ParserException(self):
        config = cfg()

        with self.assertRaises(exceptions.InputError) as exception:
            raw = "t-test -query"
            result = argumentparser.parse(raw=raw, config=config)

        with self.assertRaises(exceptions.InputError) as exception:
            raw = "t-test --query= "
            result = argumentparser.parse(raw=raw, config=config)

        with self.assertRaises(exceptions.InputError) as exception:
            raw = "t-test '♥'"
            result = argumentparser.parse(raw=raw, config=config)
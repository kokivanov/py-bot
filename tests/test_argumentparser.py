import unittest

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils import argumentparser

class TestArgumetParser(unittest.TestCase):

    def test_ParserSimple(self):
        result = argumentparser.parse("a b c")
        expect = ["a", "b", "c"]
        self.assertEqual(result, expect)

    def test_ParserQuotes(self):
        result = argumentparser.parse("\"Hello world!\" Hello planet!")
        expect = ["Hello world!", "Hello", "planet!"]
        self.assertEqual(result, expect)
        
        result = argumentparser.parse("'Hello world!' Hello planet!")
        expect = ["Hello world!", "Hello", "planet!"]
        self.assertEqual(result, expect)

        result = argumentparser.parse("Hello world! \"Hello planet!\"")
        expect = ["Hello", "world!", "Hello planet!"]
        self.assertEqual(result, expect)
        
        result = argumentparser.parse("Hello world! 'Hello planet!'")
        expect = ["Hello", "world!", "Hello planet!"]
        self.assertEqual(result, expect)

        result = argumentparser.parse("Hell\"o w\"orld! \"Hello planet!\"")
        expect = ["Hell", "o w", "orld!", "Hello planet!"]
        self.assertEqual(result, expect)
        
        result = argumentparser.parse("Hell'o w'orld! \"Hello planet!\"")
        expect = ["Hell", "o w", "orld!", "Hello planet!"]
        self.assertEqual(result, expect)
        
    def test_ParserOddQuotes(self):
        result = argumentparser.parse("\"Hello world!\" \"Hello planet!")
        expect = ["Hello world!", "Hello planet!"]
        self.assertEqual(result, expect)
        
        result = argumentparser.parse("'Hello world!' 'Hello planet!")
        expect = ["Hello world!", "Hello planet!"]
        self.assertEqual(result, expect)

        result = argumentparser.parse("'Hello world!' Hel'lo planet!")
        expect = ["Hello world!", "Hel", "lo planet!"]
        self.assertEqual(result, expect)

        result = argumentparser.parse("\"Hello world!\" Hel\"lo planet!")
        expect = ["Hello world!", "Hel", "lo planet!"]
        self.assertEqual(result, expect)

    def test_ParserMultipleQuotesSimple(self):
        result = argumentparser.parse("\"Hello world!\" 'Hello planet!'")
        expect = ["Hello world!", "Hello planet!"]
        self.assertEqual(result, expect)

        result = argumentparser.parse("\"Hello world!\" He'llo p'lanet!")
        expect = ["Hello world!", "He", "llo p", "lanet!"]
        self.assertEqual(result, expect)

    def test_ParserMultipleOddQuotes(self):
        result = argumentparser.parse("\"Hello 'world!'\" 'Hel'lo \"planet!\"'")
        expect = ["Hello 'world!'", "Hel", "lo", "planet!"]
        self.assertEqual(result, expect)

    def test_ParserLongString(self):
        result = argumentparser.parse("say \"Lorem in the bath so I'll take over her duty\" \"10\" '@datak#1232\"\"\" kek w")
        expect = ["say", "Lorem in the bath so I'll take over her duty", "10", "@datak#1232\"\"\" kek w"]
        self.assertEqual(result, expect)
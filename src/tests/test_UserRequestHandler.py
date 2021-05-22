import unittest
import datetime
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils import abc

class TestUserRequestHandler(unittest.TestCase):
    
    def testInitCorrect(self):
        command = "say"
        args = ["Hellow world!"]
        flags = {"channel" : "210654654006"}
        
        test = abc.userRequestHandler(command=command, args=args, flags=flags)

        self.assertIsInstance(test, abc.userRequestHandler)
        self.assertEqual(command, test.command)
        self.assertEqual(args, test.args)
        self.assertEqual(flags, test.flags)

        del test

        test = abc.userRequestHandler(command, args, flags)

        self.assertIsInstance(test, abc.userRequestHandler)
        self.assertEqual(command, test.command)
        self.assertEqual(args, test.args)
        self.assertEqual(flags, test.flags)

        del test

        test1 = abc.userRequestHandler(command, args, flags)
        test2 = abc.userRequestHandler()
        self.assertNotEqual(test1, test2)


    def testInitOneArgument(self):
        command = "say"
        args = ["Hellow world!"]
        flags = {"channel" : "210654654006"}

        test = abc.userRequestHandler(command=command)

        self.assertIsInstance(test, abc.userRequestHandler)
        self.assertEqual(command, test.command)
        self.assertEqual(test.args, [])
        self.assertEqual(test.flags, {})

        del test

        test = abc.userRequestHandler(command)

        self.assertIsInstance(test, abc.userRequestHandler)
        self.assertEqual(command, test.command)
        self.assertEqual(test.args, [])
        self.assertEqual(test.flags, {})

        del test

    def testInitMixedArguments(self):
        command = "say"
        args = ["Hellow world!"]
        flags = {"channel" : "210654654006"}

        test = abc.userRequestHandler(command, args, flags)

        self.assertIsInstance(test, abc.userRequestHandler)
        self.assertEqual(command, test.command)
        self.assertEqual(args, test.args)
        self.assertEqual(flags, test.flags)
        
        del test
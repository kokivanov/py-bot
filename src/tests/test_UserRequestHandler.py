import unittest
import datetime
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils import abc

class UserRequestHandler(unittest.TestCase):
    
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

    def testInitOneArgument(self):
        command = "say"
        args = ["Hellow world!"]
        flags = {"channel" : "210654654006"}

        test = abc.userRequestHandler(command=command)

        self.assertIsInstance(test, abc.userRequestHandler)
        self.assertEqual(command, test.command)
        self.assertEqual(test.args, None)
        self.assertEqual(test.flags, None)

        del test

        test = abc.userRequestHandler(command)

        self.assertIsInstance(test, abc.userRequestHandler)
        self.assertEqual(command, test.command)
        self.assertEqual(test.args, None)
        self.assertEqual(test.flags, None)

        del test

    def testInitMixedArguments(self):
        command = "say"
        args = ["Hellow world!"]
        flags = {"channel" : "210654654006"}

        test = abc.userRequestHandler(args, command=command, flags=flags)

        self.assertIsInstance(test, abc.userRequestHandler)
        self.assertEqual(command, test.command)
        self.assertEqual(args, test.args)
        self.assertEqual(flags, test.flags)
        
        del test

        test = abc.userRequestHandler(command, args=args, flags=flags)

        self.assertIsInstance(test, abc.userRequestHandler)
        self.assertEqual(command, test.command)
        self.assertEqual(args, test.args)
        self.assertEqual(flags, test.flags)

        del test

    def testInitIncorrectArgument(self):
        command = "say"
        args = ["Hellow world!"]
        flags = {"channel" : "210654654006"}

        test = abc.userRequestHandler(flags=flags)

        self.assertIsInstance(test, abc.userRequestHandler)
        self.assertEqual(test.command, None)
        self.assertEqual(test.args, None)
        self.assertEqual(test.flags, None)
        
        del test
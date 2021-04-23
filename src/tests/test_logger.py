import unittest
import datetime
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils import logger

class TestLogger(unittest.TestCase):
    
    def testLoggerNoFileInit(self):
        result = logger.logger(file_output = False, logging_level = logger.LOG_ALL)
        self.assertIsInstance(result, logger.logger)
        self.assertEqual(result.file_output, False)
        self.assertEqual(result.logging_level, logger.LOG_ALL)

    def testLoggerFileInit(self):
        result = logger.logger(file_output = True, logging_level = logger.LOG_ALL)
        file_path  = "logs/log_{}.log".format(datetime.datetime.now().strftime("%m-%d-%Y_%H-%M"))
        self.assertIsInstance(result, logger.logger)
        self.assertEqual(result.file_output, True)
        self.assertEqual(result.file_path, file_path)
        self.assertEqual(result.logging_level, logger.LOG_ALL)
        self.assertTrue(os.path.exists(file_path))
        del result

        os.remove(file_path)
        os.rmdir(os.path.dirname(file_path))
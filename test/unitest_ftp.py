import os
import sys
import unittest

import config

from test.ftp.testMain import testMain
from test.ftp.testFTPCommandClient import TestFTPCommandClient

def test_ftp():
    test_main = unittest.TestLoader().loadTestsFromTestCase(testMain)
    test_ftp_command_client = unittest.TestLoader().loadTestsFromTestCase(TestFTPCommandClient)

    allTests = unittest.TestSuite()
    
    allTests.addTest(test_main)
    allTests.addTest(test_ftp_command_client)

    unittest.TextTestRunner(verbosity=2, failfast=True).run(allTests)

test_ftp()
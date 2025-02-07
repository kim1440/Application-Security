import os
import sys
import unittest

import config

from test.ftp.testMain import testMain

def test_ftp():
    test_main = unittest.TestLoader().loadTestsFromTestCase(testMain)

    allTests = unittest.TestSuite()
    
    allTests.addTest(test_main)

    unittest.TextTestRunner(verbosity=2, failfast=True).run(allTests)

test_ftp()
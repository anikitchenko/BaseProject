# -*- coding: utf-8 -*-

import unittest
import sys

from test.Test.LeadPage.LeadPageTestCase import LeadPageTestCase


def suite():

    test_suite = unittest.TestSuite()

    test_suite.addTest(LeadPageTestCase("test_change_lead_status"))
    return test_suite


if __name__ == '__main__':
    result = unittest.TextTestRunner(verbosity=2).run(suite())
    sys.exit(not result.wasSuccessful())

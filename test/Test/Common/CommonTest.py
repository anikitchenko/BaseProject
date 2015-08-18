# -*- coding: utf-8 -*-

import logging
import unittest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class CommonTestCase(unittest.TestCase):
    
    browser = "firefox"

    def setUp(self):
        if self.browser == "firefox":
            self.driver = webdriver.Firefox()
            self.wait = WebDriverWait
            logging.info("Opening browser Firefox")
            self.is_browser_open = True
        self.driver.maximize_window()
        return self.driver

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
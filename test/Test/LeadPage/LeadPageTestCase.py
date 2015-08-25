# -*- coding: utf-8 -*-

import unittest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from test.Action.LoginPageAction import LoginPageAction

from test.Action.SettingsPageAction import SettingsPageAction
from test.Model.Enum.SettingsPageEnum import SettingsPageEnum
from test.Model.SettingsPage.SettingsPageModel import SettingsPageModel
from test.View.SettingsPageVeiw import SettingsPageView

from test.Action.LeadPageAction import LeadPageAction
from test.Model.Enum.LeadPageEnum import LeadPageEnum
from test.Model.LeadPage.LeadPageModel import LeadPageModel
from test.View.LeadPageView import LeadPageView


class LeadPageTestCase(unittest.TestCase):

    # region Config
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait
        self.driver.maximize_window()
        self.login_page_action = LoginPageAction(self.driver, self.wait)
        self.lead_page_action = LeadPageAction(self.driver, self.wait)
        self.settings_page_action = SettingsPageAction(self.driver, self.wait)
        self.lead_page_model = LeadPageModel(self.driver, self.wait)
        self.settings_page_model = SettingsPageModel(self.driver, self.wait)
        self.login_page_action.open_login_page()
        self.login_page_action.handle_login_form()

    def tearDown(self):
        self.settings_page_action.change_lead_status(LeadPageEnum.LEAD_STATUS.get(1))
        self.lead_page_action.delete_new_lead()
        self.driver.close()
        self.driver.quit()
    # endregion

    def test_change_lead_status(self):
        self.lead_page_action.create_new_lead()
        self.assertEqual(self.lead_page_model.get_breadcrumbs_lead_title(),
                         (LeadPageEnum.NAME + LeadPageEnum.LAST_NAME), LeadPageView.INCORRECT_TITLE)
        self.assertEqual(self.lead_page_model.get_lead_status(), LeadPageEnum.LEAD_STATUS.get(1),
                         LeadPageView.INCORRECT_LEAD_STATUS)
        self.settings_page_action.change_lead_status(SettingsPageEnum.NEW_STATUS_TITLE)
        self.assertEqual(SettingsPageEnum.NEW_STATUS_MESSAGE, self.settings_page_model.get_new_lead_status_message(),
                         SettingsPageView.INCORRECT_NEW_STATUS_MESSAGE)
        self.assertEqual(SettingsPageEnum.NEW_STATUS_TITLE, self.settings_page_model.get_lead_changed_status(),
                         SettingsPageView.INCORRECT_NEW_STATUS_TITLE)
        self.lead_page_action.open_new_lead()
        self.assertListEqual(self.lead_page_model.get_list_of_status_from_drop_down(),
                             LeadPageEnum.LEAD_STATUS_LIST, LeadPageView.INCORRECT_LIST_OF_STATUS)

# -*- coding: utf-8 -*-

import time
from test.Action.SettingsPageAction import SettingsPageAction
from test.Model.Enum.SettingsPageEnum import SettingsPageEnum
from test.Model.SettingsPage.SettingsPageModel import SettingsPageModel

from test.Test.Common.CommonTest import CommonTestCase

from test.Action.LeadPageAction import LeadPageAction
from test.Action.LoginPageAction import LoginPageAction

from test.Model.LeadPage.LeadPageModel import LeadPageModel

from test.Model.Enum.LeadPageEnum import LeadPageEnum

from test.View.LeadPageView import LeadPageView as ET


class LeadPageTestCase(CommonTestCase):

    def test_add_new_lead(self):
        login_page_action = LoginPageAction(self.driver, self.wait)
        lead_page_action = LeadPageAction(self.driver, self.wait)
        lead_page_model = LeadPageModel(self.driver, self.wait)
        login_page_action.open_login_page()
        login_page_action.handle_login_form()
        lead_page_action.open_lead_page()
        lead_page_action.handle_new_lead()
        self.assertEqual(lead_page_model.get_breadcrumbs_lead_title(), (LeadPageEnum.NAME + LeadPageEnum.LAST_NAME),
                         ET.INCORRECT_TITLE)
        self.assertEqual(lead_page_model.get_lead_status(), LeadPageEnum.LEAD_STATUS.get(1), ET.INCORECT_LEAD_STATUS)

    def test_add_new_lead_status(self):
        login_page_action = LoginPageAction(self.driver, self.wait)
        lead_page_action = LeadPageAction(self.driver, self.wait)
        settings_page_action = SettingsPageAction(self.driver, self.wait)
        settings_page_model = SettingsPageModel(self.driver, self.wait)
        login_page_action.open_login_page()
        login_page_action.handle_login_form()
        settings_page_action.open_settings_page()
        settings_page_action.handle_new_lead_status()
        self.assertEqual(SettingsPageEnum.NEW_STATUS_MESSAGE, settings_page_model.get_new_lead_status_message(), "asdasd")
        self.assertEqual(SettingsPageEnum.NEW_STATUS_TITLE, settings_page_model.get_lead_status_list(), "asdasd")

        # lead_page_action.open_lead_page()
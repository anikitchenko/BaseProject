#!/usr/bin/python3.3
# -*- coding: utf-8 -*-

from test.Model.Selector.SettingsPageSelector import SettingsPageSelector


class SettingsPageModel(object):

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def get_lead_status_new_element(self):
        new_lead_status = self.driver.find_element_by_css_selector(SettingsPageSelector.LEAD_STATUS_LAST_ELEMENT).text
        return new_lead_status

    def get_new_lead_status_message(self):
        new_lead_status_message = self.driver.find_element_by_css_selector(SettingsPageSelector.NEW_LEAD_MESSAGE).text
        return new_lead_status_message

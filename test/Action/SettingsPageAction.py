#!/usr/bin/python3.3
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from test.Model.Enum.CommonEnum import CommonEnum

from test.Model.Selector.SettingsPageSelector import SettingsPageSelector


class SettingsPageAction(object):

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def open_settings_page(self):
        self.driver.get(CommonEnum.SETTINGS_LEAD_PAGE_STATUS)

    def change_lead_status(self, lead_status):
        self.open_settings_page()
        self.__wait_until_element_exist(SettingsPageSelector.EDIT_LEAD_STATUS_BUTTON)
        self.__click_edit_lead_button()
        self.__wait_until_element_exist(SettingsPageSelector.EDIT_LEAD_STATUS_NAME_FIELD)
        self.__fill_name_field(lead_status)
        self.__click_save_button()
        self.__wait_until_element_exist(SettingsPageSelector.NEW_LEAD_MESSAGE)

    def __click_edit_lead_button(self):
        self.driver.find_element_by_css_selector(SettingsPageSelector.EDIT_LEAD_STATUS_BUTTON).click()

    def __fill_name_field(self, lead_status):
        self.driver.find_element_by_css_selector(SettingsPageSelector.EDIT_LEAD_STATUS_NAME_FIELD).clear()
        self.driver.find_element_by_css_selector(SettingsPageSelector.EDIT_LEAD_STATUS_NAME_FIELD).\
            send_keys(lead_status)

    def __click_save_button(self):
        self.driver.find_element_by_css_selector(SettingsPageSelector.EDIT_LEAD_STATUS_BUTTON_SAVE).click()

    def __wait_until_element_exist(self, selector):
        self.wait(self.driver, 200).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))

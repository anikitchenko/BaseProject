#!/usr/bin/python3.3
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from test.Model.Enum.CommonEnum import CommonEnum

from test.Model.Enum.LeadPageEnum import LeadPageEnum
from test.Model.Selector.LeadPageSelector import LeadPageSelector


class LeadPageAction(object):

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def open_lead_page(self):
        self.driver.get(CommonEnum.LEADS_PAGE)

    def handle_new_lead(self):
        self.__wait_until_element_exist(LeadPageSelector.NEW_LEAD_BUTTON)
        self.__click_new_lead_button()
        self.__wait_until_element_exist(LeadPageSelector.NEW_LEAD_SAVE_BUTTON)
        self.__fill_name_field()
        self.__fill_last_name_field()
        self.__fill_company_field()
        self.__click_save_button()
        self.__wait_until_element_exist(LeadPageSelector.EDIT_LEAD_BUTTON)

    def __click_new_lead_button(self):
        self.driver.find_element_by_css_selector(LeadPageSelector.NEW_LEAD_BUTTON).click()

    def __fill_name_field(self):
        self.driver.find_element_by_css_selector(LeadPageSelector.NEW_LEAD_NAME_FIELD).send_keys(LeadPageEnum.NAME)

    def __fill_last_name_field(self):
        self.driver.find_element_by_css_selector(LeadPageSelector.NEW_LEAD_SURNAME_FIELD).send_keys(LeadPageEnum.LAST_NAME)

    def __fill_company_field(self):
        self.driver.find_element_by_css_selector(LeadPageSelector.NEW_LEAD_COMPANY_NAME_FIELD).send_keys(LeadPageEnum.COMPANY_NAME)

    def __click_save_button(self):
        self.driver.find_element_by_css_selector(LeadPageSelector.NEW_LEAD_SAVE_BUTTON).click()

    def __wait_until_element_exist(self, selector):
        self.wait(self.driver, 200).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))

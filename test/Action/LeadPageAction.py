#!/usr/bin/python3.3
# -*- coding: utf-8 -*-

import time

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

    def create_new_lead(self):
        self.__wait_until_element_exist(LeadPageSelector.NEW_LEAD_BUTTON)
        self.__click_new_lead_button()
        self.__wait_until_element_exist(LeadPageSelector.NEW_LEAD_SAVE_BUTTON)
        self.__fill_name_field()
        self.__fill_last_name_field()
        self.__fill_company_field()
        self.__click_save_button()
        self.__wait_until_element_exist(LeadPageSelector.EDIT_LEAD_BUTTON)

    def open_new_lead(self):
        self.__wait_until_element_exist(LeadPageSelector.LAST_LEAD_ELEMENT_FORM_LIST)
        self.__open_last_lead()
        self.__wait_until_element_exist(LeadPageSelector.LEAD_STATUS_LINK)
        self.__open_lead_status_drop_down()
        self.__wait_until_element_exist(LeadPageSelector.LEAD_STATUS_DROP_DOWN_ELEMENTS)

    def delete_new_lead(self):
        self.open_lead_page()
        self.__wait_until_element_exist(LeadPageSelector.LAST_LEAD_ELEMENT_FORM_LIST)
        self.__open_last_lead()
        self.__wait_until_element_exist(LeadPageSelector.DELETE_LEAD_BUTTON)
        self.__click_delete_lead_button()
        self.__wait_until_element_exist(LeadPageSelector.ACCEPT_DELETE_LEAD_BUTTON)
        self.__accept_delete_lead()
        time.sleep(2)

    def __click_new_lead_button(self):
        self.driver.find_element_by_css_selector(LeadPageSelector.NEW_LEAD_BUTTON).click()

    def __fill_name_field(self):
        self.driver.find_element_by_css_selector(LeadPageSelector.NEW_LEAD_NAME_FIELD).send_keys(LeadPageEnum.NAME)

    def __fill_last_name_field(self):
        self.driver.find_element_by_css_selector(LeadPageSelector.NEW_LEAD_SURNAME_FIELD).\
            send_keys(LeadPageEnum.LAST_NAME)

    def __fill_company_field(self):
        self.driver.find_element_by_css_selector(LeadPageSelector.NEW_LEAD_COMPANY_NAME_FIELD).\
            send_keys(LeadPageEnum.COMPANY_NAME)

    def __click_save_button(self):
        self.driver.find_element_by_css_selector(LeadPageSelector.NEW_LEAD_SAVE_BUTTON).click()

    def __wait_until_element_exist(self, selector):
        self.wait(self.driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))

    def __open_last_lead(self):
        self.driver.find_element_by_css_selector(LeadPageSelector.LAST_LEAD_ELEMENT_FORM_LIST).click()

    def __open_lead_status_drop_down(self):
        self.driver.find_element_by_css_selector(LeadPageSelector.LEAD_STATUS_LINK).click()

    def __click_delete_lead_button(self):
        self.driver.find_element_by_css_selector(LeadPageSelector.DELETE_LEAD_BUTTON)

    def __accept_delete_lead(self):
        self.driver.find_element_by_css_selector(LeadPageSelector.ACCEPT_DELETE_LEAD_BUTTON)


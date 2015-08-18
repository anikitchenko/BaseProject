#!/usr/bin/python3.3
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from test.Model.Enum.CommonEnum import CommonEnum

from test.Model.Selector.LoginPageSelector import LoginPageSelector
from test.Model.Selector.MainPageSelector import MainPageSelector


class LoginPageAction(object):

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def open_login_page(self):
        self.driver.get(CommonEnum.LOGIN_PAGE)

    def handle_login_form(self):
        self.__fill_login_field()
        self.__fill_password_field()
        self.__click_submit_button()
        self.__wait_until_element_exist(MainPageSelector.LEADS_MENU_BUTTON)

    def __fill_login_field(self):
        self.driver.find_element_by_css_selector(LoginPageSelector.LOGIN_FIELD).send_keys(CommonEnum.LOGIN)

    def __fill_password_field(self):
        self.driver.find_element_by_css_selector(LoginPageSelector.PASSWORD_FIELD).send_keys(CommonEnum.PASSWORD)

    def __click_submit_button(self):
        self.driver.find_element_by_css_selector(LoginPageSelector.LOGIN_BUTTON).click()

    def __wait_until_element_exist(self, selector):
        self.wait(self.driver, 200).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))



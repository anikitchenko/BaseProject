#!/usr/bin/python3.3
# -*- coding: utf-8 -*-

from test.Model.Selector.LeadPageSelector import LeadPageSelector


class LeadPageModel(object):

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def get_breadcrumbs_lead_title(self):
        lead_title = self.driver.find_element_by_css_selector(LeadPageSelector.LEAD_BREADCRUMBS_TITLE).text
        new_lead_title = lead_title.strip().replace(" ", "")
        return new_lead_title

    def get_lead_status(self):
        lead_status = self.driver.find_element_by_css_selector(LeadPageSelector.LEAD_STATUS_LINK).text
        return lead_status
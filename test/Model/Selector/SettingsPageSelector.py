#!/usr/bin/python3.3
# -*- coding: utf-8 -*-


class SettingsPageSelector(object):

    __ADD_LEAD_BLOCK = "#lead-status "
    ADD_LEAD_STATUS_BUTTON = __ADD_LEAD_BLOCK + ".btn.btn-mini.new"
    ADD_LEAD_STATUS_NAME_FIELD = __ADD_LEAD_BLOCK + "#name"
    ADD_LEAD_STATUS_BUTTON_SAVE = __ADD_LEAD_BLOCK + ".btn.btn-primary.save"

    NEW_LEAD_MESSAGE = ".alert.alert-success"
    LEAD_STATUSES_LAST_ELEMENT = __ADD_LEAD_BLOCK + ".control-group.item .control-label:last-of-type h4"

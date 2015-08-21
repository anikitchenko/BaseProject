#!/usr/bin/python3.3
# -*- coding: utf-8 -*-


class SettingsPageSelector(object):

    __LEAD_BLOCK = "#lead-status span.named-object-lead"
    EDIT_LEAD_STATUS_BUTTON = __LEAD_BLOCK + ":first-of-type .btn.btn-mini.edit"
    LEAD_STATUS_TITLE = __LEAD_BLOCK + ":nth-of-type({index}) h4".format(index=1)

    EDIT_LEAD_STATUS_NAME_FIELD = __LEAD_BLOCK + " .input-xlarge"
    EDIT_LEAD_STATUS_BUTTON_SAVE = __LEAD_BLOCK + " .btn.btn-primary.save"

    NEW_LEAD_MESSAGE = ".alert.alert-success"

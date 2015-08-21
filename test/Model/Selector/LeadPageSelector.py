#!/usr/bin/python3.3
# -*- coding: utf-8 -*-


class LeadPageSelector(object):

    NEW_LEAD_BUTTON = "#leads-new"

    NEW_LEAD_NAME_FIELD = "#lead-first-name"
    NEW_LEAD_SURNAME_FIELD = "#lead-last-name"
    NEW_LEAD_COMPANY_NAME_FIELD = "#lead-company-name"
    NEW_LEAD_SAVE_BUTTON = ".save.btn.btn-large.btn-primary"

    EDIT_LEAD_BUTTON = ".btn.btn-mini.detail-edit"
    LEAD_STATUS_LINK = ".lead-status"
    LEAD_STATUS_DROP_DOWN_ELEMENTS = ".dropdown.open li"
    LEAD_BREADCRUMBS_TITLE = ".detail-title"

    LAST_LEAD_ELEMENT_FORM_LIST = ".object-list-item:last-of-type h3 a.lead-name"

    DELETE_LEAD_BUTTON = ".sidebar-section a.btn.delete"
    ACCEPT_DELETE_LEAD_BUTTON = ".modal-footer a:last-of-type"

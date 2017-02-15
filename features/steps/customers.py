# -*- coding: utf-8 -*-
import re
from ConfigParser import SafeConfigParser

import time
from behave import *
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from wheel.signatures import assertTrue
from features.pages.page_selector import AddManager, GeneralLocator, AddCustomer
import general_methods

@when("delete all customers")
def step_impl(context):
    context.browser.implicitly_wait(10)
    i = 1
    while i <= len(context.browser.find_elements(*GeneralLocator.TABLE_BODY)):
        context.browser.find_element(*GeneralLocator.TABLE_FIRST).click()
        btn = context.browser.find_element(By.ID, "deleteCustomerBtn")
        btn.click()
        time.sleep(1)


@when('create "{text}" customers')
def step_impl(context, text):
    general_methods.create_customers(context, text)

user_info_edit = []
@when('change Company "{company}", Phone "{phone}", Country "{country}"')
def step_impl(context, company, phone, country):
    context.browser.find_element(*AddCustomer.COMPANY_SIDE_MENU).clear()
    context.browser.find_element(*AddCustomer.COMPANY_SIDE_MENU).send_keys(company)
    context.browser.find_element(*AddCustomer.PHONE_SIDE_MENU).clear()
    context.browser.find_element(*AddCustomer.PHONE_SIDE_MENU).send_keys(phone)
    context.browser.find_element(*AddCustomer.COUNTRY_SIDE_MENU).clear()
    context.browser.find_element(*AddCustomer.COUNTRY_SIDE_MENU).send_keys(country)
    user_info_edit.extend([company, phone, country])


@then("customer was changed successfully")
def step_impl(context):
    context.browser.find_element(*GeneralLocator.SEARCH).send_keys(user_info_edit[0])
    context.browser.find_element(*GeneralLocator.SEARCH).send_keys(Keys.ENTER)
    time.sleep(2)
    ac = context.browser.find_element(*GeneralLocator.TABLE_FIRST).text
    user_info = ac.split("\n")
    user = [user_info_edit[0], user_info_edit[1], user_info_edit[2]]
    user_info.pop(4)
    user_info.pop(2)
    user.sort()
    user_info.sort()
    assert user == user_info


@when("click on Save button into Managers")
def step_impl(context):
    context.browser.find_element(*AddCustomer.SAVE_EDITABLE_CUSTOMER).click()
    time.sleep(1)
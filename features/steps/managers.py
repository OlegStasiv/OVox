# -*- coding: utf-8 -*-
import re
from ConfigParser import SafeConfigParser

import time

from behave import model
from lxml import etree
from telnetlib import EC

from behave import *
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from wheel.signatures import assertTrue
from features.pages.page_selector import AddManager, GeneralLocator
import general_methods

config = SafeConfigParser()
config.read('settings.ini')
username = config.get('main', 'username')
psw = config.get('main', 'psw')

#Вводимо логін
@when("login ass owner")
def step(context):
    time.sleep(2)
    general_methods.login(context,email=username, password=psw)
    time.sleep(1)


@when('create "{text}" manager')
def step_impl(context, text):
    time.sleep(1)
    general_methods.create_managers(context, text)


@when('click on "{name}" in Menu')
def step_impl(context, name):
    time.sleep(1)
    context.browser.find_element(By.XPATH, './/a[text()="{}"]'.format(name)).click()
    time.sleep(1)


@given('website "{text}"')
def step_impl(context,text):
    context.browser.get(text)


@then("pagination is present")
def step_impl(context):
    assertTrue(general_methods.check_exists_by_xpath(context, ".//div[@id='pagination']"))


@when('click on pagination "{text}"')
def step_impl(context, text):
    context.browser.find_element(*GeneralLocator.PAGINATION_DROPDOWN).click()
    time.sleep(0.2)
    context.browser.find_element(By.XPATH, ".//div[text()='{}']".format(text)).click()
    time.sleep(5)


@then('managers list will be contain "{text}" users')
def step_impl(context, text):
    count_elements = int(len(context.browser.find_elements(*GeneralLocator.TABLE_BODY)))
    assert (int(text) == count_elements)


@when("click on any manager")
def step_impl(context):
    context.browser.find_element(*GeneralLocator.TABLE_FIRST).click()
    time.sleep(1)

user_info_edit = []

@when('change F-Name "{}", L-Name "{}", Phone "{}", Email "{}"')
def step_impl(context, fname, lname, phone, email):
    context.browser.find_element(*AddManager.F_NAME_SIDE_MENU).clear()
    context.browser.find_element(*AddManager.F_NAME_SIDE_MENU).send_keys(fname)
    context.browser.find_element(*AddManager.L_NAME_SIDE_MENU).clear()
    context.browser.find_element(*AddManager.L_NAME_SIDE_MENU).send_keys(lname)
    context.browser.find_element(*AddManager.PHONE_SIDE_MENU).clear()
    context.browser.find_element(*AddManager.PHONE_SIDE_MENU).send_keys(phone)
    context.browser.find_element(*AddManager.EMAIL_SIDE_MENU).clear()
    context.browser.find_element(*AddManager.EMAIL_SIDE_MENU).send_keys(email)
    user_info_edit.extend([fname, lname, phone, email])



@when("click on Save button")
def step_impl(context):
    context.browser.find_element(*AddManager.SAVE_EDITABLE_MANAGER).click()
    time.sleep(1)


@then("user profile was changed successfully")
def step_impl(context):
    context.browser.find_element(*GeneralLocator.SEARCH).send_keys(user_info_edit[0])
    context.browser.find_element(*GeneralLocator.SEARCH).send_keys(Keys.ENTER)
    time.sleep(2)
    ac = context.browser.find_element(*GeneralLocator.TABLE_FIRST).text
    user_info = ac.split("\n")
    user = [user_info_edit[0] + " " + user_info_edit[1], user_info_edit[2], user_info_edit[3]]
    user_info.pop(3)
    user.sort()
    user_info.sort()
    assert user == user_info

@when("delete all managers except owner")
def step_impl(context):
    i = 1
    while i < len(context.browser.find_elements(*GeneralLocator.TABLE_BODY)):
        #count = len(context.browser.find_elements(*GeneralLocator.TABLE_BODY))
        context.browser.find_element(*GeneralLocator.TABLE_FIRST).click()
        a = context.browser.find_element(By.XPATH, ".//div[@id='managerDetailsList']").get_attribute("class")
        if 'item disable-all' != a:
            context.browser.find_element(*AddManager.DELETE_MANAGER).click()
            time.sleep(0.5)
        else:
            context.browser.find_element(*GeneralLocator.TABLE_SECOND).click()
            context.browser.find_element(*AddManager.DELETE_MANAGER).click()
            time.sleep(0.5)
    time.sleep(2)

@when("delete all customers")
def step_impl(context):
    i = 1
    while i < len(context.browser.find_elements(*GeneralLocator.TABLE_BODY)):
        context.browser.find_element(*GeneralLocator.TABLE_FIRST).click()
        deleteBtn = WebDriverWait(context.browser, 20).until(
            EC.element_to_be_clickable((By.ID, "deleteCustomerBtn")))
        deleteBtn.click()

    time.sleep(2)


@when("create few managers")
def step_impl(context):
    for row in context.table:
        context.browser.find_element(*GeneralLocator.ADD_MANAGER_BTN).click()
        time.sleep(1)
        context.browser.find_element(*AddManager.F_NAME).send_keys(row["first"])
        context.browser.find_element(*AddManager.L_NAME).send_keys(row["last"])
        context.browser.find_element(*AddManager.PHONE).send_keys(row["phone"])
        context.browser.find_element(*AddManager.EMAIL).send_keys(row["email"])
        context.browser.find_element(*AddManager.PASSWORD).send_keys("Go1234")
        context.browser.find_element(*AddManager.CONFIRM_PASSWORD).send_keys("Go1234")
        context.browser.find_element(*AddManager.SAVE_NEW_MANAGER_BTN).click()
        time.sleep(1)

@then('verify that sort works correctly for "{name}" column')
def step_impl(context,name):
    general_methods.sort_by_column_name(context, name)


@when('try search "{name}"')
def step_impl(context, name):
    context.browser.find_element(*GeneralLocator.SEARCH).send_keys(name)
    context.browser.find_element(*GeneralLocator.SEARCH).send_keys(Keys.ENTER)

@then('list contain only "{name1}" and not contain "{name2}"')
def step_impl(context, name1, name2):
    time.sleep(1)
    search_result = context.browser.find_elements(*GeneralLocator.TABLE_BODY)
    search_array = []
    if not search_result:
        print ("List is empty")
    else:

        for i in search_result:
            a = i.text
            b = a.split("\n")
            search_array.append(b)
        assert (any(name1 in s for s in search_array))


@when("click on AddManager button")
def step_impl(context):
    context.browser.find_element(*GeneralLocator.ADD_MANAGER_BTN).click()
    time.sleep(1)


@when("click on Add Manager without any data")
def step_impl(context):
    time.sleep(0.5)
    context.browser.find_element(*AddManager.SAVE_NEW_MANAGER_BTN).click()
    #context.browser.find_element(*AddManager.SAVE_NEW_MANAGER_BTN).click()
    time.sleep(0.5)
@then('appears toast message "{toast}"')
def step_impl(context, toast):
    message = general_methods.getToastMessage(context)
    try:
        my = message.text
        print (my)
        assert toast == my
    except AttributeError:
        time.sleep(0.5)
        assert False

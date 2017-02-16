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
from features.pages.page_selector import AddManager, GeneralLocator, AddCustomer, AddWorker
import general_methods



@when('create "{text}" workers')
def step_impl(context, text):
    general_methods.create_workers(context, text)


@when("click on any worker")
def step_impl(context):
    try:
        context.browser.find_element(By.XPATH, ".//div[@id='tableBody']/div[1]").click()
        time.sleep(2)
    except:
        general_methods.create_workers(context,1)
        time.sleep(1)
        context.browser.find_element(By.XPATH, ".//div[@id='tableBody']/div[1]").click()
        time.sleep(2)


@when("click on Show Protocol button")
def step_impl(context):
    context.browser.find_element(*AddWorker.SHOW_PROTOCOL_BTN).click()


@when('click on "{name}" tab')
def step_impl(context, name):
    context.browser.find_element(By.XPATH, ".//ul[@class='control-list']/li[text()='{}']"
                                 .format(name)).click()
    time.sleep(1)


@when("click on Get Report button")
def step_impl(context):
    time.sleep(0.5)
    context.browser.find_element(*AddWorker.GET_REPORT_BTN).click()
    time.sleep(0.5)


@when("click on any worker by means of multiaction")
def step_impl(context):
    try:
        context.browser.find_element(By.XPATH, ".//div[@id='tableBody']/div[1]/div[1]/label").click()
        time.sleep(1)
        context.browser.find_element(*AddWorker.MULTIActionReportBtn).click()
        time.sleep(0.5)
    except:
        general_methods.create_workers(context,1)
        time.sleep(1)
        context.browser.find_element(By.XPATH, ".//div[@id='tableBody']/div[1]/div[1]/label").click()
        time.sleep(0.5)
        context.browser.find_element(*AddWorker.MULTIActionReportBtn).click()
        time.sleep(0.5)

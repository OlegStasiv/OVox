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



@when("delete all customers")
def step_impl(context):
    i = 1
    while i < len(context.browser.find_elements(*GeneralLocator.TABLE_BODY)):
        context.browser.find_element(*GeneralLocator.TABLE_FIRST).click()
        deleteBtn = WebDriverWait(context.browser, 20).until(
            EC.element_to_be_clickable((By.ID, "deleteCustomerBtn")))
        deleteBtn.click()

    time.sleep(2)


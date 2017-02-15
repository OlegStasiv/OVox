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



@when('create "{text}" workers')
def step_impl(context, text):
    general_methods.create_workers(context, text)
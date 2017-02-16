import time
from behave import *
from behave import when, then
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from wheel.signatures import assertTrue

from features.steps import general_methods
from features.pages.page_selector import AddManager, GeneralLocator, AddCustomer


@then("modal window appears")
def step(context):
    popup = context.browser.find_element(By.CLASS_NAME, 'modal-body')
    assertTrue(popup, "Pop up not appears")

@when("close popup")
def step(context):
    time.sleep(0.5)
    close = context.browser.find_element(By.ID, 'cancelPopup')
    close.click()
    time.sleep(0.5)

@then("modal window disappears")
def step(context):
    context.browser.implicitly_wait(2)
    try:
        context.browser.find_element(By.CLASS_NAME, 'modal-body')
    except:
        pass
import os
import random
import string
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from wheel.signatures import assertTrue
import json
from pprint import pprint
from features.pages.page_selector import LoginPageLocator, GeneralLocator, \
    AddManager
from selenium.webdriver.support import expected_conditions as EC


def login(context, email, password):
    context.browser.find_element(*LoginPageLocator.EMAIL_FIELD).send_keys(email)
    context.browser.find_element(*LoginPageLocator.PASSWORD_FIELD).send_keys(password)
    context.browser.find_element(*LoginPageLocator.SIGNIN_BUTTON).click()


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def create_managers(context, count):
    context.browser.find_element(*GeneralLocator.MENU_MANAGER).click()
    with open(ROOT_DIR + '/managers.json') as data_file:
        data = json.load(data_file)
    i = 0

    while i < int(count):
        context.browser.find_element(*GeneralLocator.ADD_MANAGER_BTN).click()
        time.sleep(1)
        context.browser.find_element(*AddManager.F_NAME).send_keys(data["data"][i][0])
        context.browser.find_element(*AddManager.L_NAME).send_keys(data["data"][i][1])
        context.browser.find_element(*AddManager.PHONE).send_keys(data["data"][i][2])
        context.browser.find_element(*AddManager.EMAIL).send_keys(data["data"][i][3])
        context.browser.find_element(*AddManager.PASSWORD).send_keys("Go1234")
        context.browser.find_element(*AddManager.CONFIRM_PASSWORD).send_keys("Go1234")
        context.browser.find_element(*AddManager.SAVE_NEW_MANAGER_BTN).click()
        time.sleep(1)
        i = i + 1

def create_customers(context, count):
    context.browser.find_element(*GeneralLocator.MENU_MANAGER).click()
    with open(ROOT_DIR + '/managers.json') as data_file:
        data = json.load(data_file)
    i = 0

    while i < int(count):
        context.browser.find_element(*GeneralLocator.ADD_MANAGER_BTN).click()
        time.sleep(1)
        context.browser.find_element(*AddManager.F_NAME).send_keys(data["data"][i][0])
        context.browser.find_element(*AddManager.L_NAME).send_keys(data["data"][i][1])
        context.browser.find_element(*AddManager.PHONE).send_keys(data["data"][i][2])
        context.browser.find_element(*AddManager.EMAIL).send_keys(data["data"][i][3])
        context.browser.find_element(*AddManager.PASSWORD).send_keys("Go1234")
        context.browser.find_element(*AddManager.CONFIRM_PASSWORD).send_keys("Go1234")
        context.browser.find_element(*AddManager.SAVE_NEW_MANAGER_BTN).click()
        time.sleep(1)
        i = i + 1


def generate_any_word(lenght_word_digit):
    from random import choice
    from string import lowercase
    n = lenght_word_digit

    string_val = "".join(choice(lowercase) for i in range(n))

    return string_val


def generate_digits(lenght_digit):
    from random import choice
    from string import lowercase
    n = lenght_digit

    string_val = "".join(choice(string.digits) for i in range(n))

    return string_val


def check_exists_by_xpath(context, xpath):
    try:
        context.browser.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True

def sort_by_column_name(context, name):

    context.browser.implicitly_wait(10)

    array = []
    get_index = context.browser.find_elements(By.XPATH, './/div[@class="table-head-row"]/div/span')
    for i in get_index:
        array.append(i.text)

    column = array.index(name)

    column_text = context.browser.find_element(By.XPATH,
                                 './/span[text()[contains(.,"{}")]]'.format(name))
    text_color = column_text.value_of_css_property('color')

    if (text_color == 'rgba(83, 83, 83, 1)'):
        context.browser.find_element(By.XPATH, './/span[text()[contains(.,"{}")]]'.format(name)).click()

    else:
        context.browser.find_element(By.XPATH, './/span[text()[contains(.,"{}")]]'.format(name)).click()
        context.browser.find_element(By.XPATH, './/span[text()[contains(.,"{}")]]'.format(name)).click()

    time.sleep(1)

    managers_list = context.browser.find_elements(By.XPATH, ".//div[@class='table-row']")

    all_managers_after_filter_by_name = []
    for i in managers_list:
        a = i.text
        b = a.split("\n")
        all_managers_after_filter_by_name.append(b[column])

    print(all_managers_after_filter_by_name)
    actual_result = sorted(all_managers_after_filter_by_name, reverse=True)
    assert all_managers_after_filter_by_name == actual_result


def getToastMessage(context):
    try:
        search_result = context.browser.find_element(*GeneralLocator.TOAST)
        return search_result
    except NoSuchElementException:
        time.sleep(0.5)

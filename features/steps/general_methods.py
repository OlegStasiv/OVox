import os
import random
import string
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from wheel.signatures import assertTrue
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from pprint import pprint
from features.pages.page_selector import LoginPageLocator, GeneralLocator, \
    AddManager, AddCustomer, AddWorker
from selenium.webdriver.support import expected_conditions as EC


def login(context, email, password):
    wait = WebDriverWait(context.browser, 10)
    wait.until(EC.element_to_be_clickable((LoginPageLocator.EMAIL_FIELD)))\
        .send_keys(email)
    wait.until(EC.element_to_be_clickable((LoginPageLocator.PASSWORD_FIELD)))\
        .send_keys(password)
    wait.until(EC.element_to_be_clickable((LoginPageLocator.SIGNIN_BUTTON)))\
        .click()

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def create_managers(context, count):
    wait = WebDriverWait(context.browser, 10)

    # wait.until(EC.element_located_to_be_selected((GeneralLocator.MENU_MANAGER))).click()
    # context.browser.find_element(*GeneralLocator.MENU_MANAGER).click()
    with open(ROOT_DIR + '/managers.json') as data_file:
        data = json.load(data_file)
    i = 0

    while i < int(count):
        time.sleep(0.3)
        context.browser.find_element(*GeneralLocator.ADD_MANAGER_BTN).click()
        wait.until(EC.presence_of_element_located((AddManager.F_NAME))).\
            send_keys(data["data"][i][0])
        context.browser.find_element(*AddManager.L_NAME).send_keys(data["data"][i][1])
        context.browser.find_element(*AddManager.PHONE).send_keys(data["data"][i][2])
        context.browser.find_element(*AddManager.EMAIL).send_keys(data["data"][i][3])
        context.browser.find_element(*AddManager.PASSWORD).send_keys("Go1234")
        context.browser.find_element(*AddManager.CONFIRM_PASSWORD).send_keys("Go1234")
        context.browser.find_element(*AddManager.SAVE_NEW_MANAGER_BTN).click()
        time.sleep(0.3)
        i = i + 1

def create_customers(context, count):
    context.browser.find_element(*GeneralLocator.MENU_CUSTOMER).click()
    with open(ROOT_DIR + '/customers.json') as data_file:
        data = json.load(data_file)
    i = 0

    while i < int(count):
        context.browser.find_element(*GeneralLocator.ADD_MANAGER_BTN).click()
        time.sleep(1)
        context.browser.find_element(*AddCustomer.COMPANY).send_keys(data[i]['company'])
        context.browser.find_element(*AddCustomer.VATIN).send_keys(data[i]['vatin'])
        context.browser.find_element(*AddCustomer.COUNTRY).send_keys(data[i]['country'])
        context.browser.find_element(*AddCustomer.CITY).send_keys(data[i]['city'])
        context.browser.find_element(*AddCustomer.STREET).send_keys(data[i]['street'])
        context.browser.find_element(*AddCustomer.HOUSE).send_keys(data[i]['house'])
        context.browser.find_element(*AddCustomer.PHONE).send_keys(data[i]['phone'])
        context.browser.find_element(*AddCustomer.SAVE_NEW_CUSTOMER_BTN).click()
        time.sleep(0.5)
        i = i + 1


def create_workers(context, count):
    context.browser.find_element(*GeneralLocator.MENU_WORKER).click()
    with open(ROOT_DIR + '/workers.json') as data_file:
        data = json.load(data_file)
    i = 0

    while i < int(count):
        context.browser.find_element(*GeneralLocator.ADD_MANAGER_BTN).click()
        time.sleep(1)
        context.browser.find_element(*AddWorker.FIRST_NAME).send_keys(data[i]['first'])
        context.browser.find_element(*AddWorker.LAST_NAME).send_keys(data[i]['last'])
        context.browser.find_element(*AddWorker.PHONE).send_keys(data[i]['phone'])
        context.browser.find_element(*AddWorker.DROPDOWN_LIST).click()
        context.browser.find_element(By.XPATH, ".//ul[@id='managerForNewWorker-menu']/li[2]").click()
        context.browser.find_element(*AddWorker.SAVE_NEW_WORKER_BTN).click()
        time.sleep(0.5)
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

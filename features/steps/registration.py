import json
import time
from behave import given, when, then

#from dbfolder.writeToFile import write_to_file
from dbfolder.writeToFile import write_to_file
from features.pages.page_selector import LoginPageLocator, SignUpLocator, GeneralLocator
from features.steps.general_methods import generate_any_word, generate_digits


@when("click on Sign up tab")
def step(context):
    context.browser.find_element(*SignUpLocator.SIGNUP_BTN).click()

company = generate_any_word(15)
vatin = generate_digits(16)
firstname = generate_any_word(8)
lastname = generate_any_word(8)
phonenumber = generate_digits(11)
postalcode = generate_digits(5)
email = '{}@gmail.com'.format(generate_any_word(8))
street = generate_any_word(8)
housenumber = generate_digits(3)
fax = generate_digits(7)

@when("fill all fields with valid data")
def step_impl(context):
    context.browser.find_element(*SignUpLocator.COMPANY_NAME).send_keys(company)
    context.browser.find_element(*SignUpLocator.VATIN).send_keys(vatin)
    context.browser.find_element(*SignUpLocator.FIRSTNAME).send_keys(firstname)
    context.browser.find_element(*SignUpLocator.LASTNAME).send_keys(lastname)
    context.browser.find_element(*SignUpLocator.COUNTRY).send_keys("Ukraine")
    context.browser.find_element(*SignUpLocator.PHONENUMBER).send_keys(phonenumber)
    context.browser.find_element(*SignUpLocator.CITY).send_keys("Mukachevo")
    context.browser.find_element(*SignUpLocator.POSTALCODE).send_keys(postalcode)
    context.browser.find_element(*SignUpLocator.EMAIL).send_keys(email)
    context.browser.find_element(*SignUpLocator.STREET).send_keys(street)
    context.browser.find_element(*SignUpLocator.HOUSENUMBER).send_keys(housenumber)
    context.browser.find_element(*SignUpLocator.PASSWORD).send_keys("Go1234")
    context.browser.find_element(*SignUpLocator.CONFIRMPASSWORD).send_keys("Go1234")
    context.browser.find_element(*SignUpLocator.FAX).send_keys(fax)


@when("click on Signup button")
def step_impl(context):
    context.browser.find_element(*SignUpLocator.SIGNUP).click()
    time.sleep(2)


@when("click on Setting Profile")
def step_impl(context):
    context.browser.find_element(*GeneralLocator.PROFILE_DROPDOWN).click()
    context.browser.find_element(*GeneralLocator.SETTINGS).click()
    time.sleep(1)


@then("all data is correct")
def step_impl(context):
    get_company = context.browser.find_element(*SignUpLocator.COMPANY_NAME).get_attribute('value')
    assert company == get_company
    get_phone = context.browser.find_element(*SignUpLocator.PHONENUMBER).get_attribute('value')
    assert phonenumber == get_phone
    get_vatin = context.browser.find_element(*SignUpLocator.VATIN).get_attribute('value')
    assert vatin == get_vatin
    get_country = context.browser.find_element(*SignUpLocator.COUNTRY).get_attribute('value')
    assert "Ukraine" == get_country
    get_fax = context.browser.find_element(*SignUpLocator.FAX).get_attribute('value')
    assert fax == get_fax
    get_email = context.browser.find_element(*SignUpLocator.EMAIL).get_attribute('value')
    assert email == get_email
    get_city = context.browser.find_element(*SignUpLocator.CITY).get_attribute('value')
    assert "Mukachevo" == get_city
    get_postal = context.browser.find_element(*SignUpLocator.POSTALCODE).get_attribute('value')
    assert postalcode == get_postal
    get_street = context.browser.find_element(*SignUpLocator.STREET).get_attribute('value')
    assert street == get_street
    get_house = context.browser.find_element(*SignUpLocator.HOUSENUMBER).get_attribute('value')
    assert housenumber == get_house
    get_fname = context.browser.find_element(*SignUpLocator.FIRSTNAME).get_attribute('value')
    assert firstname == get_fname
    get_lname = context.browser.find_element(*SignUpLocator.LASTNAME).get_attribute('value')
    assert lastname == get_lname
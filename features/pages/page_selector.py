from selenium.webdriver.common.by import By


class LoginPageLocator(object):

    EMAIL_FIELD = (By.ID, 'signInEmail')
    PASSWORD_FIELD = (By.ID, "signInPassword")
    SIGNIN_BUTTON = (By.ID, "logInBtn")

class AddManager(object):
    F_NAME = (By.ID, 'firstNameForNewManager')
    F_NAME_SIDE_MENU = (By.ID, 'firstName')
    L_NAME = (By.ID, 'lastNameForNewManager')
    L_NAME_SIDE_MENU = (By.ID, 'lastName')
    PHONE = (By.ID, 'phoneNumberForNewManager')
    PHONE_SIDE_MENU = (By.ID, 'phoneNumber')
    EMAIL = (By.ID, 'emailForNewManager')
    EMAIL_SIDE_MENU = (By.ID, 'email')
    PASSWORD = (By.ID, 'passwordForNewManager')
    CONFIRM_PASSWORD = (By.ID, 'confirmPasswordForNewManager')
    SAVE_NEW_MANAGER_BTN = (By.ID, 'saveNewManagerBtn')
    SAVE_EDITABLE_MANAGER = (By.ID, 'editManagerBtn')
    MANAGERS_DATA_LIST_CLASS = (By.XPATH, ".//div[@id='managerDetailsList']")
    DELETE_MANAGER = (By.ID, 'deleteManagerBtn')

class AddCustomer(object):
    COMPANY = (By.ID, 'companyNameForNewCustomer')
    VATIN = (By.ID, 'VATINForNewCustomer')
    COUNTRY = (By.ID, 'countryForNewCustomer')
    CITY = (By.ID, 'cityForNewCustomer')
    STREET = (By.ID, 'streetForNewCustomer')
    HOUSE = (By.ID, 'houseNumberForNewCustomer')
    PHONE = (By.ID, 'phoneNumberForNewCustomer')
    SAVE_NEW_CUSTOMER_BTN = (By.ID, 'saveNewCustomerBtn')
    COMPANY_SIDE_MENU = (By.ID, 'companyName')
    PHONE_SIDE_MENU = (By.ID, 'phoneNumber')
    COUNTRY_SIDE_MENU = (By.ID, 'country')
    CITY_SIDE_MENU = (By.ID, 'city')
    STREET_SIDE_MENU = (By.ID, 'street')
    HOUSE_SIDE_MENU = (By.ID, 'houseNumber')
    VATIN_SIDE_MENU = (By.ID, 'VATIN')
    SAVE_EDITABLE_CUSTOMER = (By.ID, 'editCustomerBtn')

class AddWorker(object):
    FIRST_NAME = (By.ID, 'firstNameForNewWorker')
    LAST_NAME = (By.ID, 'lastNameForNewWorker')
    PHONE = (By.ID, 'phoneNumberForNewWorker')
    SAVE_NEW_WORKER_BTN = (By.ID, 'saveNewWorkerBtn')
    DROPDOWN_LIST = (By.ID, 'managerForNewWorker-button')



class GeneralLocator(object):
    MENU_MANAGER = (By.XPATH, './/a[text()="Managers"]')
    MENU_CUSTOMER = (By.XPATH, './/a[text()="Customers"]')
    MENU_WORKER = (By.XPATH, './/a[text()="Workers"]')
    ADD_MANAGER_BTN = (By.ID, 'showAddBtn')
    PROFILE_DROPDOWN = (By.ID, 'menuDropBtn')
    SETTINGS = (By.XPATH, './/a[text()[contains(.,"Settings")]]')
    PAGINATION_ELEMENT = (By.XPATH, 'pagination')
    PAGINATION_DROPDOWN = (By.XPATH, './/div[@id="pagination"]/div/div[1]/div')
    FIFTY = (By.XPATH, ".//ul[@id='ui-id-23-menu']/li[3]")
    TABLE_BODY = (By.XPATH, './/div[@id="tableBody"]/div')
    TABLE_FIRST = (By.XPATH, './/div[@id="tableBody"]/div[1]')
    TABLE_SECOND = (By.XPATH, './/div[@id="tableBody"]/div[2]')
    SEARCH = (By.ID, 'searchContainer')
    TOAST = (By.CLASS_NAME, 'toast-message')



class SignUpLocator(object):
    SIGNUP_BTN = (By.ID, 'signUpLink')
    COMPANY_NAME = (By.ID, 'companyName')
    VATIN = (By.ID, 'VATIN')
    COUNTRY = (By.ID, 'country')
    CITY = (By.ID, 'city')
    POSTALCODE = (By.ID, 'postalCode')
    STREET = (By.ID, 'street')
    HOUSENUMBER = (By.ID, 'houseNumber')
    FAX = (By.ID, 'fax')
    FIRSTNAME = (By.ID, 'firstName')
    LASTNAME = (By.ID, 'lastName')
    PHONENUMBER = (By.ID, 'phoneNumber')
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'password')
    CONFIRMPASSWORD = (By.ID, 'confirmPassword')
    SIGNUP = (By.ID, 'signUpBtn')

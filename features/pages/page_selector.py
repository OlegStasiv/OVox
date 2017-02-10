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

class GeneralLocator(object):
    MENU_MANAGER = (By.XPATH, './/a[text()="Managers"]')
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

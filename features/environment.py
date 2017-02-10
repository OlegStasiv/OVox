import os
from pyvirtualdisplay import Display, display
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def before_scenario(context, scenario):

    #display = Display(visible=1, size=(1280, 720))

    #display.start()
    context.browser = webdriver.Chrome(executable_path='{}/chromedriver'.format(os.getcwd()))
    #context.browser = webdriver.Chrome(executable_path='{}/chromedriver'.format(os.getcwd()))
    # context.browser = webdriver.Chrome() if you have set chromedriver in your PATH

    context.browser.set_page_load_timeout(300)
    context.browser.implicitly_wait(20)
    context.browser.maximize_window()


def after_scenario(context, scenario):
    context.browser.close()

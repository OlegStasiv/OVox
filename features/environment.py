import os
from pyvirtualdisplay import Display, display
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def before_scenario(context, scenario):
    # xf = Xvfb(1920, 1080)  # xf = Xvfb(1920, 1080) - will create virtual display with 1920x1080 size
    # xf.start()
    display = Display(visible=1, size=(1280, 768))
    display.start()
    context.browser = webdriver.Chrome(executable_path='{}/chromedriver'.format(os.getcwd()))
    #context.browser = webdriver.Chrome(executable_path='{}/chromedriver'.format(os.getcwd()))
    # context.browser = webdriver.Chrome() if you have set chromedriver in your PATH

    context.browser.set_page_load_timeout(300)
    context.browser.implicitly_wait(20)
    context.browser.set_window_size(1280, 768)
    context.browser.maximize_window()


def after_scenario(context, scenario):
    context.browser.close()

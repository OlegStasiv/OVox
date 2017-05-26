import os

from pyvirtualdisplay import Display
from selenium import webdriver
from youtrack.connection import Connection

def before_scenario(context, scenario):
    # xf = Xvfb(1920, 1080)  # xf = Xvfb(1920, 1080) - will create virtual display with 1920x1080 size
    # xf.start()
    display = Display(visible=1, size=(1300, 720))
    display.start()
    context.browser = webdriver.Chrome(executable_path='{}/chromedriver'.format(os.getcwd()))
    #context.browser = webdriver.Chrome(executable_path='{}/chromedriver'.format(os.getcwd()))
    # context.browser = webdriver.Chrome() if you have set chromedriver in your PATH

    context.browser.set_page_load_timeout(300)
    context.browser.implicitly_wait(15)
    context.browser.set_window_size(1300, 720)
    context.browser.maximize_window()

# def after_scenario(context, scenario):
#     if scenario.status == "failed":
#         connection = Connection('http://45.32.154.169:8080', 'oleg.stasiv@thinkmobiles.com', 'Seatao5803axleon87')
#         # connection.getIssue('omv-194')
#         descript = []
#         n = "\n"
#         for i in scenario.steps:
#             line = i.name
#             descript.append(line)
#         issue_description = '\n'.join(descript)
#         filterr = scenario.name
#         data = connection.getIssues('omv', scenario.name, 0, 5)
#         # data = connection.getAllIssues('omv', filterr, 0, 5)
#         if not data:
#             print("Creating issue...")
#             response_issue = connection.createIssue('omv', '', scenario.name, issue_description, type='Bug')
#             issue_dict = dict(response_issue[0])
#             issue_id = str(issue_dict['location']).split('/')[-1]
#             print (issue_id)
#
#             #Get files names
#             filse_name = []
#             for file in os.listdir("features/steps/screenshots/"):
#                 if file.endswith(".png"):
#                     filse_name.append(file.split('.')[0])
#             #End
#             if scenario.name in filse_name:
#                 f = open('features/steps/screenshots/{}.png'.format(scenario.name))
#
#             connection.createAttachment(issue_id, 'screen.png', f)
#             print ("add aachment")
#         else:
#             pass



    # context.browser.close()

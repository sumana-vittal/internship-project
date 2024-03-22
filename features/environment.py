import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from app.application import Application

# Change the browser value to "chrome" or "firefox" or "headless" to execute in that environment
browser = "headless"


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    # if browser.lower() == "chrome":
    #     driver_path = ChromeDriverManager().install()
    #     service = Service(driver_path)
    #     context.driver = webdriver.Chrome(service=service)
    # elif browser.lower() == "firefox":
    #     driver_path = GeckoDriverManager().install()
    #     service = Service(driver_path)
    #     context.driver = webdriver.Firefox(service=service)
    # elif browser.lower() == "headless":
    #     options = webdriver.ChromeOptions()
    #     options.add_argument("headless")
    #     options.add_argument("window-size=1920,1080")
    #     service = Service(ChromeDriverManager().install())
    #     context.driver = webdriver.Chrome(
    #         options=options,
    #         service=service
    #     )
    # else:
    #     print("Please provide the valid browser name")

    ###BrOWSERSTACK -runing testcases on cloud###
    bs_user = "mashka_t1wvgX"
    bs_key = "zDWkbUj7bhMyPsXx1Ds2"
    url = f"https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub"

    options = Options()
    bstack_options = {
        'os': 'Windows',
        'osVersion': '11',
        'browserName': 'Firefox',
        'sessionName': scenario_name
    }

    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()

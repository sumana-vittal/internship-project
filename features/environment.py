import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from app.application import Application

# Change the browser value to "chrome" or "firefox" or "headless" to execute in that environment
browser = "chrome"


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    :scenario_name: Scenario Name
    """

    if browser.lower() == "chrome":
        driver_path = ChromeDriverManager().install()
        service = Service(driver_path)
        context.driver = webdriver.Chrome(service=service)
    elif browser.lower() == "firefox":
        driver_path = GeckoDriverManager().install()
        service = Service(driver_path)
        context.driver = webdriver.Firefox(service=service)
    elif browser.lower() == "headless":
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("window-size=1920,1080")
        service = Service(ChromeDriverManager().install())
        context.driver = webdriver.Chrome(
            options=options,
            service=service
        )
    else:
        print("Invalid browser")
        context.driver.quit()

    ###BrOWSERSTACK -runing testcases on cloud###
    # bs_user = "mashka_t1wvgX"
    # bs_key = "zDWkbUj7bhMyPsXx1Ds2"
    # url = f"https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub"
    #
    # options = Options()

    ### Desktop web capability for browser stack ####
    # bstack_options = {
    #     # 'os': 'Windows',
    #     # 'osVersion': '11',
    #     # 'browserName': 'Firefox',
    #     # 'sessionName': scenario_name
    # }

    ### Mobile Emulation web capability for browser stack ####
    # bstack_options = {
    #     "platformName": "android",
    #     "platformVersion": "9.0",
    #     "deviceName": "Google Pixel 3",
    #     "sessionName": scenario_name
    # }

    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    ### SETTINGS FOR THE MOBILE EMULATION ###
    # options = webdriver.ChromeOptions()
    # mobile_emulation = {
    #     "deviceMetrics": {"width": 411, "height": 731, "pixelRatio": 1.0, "mobile": True, "deviceScaleFactor": 50},
    #     "userAgent": "Mozilla/5.0 (Linux; Android 9; Pixel 2 Build/PPR1.180610.009) AppleWebKit/537.36 "
    #                  "(KHTML, like Gecko) Chrome/22.0.6261.112 Mobile Safari/537.36"}
    #
    # options.add_experimental_option("mobileEmulation", mobile_emulation)
    # options.add_argument("--log-level=3")
    # options.add_argument("--window-size=411,980")
    # context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

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

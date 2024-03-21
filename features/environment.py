import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from app.application import Application

# Change the browser value to "chrome" or "firefox" or "headless" to execute in that environment
browser = "headless"


def browser_init(context):
    """
    :param context: Behave context
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
        print("Please provide the valid browser name")

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    context.app = Application(context.driver)


# def pytest_adoption(parser):
#     parser.adoption("--browser")
#
#
# @pytest.fixture(scope="class", autouse=True)
# def browser(request):
#     return request.config.getoption("--browser")


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()

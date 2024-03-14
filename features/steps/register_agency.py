from time import sleep
from behave import given, when, then


@given('Open the main page')
def open_home_page(context):
    context.app.register_agency.open_home_page()


@when("Click on the sign in")
def click_sign_in(context):
    context.app.register_agency.click_sign_in()


@when("Log in to the page.")
def login_page(context):
    context.app.register_agency.login_details_and_click()


@when('Click on "Connect the company".')
def click_connect_company_btn(context):
    # store the original window
    context.original_window = context.driver.current_window_handle
    context.app.register_agency.click_connect_company()


@when("Switch the new tab")
def switch_new_tab(context):
    context.app.register_agency.switch_new_tab()


@when("Enter some test information in the form")
def enter_information(context):
    context.app.register_agency.enter_information()


@then("Verify the right information is present")
def verify_information(context):
    context.app.register_agency.verify_information()


@then('verify "send request" button is available and clickable')
def verify_request_button(context):
    context.app.register_agency.verify_request_button()


@then('Verify "buy a subscription" button is available and clickable')
def verify_buy_subscription(context):
    context.app.register_agency.verify_buy_subscription()

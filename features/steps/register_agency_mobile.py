from time import sleep
from behave import given, when, then


@when('Click on User profile image')
def click_user_profile(context):
    context.app.register_agency_mobile.click_user_profile()


@when('Click on user setting "Connect the company".')
def click_connect_company_btn(context):
    # store the original window
    context.original_window = context.driver.current_window_handle
    context.app.register_agency_mobile.click_user_profile_connect_company()

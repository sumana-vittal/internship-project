from behave import given, when, then


@when('Click on settings option.')
def click_settings(context):
    context.app.contact_us_page.click_settings()


@when('Click on Contact us option.')
def click_contact_us(context):
    context.app.contact_us_page.click_contact_us()


@then('Verify the contact us page opens.')
def verify_contact_us(context):
    context.app.contact_us_page.verify_contact_us()


@then('Verify there are at least 4 social media icons.')
def verify_social_icons(context):
    context.app.contact_us_page.verify_social_icons()


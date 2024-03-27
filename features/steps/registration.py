from behave import given, when, then


@when('Enter some test information in the input fields.')
def input_create_account_information(context):
    context.app.registration_page.input_create_account_information()


@then('Verify the right information is present.')
def verify_input_data(context):
    context.app.registration_page.verify_input_data()